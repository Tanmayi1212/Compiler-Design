# =========================================
# SEMANTIC ANALYSIS PHASE
# Output: Annotated Syntax Tree
# =========================================

symbol_table = {}


def print_annotated_tree(left, right):
    print("\nOutput 2: Annotated Syntax Tree\n")

    # Example only for expression: a = b + c * d

    print("        Assignment")
    print("        /       \\")
    print(f"   {left}:{symbol_table[left]}       +")
    print("              /   \\")
    print(f"       {right[0]}:{symbol_table[right[0]]}    *")
    print("                  / \\")
    print(f"         {right[2]}:{symbol_table[right[2]]} {right[4]}:{symbol_table[right[4]]}")


def semantic_analysis(syntax_output):
    print("----- Semantic Analysis Phase -----\n")

    validated_expression = None

    for item in syntax_output:

        # Declaration
        if item[0] == "declare":
            _, dtype, var = item

            if var in symbol_table:
                print(f"Semantic Error: Variable '{var}' already declared")
                return None

            symbol_table[var] = dtype

        # Assignment
        elif item[0] == "assign":
            _, left, right = item

            if left not in symbol_table:
                print(f"Semantic Error: Variable '{left}' not declared")
                return None

            for token in right:
                if token.isalpha():
                    if token not in symbol_table:
                        print(f"Semantic Error: Variable '{token}' not declared")
                        return None

            validated_expression = (left, right)

    print("Semantic Analysis Successful!\n")

    print("Output 1: Symbol Table")
    for var, dtype in symbol_table.items():
        print(var, ":", dtype)

    if validated_expression:
        left, right = validated_expression
        print_annotated_tree(left, right)

    print("\nOutput 3: Validated Expression passed to ICG")
    print(validated_expression)

    return validated_expression


# Example input from Syntax Analysis
syntax_output = [
    ('declare', 'int', 'a'),
    ('declare', 'int', 'b'),
    ('declare', 'int', 'c'),
    ('declare', 'int', 'd'),
    ('assign', 'a', ['b', '+', 'c', '*', 'd'])
]

semantic_analysis(syntax_output)