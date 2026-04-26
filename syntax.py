# =========================================
# SYNTAX ANALYZER
# (Runs independently with sample input)
# =========================================

from lexical import Lexer


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, expected_type, expected_value=None):
        token = self.current()

        if token is None:
            raise Exception("Syntax Error: Unexpected end")

        if token.type != expected_type:
            raise Exception(f"Syntax Error: Expected {expected_type}, got {token.type}")

        if expected_value and token.value != expected_value:
            raise Exception(f"Syntax Error: Expected '{expected_value}', got '{token.value}'")

        self.pos += 1
        return token

    def parse(self):
        result = []

        while self.current() is not None:
            token = self.current()

            if token.type == "KEYWORD":
                result.append(self.parse_declaration())

            elif token.type == "IDENTIFIER":
                result.append(self.parse_assignment())

            else:
                raise Exception(f"Syntax Error: Invalid start {token}")

        return result

    def parse_declaration(self):
        self.eat("KEYWORD", "int")
        var = self.eat("IDENTIFIER").value
        self.eat("SEMICOLON")

        return ('declare', 'int', var)

    def parse_assignment(self):
        left = self.eat("IDENTIFIER").value
        self.eat("OPERATOR", "=")

        expr = []
        while self.current() and self.current().type != "SEMICOLON":
            expr.append(self.current().value)
            self.pos += 1

        self.eat("SEMICOLON")

        return ('assign', left, expr)


# ===============================
# SAMPLE RUN
# ===============================
if __name__ == "__main__":
    code = "int a; int b; int c; a = b + c * 5;"

    print("INPUT CODE:\n", code)

    # Run lexer first
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("\nTOKENS:")
    print(tokens)

    # Run parser
    parser = Parser(tokens)
    syntax_output = parser.parse()

    print("\nSYNTAX OUTPUT:")
    for stmt in syntax_output:
        print(stmt)