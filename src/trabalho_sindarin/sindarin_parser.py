import ply.yacc as yacc
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from graphviz import Digraph
from ply.yacc import YaccProduction

from .sindarin_dict import sindarin_dict
from .sindarin_lexer import tokens

precedence = (("left", "CONJUNCTION"),)


def p_sentence_simple(p: YaccProduction):
    """sentence : ARTICLE NOUN"""
    print("oi")
    print(p)
    print(type(p))
    p[0] = Node("S", children=[Node("A", children=[Node(p[1])]), Node("N", children=[Node(p[2])])])


def p_sentence_noun_verb(p):
    """sentence : ARTICLE NOUN VERB"""
    p[0] = Node(
        "S",
        children=[
            Node("A", children=[Node(p[1])]),
            Node("N", children=[Node(p[2])]),
            Node("V", children=[Node(p[3])]),
        ],
    )


def p_sentence_noun_verb_prep_noun(p):
    """sentence : ARTICLE NOUN VERB prepositional_phrase"""
    p[0] = Node(
        "S",
        children=[
            Node("A", children=[Node(p[1])]),
            Node("N", children=[Node(p[2])]),
            Node("V", children=[Node(p[3])]),
            p[4],  # Attach the prepositional phrase node
        ],
    )


def p_prepositional_phrase(p: YaccProduction):
    """prepositional_phrase : PREPOSITION ARTICLE NOUN"""
    p[0] = Node(
        "P",
        children=[Node(p[1]), Node("A", children=[Node(p[2])]), Node("N", children=[Node(p[3])])],
    )


def p_sentence_conjunction(p: YaccProduction):
    """sentence : sentence CONJUNCTION sentence"""
    p[0] = Node(
        "S",
        children=[
            p[1],  # First sentence
            Node("C", children=[Node(p[2]), p[3]]),  # Conjunction with second sentence
        ],
    )


def p_error(p: YaccProduction):
    print("Syntax error in input!")


parser = yacc.yacc()


def visualize_tree(root, show_elvish=False):
    dot = Digraph(format="png")

    elvish_dict = {value: key for key, value in sindarin_dict.items()}

    def add_nodes_edges(node, parent_id=None):
        node_id = str(id(node))

        if show_elvish and not node.children:
            english_word = node.name
            elvish_word = elvish_dict.get(english_word)

            dot.node(node_id, elvish_word, shape="ellipse", color="blue")

            english_id = node_id + "_eng"
            dot.node(english_id, english_word, shape="rectangle", color="green")

            dot.edge(node_id, english_id, style="dashed", color="gray")
        else:
            dot.node(node_id, node.name)

        if parent_id:
            dot.edge(parent_id, node_id)

        for child in node.children:
            add_nodes_edges(child, node_id)

    # def add_nodes_edges(node: Node):
    #     node_id = str(id(node))
    #     dot.node(node_id, node.name)
    #     for child in node.children:
    #         dot.edge(node_id, str(id(child)))
    #         add_nodes_edges(child)

    add_nodes_edges(root)
    filepath = dot.render("tree_visualization_sentence")
    print(f"Tree visualizations saved as {filepath} and tree_visualization_sentence.png")


def parse_and_show_tree(sentence, show_elvish=False):
    result = parser.parse(sentence)

    if result is None:
        return

    print("\nParse Tree (Text Representation):")
    for pre, _, node in RenderTree(result):
        print(f"{pre}{node.name}")

    visualize_tree(result, show_elvish=show_elvish)


if __name__ == "__main__":
    while True:
        try:
            s = input("Sindarin > ")
        except EOFError:
            break
        except KeyboardInterrupt:
            print()
            break
        if not s:
            continue
        parse_and_show_tree(s, show_elvish=True)
