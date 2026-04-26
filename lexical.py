# =========================================
# LEXICAL ANALYZER (Production Level)
# =========================================

import re


class Token:
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"{self.type}({self.value})"


class LexerError(Exception):
    pass


class Lexer:
    KEYWORDS = {"int"}
    TOKEN_SPEC = [
        ("NUMBER",   r'\d+'),
        ("ID",       r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ("OP",       r'[+\-*/=]'),
        ("SEMI",     r';'),
        ("SKIP",     r'[ \t]+'),
        ("NEWLINE",  r'\n'),
        ("MISMATCH", r'.'),
    ]

    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        regex = '|'.join(f'(?P<{name}>{pattern})'
                         for name, pattern in self.TOKEN_SPEC)

        line_num = 1
        line_start = 0

        for match in re.finditer(regex, self.code):
            kind = match.lastgroup
            value = match.group()
            column = match.start() - line_start

            if kind == "NUMBER":
                token = Token("NUMBER", value, line_num, column)

            elif kind == "ID":
                if value in self.KEYWORDS:
                    token = Token("KEYWORD", value, line_num, column)
                else:
                    token = Token("IDENTIFIER", value, line_num, column)

            elif kind == "OP":
                token = Token("OPERATOR", value, line_num, column)

            elif kind == "SEMI":
                token = Token("SEMICOLON", value, line_num, column)

            elif kind == "NEWLINE":
                line_num += 1
                line_start = match.end()
                continue

            elif kind == "SKIP":
                continue

            elif kind == "MISMATCH":
                raise LexerError(f"Unexpected character '{value}' at line {line_num}")

            self.tokens.append(token)

        return self.tokens