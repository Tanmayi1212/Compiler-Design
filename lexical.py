import re
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    line: int


TOKEN_SPEC = [
    ("LET", r"let\b"),
    ("SHOW", r"show\b"),
    ("PLUS", r"plus\b"),
    ("ARROW", r"->"),
    ("NUMBER", r"\d+"),
    ("IDENTIFIER", r"[a-zA-Z_]\w*"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
    ("MISMATCH", r"."),
]


class Lexer:
    def __init__(self, code):
        self.code = code

    def tokenize(self):
        tokens = []
        line = 1

        regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC)

        for match in re.finditer(regex, self.code):
            name = match.lastgroup
            value = match.group()

            if name == "NEWLINE":
                line += 1
            elif name == "SKIP":
                continue
            elif name == "MISMATCH":
                raise SyntaxError(f"Unexpected character '{value}' at line {line}")
            else:
                tokens.append(Token(name, value, line))

        return tokens