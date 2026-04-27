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
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left} + {self.right}"


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
                self.eat("ARROW")

                left = self.eat("IDENTIFIER") if self.current().type == "IDENTIFIER" else self.eat("NUMBER")

                if self.current() and self.current().type == "PLUS":
                    self.eat("PLUS")
                    right = self.eat("IDENTIFIER") if self.current().type == "IDENTIFIER" else self.eat("NUMBER")
                    ast.append(Assign(var, BinOp(left.value, right.value)))
                else:
                    ast.append(Assign(var, left.value))

            elif tok.type == "SHOW":
                self.eat("SHOW")
                var = self.eat("IDENTIFIER").value
                ast.append(Print(var))

            else:
                self.pos += 1

        return ast