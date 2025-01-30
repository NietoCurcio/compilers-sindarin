import ply.yacc as yacc

from trabalho_sindarin.sindarin_lexer import tokens  # Import the tokens from our lexer


# Parsing rules
def p_sentence(p):
    """sentence : ARTICLE WORD WORD
    | WORD ARTICLE WORD
    | WORD PREPOSITION WORD"""
    p[0] = " ".join(p[1:])


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

# Test
if __name__ == "__main__":
    while True:
        try:
            s = input("Sindarin > ")
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        print("English:", result)
