class ASTNode:
    pass


class Assign(ASTNode):
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f"Assign({self.var} = {self.expr})"


class Print(ASTNode):
    def __init__(self, var):
        self.var = var

    def __repr__(self):
        return f"Print({self.var})"


class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"{self.left} {self.op} {self.right}"


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        tok = self.current()
        if tok and tok.type == token_type:
            self.pos += 1
            return tok
        raise SyntaxError(f"Expected {token_type}")

    def parse(self):
        ast = []
        while self.current():
            tok = self.current()

            if tok.type == "LET":
                self.eat("LET")
                var = self.eat("IDENTIFIER").value
                self.eat("ASSIGN")
                expr = self.parse_expr()
                ast.append(Assign(var, expr))

            elif tok.type == "SHOW":
                self.eat("SHOW")
                var = self.eat("IDENTIFIER").value
                ast.append(Print(var))

            else:
                self.pos += 1

        return ast

    def parse_expr(self):
        node = self.parse_term()

        while self.current() and self.current().type == "OPERATOR" and self.current().value in {"+", "-"}:
            op = self.current().value
            self.eat("OPERATOR")
            right = self.parse_term()
            node = BinOp(node, op, right)

        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.current() and self.current().type == "OPERATOR" and self.current().value in {"*", "/"}:
            op = self.current().value
            self.eat("OPERATOR")
            right = self.parse_factor()
            node = BinOp(node, op, right)

        return node

    def parse_factor(self):
        tok = self.current()
        if not tok:
            raise SyntaxError("Unexpected end of input")

        if tok.type == "IDENTIFIER":
            return self.eat("IDENTIFIER").value
        if tok.type == "NUMBER":
            return self.eat("NUMBER").value

        raise SyntaxError(f"Unexpected token {tok.type}")