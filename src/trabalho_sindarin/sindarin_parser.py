import ply.yacc as yacc
from anytree import Node, RenderTree
from graphviz import Digraph

from .sindarin_lexer import tokens

# ✅ FIX: Define precedence to resolve shift/reduce conflict
precedence = (
    ("left", "CONJUNCTION"),  # Process conjunctions last (lowest precedence)
)

# === Grammar Rules ===


def p_sentence_simple(p):
    """sentence : ARTICLE NOUN"""
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


def p_prepositional_phrase(p):
    """prepositional_phrase : PREPOSITION ARTICLE NOUN"""
    p[0] = Node(
        "P",
        children=[Node(p[1]), Node("A", children=[Node(p[2])]), Node("N", children=[Node(p[3])])],
    )


# ✅ Ensure conjunctions are parsed **after** complete sentences
def p_sentence_conjunction(p):
    """sentence : sentence CONJUNCTION sentence"""
    p[0] = Node(
        "S",
        children=[
            p[1],  # First sentence
            Node("C", children=[Node(p[2]), p[3]]),  # Conjunction with second sentence
        ],
    )


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()


# === Function to Display Parse Tree with Graphviz ===
def visualize_tree(root, filename="parse_tree"):
    """Generates a visual tree using Graphviz"""
    dot = Digraph(format="png")

    def add_nodes_edges(node, parent_id=None):
        node_id = str(id(node))
        dot.node(node_id, node.name)  # Create node

        if parent_id:
            dot.edge(parent_id, node_id)  # Link nodes

        for child in node.children:
            add_nodes_edges(child, node_id)

    add_nodes_edges(root)  # Start recursion
    filepath = dot.render(filename)
    print(f"Tree visualization saved as {filepath}")


def parse_and_show_tree(sentence):
    result = parser.parse(sentence)

    if result:
        print("\nParse Tree (Text Representation):")
        for pre, _, node in RenderTree(result):
            print("%s%s" % (pre, node.name))

        visualize_tree(result)  # Generate graphical visualization


if __name__ == "__main__":
    while True:
        try:
            s = input("Sindarin > ")
        except EOFError:
            break
        if not s:
            continue
        parse_and_show_tree(s)
