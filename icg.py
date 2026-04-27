from syntax import Assign, BinOp, Print


class ICG:
    def generate(self, ast):
        code = []

        for node in ast:
            if isinstance(node, Assign):
                if isinstance(node.expr, BinOp):
                    code.append(f"{node.var} = {node.expr.left} + {node.expr.right}")
                else:
                    code.append(f"{node.var} = {node.expr}")

            elif isinstance(node, Print):
                code.append(f"PRINT {node.var}")

        return code