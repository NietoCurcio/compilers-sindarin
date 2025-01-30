import ply.lex as lex

tokens = ("ARTICLE", "NOUN", "VERB", "PREPOSITION")

# Dictionary for translation
sindarin_dict = {
    "i": "the",
    "in": "the (plural)",
    "na": "to",
    "o": "from",
    "nor": "run",
    "galad": "light",
    "adar": "father",
}


def t_ARTICLE(t):
    r"i|in"
    t.value = sindarin_dict[t.value]
    return t


def t_PREPOSITION(t):
    r"na|o"
    t.value = sindarin_dict[t.value]
    return t


def t_VERB(t):
    r"nor"
    t.value = sindarin_dict[t.value]
    return t


def t_NOUN(t):
    r"galad|adar"
    t.value = sindarin_dict[t.value]
    return t


t_ignore = " \t\n"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    lexer.input("i galad nor na adar")
    for tok in lexer:
        print(tok)
