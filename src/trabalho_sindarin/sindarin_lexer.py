import ply.lex as lex

tokens = ("ARTICLE", "NOUN", "VERB", "PREPOSITION", "CONJUNCTION")

# Dictionary for translation
sindarin_dict = {
    "i": "the",
    "in": "the (plural)",
    "na": "to",
    "o": "from",
    "nor": "run",
    "galad": "light",
    "adar": "father",
    "arwen": "Arwen",
    "valinor": "Valinor",
    "edhel": "elf",
    "a": "and",  # Conjunction
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
    r"galad|adar|arwen|valinor|edhel"
    t.value = sindarin_dict[t.value]
    return t


def t_CONJUNCTION(t):
    r"a"
    t.value = sindarin_dict[t.value]
    return t


t_ignore = " \t\n"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    lexer.input("i arwen nor o i valinor")
    for tok in lexer:
        print(tok)
