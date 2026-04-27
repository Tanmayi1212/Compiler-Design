symbol_table = {}

def semantic_analysis(ast):
    print("----- Semantic Analysis Phase -----\n")

    validated_expression = None

    for item in ast:
        if item[0] == "declare":
            _, dtype, var = item

            if var in symbol_table:
                raise Exception(f"Variable '{var}' already declared")

            symbol_table[var] = dtype

        elif item[0] == "assign":
            _, left, right = item

            if left not in symbol_table:
                raise Exception(f"Variable '{left}' not declared")

            for token in right:
                if token.isalpha() and token not in symbol_table:
                    raise Exception(f"Variable '{token}' not declared")

            validated_expression = (left, right)

    print("Semantic Analysis Successful!\n")

    print("Symbol Table:")
    for k, v in symbol_table.items():
        print(f"{k} : {v}")

    print("\nValidated Expression:")
    print(validated_expression)

    return validated_expression