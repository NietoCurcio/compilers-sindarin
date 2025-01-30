import ply.yacc as yacc
from anytree import Node, RenderTree

from .sindarin_lexer import tokens

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
    """sentence : ARTICLE NOUN VERB PREPOSITION ARTICLE NOUN"""
    p[0] = Node(
        "S",
        children=[
            Node("A", children=[Node(p[1])]),
            Node("N", children=[Node(p[2])]),
            Node("V", children=[Node(p[3])]),
            Node(
                "P",
                children=[
                    Node(p[4]),  # Preposition (na, o)
                    Node("A", children=[Node(p[5])]),  # Article (i, in)
                    Node("N", children=[Node(p[6])]),  # Noun (galad, adar)
                ],
            ),
        ],
    )


# ✅ New Rule: Allow multiple sentences joined by "a" (Conjunction)
def p_sentence_conjunction(p):
    """sentence : sentence CONJUNCTION sentence"""
    p[0] = Node(
        "S",
        children=[
            p[1],  # First sentence
            Node("C", children=[Node(p[2]), p[3]]),  # Conjunction with second sentence
        ],
    )


def p_prepositional_phrase(p):
    """prepositional_phrase : PREPOSITION ARTICLE NOUN"""
    p[0] = Node(
        "P",
        children=[Node(p[1]), Node("A", children=[Node(p[2])]), Node("N", children=[Node(p[3])])],
    )


def p_error(p):
    print("Syntax error in input!")


parser = yacc.yacc()


# === Function to Display Parse Tree ===
def parse_and_show_tree(sentence):
    result = parser.parse(sentence)

    if result:
        for pre, _, node in RenderTree(result):
            print("%s%s" % (pre, node.name))


if __name__ == "__main__":
    while True:
        try:
            s = input("Sindarin > ")
        except EOFError:
            break
        if not s:
            continue
        print("\nParse Tree:")
        parse_and_show_tree(s)
