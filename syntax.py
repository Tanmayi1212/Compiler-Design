class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type, expected_value=None):
        token = self.current()

        if token is None:
            raise Exception("Syntax Error: Unexpected end of input")

        if token.type != expected_type:
            raise Exception(f"Syntax Error: Expected {expected_type}, got {token.type}")

        if expected_value and token.value != expected_value:
            raise Exception(f"Syntax Error: Expected '{expected_value}', got '{token.value}'")

        self.pos += 1
        return token

    # =========================
    # MAIN PARSE FUNCTION
    # =========================
    def parse(self):
        result = []

        while self.current():
            token = self.current()

            if token.type == "KEYWORD":
                result.append(self.parse_declaration())

            elif token.type == "IDENTIFIER":
                result.append(self.parse_assignment())

            else:
                raise Exception(f"Syntax Error: Invalid start {token}")

        return result

    # =========================
    # DECLARATION: int a;
    # =========================
    def parse_declaration(self):
        self.eat("KEYWORD", "int")
        var = self.eat("IDENTIFIER").value
        self.eat("SEMICOLON")

        return ('declare', 'int', var)

    # =========================
    # ASSIGNMENT: a = b + 3;
    # =========================
    def parse_assignment(self):
        left = self.eat("IDENTIFIER").value
        self.eat("OPERATOR", "=")

        expr = []

        while self.current() and self.current().type != "SEMICOLON":
            expr.append(self.current().value)
            self.pos += 1

        self.eat("SEMICOLON")

        return ('assign', left, expr)