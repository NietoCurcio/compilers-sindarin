from typing import cast

import ply.lex as lex
from ply.lex import LexToken

tokens = ("ARTICLE", "NOUN", "VERB", "PREPOSITION", "CONJUNCTION")

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
    "a": "and",
}


def t_ARTICLE(t: LexToken) -> LexToken:
    r"i|in"
    t.value = sindarin_dict[t.value]
    return t


def t_PREPOSITION(t: LexToken) -> LexToken:
    r"na|o"
    t.value = sindarin_dict[t.value]
    return t


def t_VERB(t: LexToken) -> LexToken:
    r"nor"
    # noro
    # norn
    t.value = sindarin_dict[t.value]
    return t


def t_NOUN(t: LexToken) -> LexToken:
    r"galad|adar|arwen|valinor|edhel"
    t.value = sindarin_dict[t.value]
    return t


def t_CONJUNCTION(t: LexToken) -> LexToken:
    r"a"
    t.value = sindarin_dict[t.value]
    return t


t_ignore = " \t\n"


def t_error(t: LexToken) -> None:
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == "__main__":
    lexer.input("i arwen nor o i valinor")
    # lexer.input("felipe")
    for token in lexer:
        token = cast(LexToken, token)
        print(token)
        print(token.value)
        print(token.lineno)
        print(token.lexpos)
        print()
        # lineno: The line number on which the token was found.
        # lexpos: The position of the token in the input string.
