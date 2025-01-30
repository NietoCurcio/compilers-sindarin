import ply.lex as lex

# Define tokens
tokens = ("WORD", "ARTICLE", "PREPOSITION")

# Simple Sindarin-to-English dictionary
sindarin_dict = {
    "i": "the",
    "na": "to",
    "ed": "out of",
    "gwaen": "I go",
    "galad": "light",
}


# Token rules
def t_ARTICLE(t):
    r"i"
    t.value = sindarin_dict.get(t.value, t.value)
    return t


def t_PREPOSITION(t):
    r"na|ed"
    t.value = sindarin_dict.get(t.value, t.value)
    return t


def t_WORD(t):
    r"[a-zA-Z]+"
    t.value = sindarin_dict.get(t.value, t.value)
    return t


# Ignore spaces and newlines
t_ignore = " \t\n"


# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test
if __name__ == "__main__":
    lexer.input("i na galad gwaen")
    for tok in lexer:
        print(tok)
