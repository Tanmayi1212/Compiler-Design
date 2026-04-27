from syntax import Assign, Print


class SemanticAnalyzer:
    def __init__(self):
        self.symbols = {}

    def analyze(self, ast):
        for node in ast:
            if isinstance(node, Assign):
                self.symbols[node.var] = "int"

            elif isinstance(node, Print):
                if node.var not in self.symbols:
                    raise Exception(f"Semantic Error: {node.var} not defined")

        return self.symbols