from syntax import Assign, BinOp, Print


class ICG:
    def __init__(self):
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate_expr(self, expr, code):
        if isinstance(expr, BinOp):
            left = self.generate_expr(expr.left, code)
            right = self.generate_expr(expr.right, code)
            temp = self.new_temp()
            code.append(f"{temp} = {left} {expr.op} {right}")
            return temp

        return expr

    def generate(self, ast):
        code = []

        for node in ast:
            if isinstance(node, Assign):
                value = self.generate_expr(node.expr, code)
                code.append(f"{node.var} = {value}")

            elif isinstance(node, Print):
                code.append(f"PRINT {node.var}")

        return code