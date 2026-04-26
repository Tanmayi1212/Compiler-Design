# =========================================
# INTERMEDIATE CODE GENERATION (ICG) PHASE
# Input  : Output from Semantic Analysis Phase
#          (Validated Expression)
# Output : Three Address Code (TAC)
# =========================================

temp_count = 1


def generate_temp():
    global temp_count
    temp = "t" + str(temp_count)
    temp_count += 1
    return temp


def intermediate_code_generation(semantic_output):
    print("----- Intermediate Code Generation Phase -----\n")

    # Input from Semantic Analysis
    # Example:
    # ('a', ['b', '+', 'c', '*', 'd'])

    left, tokens = semantic_output

    print("Input from Semantic Analysis:")
    print(semantic_output)

    print("\nOutput: Three Address Code (TAC)\n")

    while len(tokens) > 1:
        done = False

        # First handle * and /
        for i in range(len(tokens)):
            if tokens[i] in ["*", "/"]:
                temp = generate_temp()

                print(f"{temp} = {tokens[i-1]} {tokens[i]} {tokens[i+1]}")

                tokens = tokens[:i-1] + [temp] + tokens[i+2:]
                done = True
                break

        if done:
            continue

        # Then handle + and -
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-"]:
                temp = generate_temp()

                print(f"{temp} = {tokens[i-1]} {tokens[i]} {tokens[i+1]}")

                tokens = tokens[:i-1] + [temp] + tokens[i+2:]
                break

        if len(tokens) == 1:
            break

    print(f"{left} = {tokens[0]}")


# =========================================
# Example Input from Semantic Analysis Phase
# =========================================

semantic_output = ('a', ['b', '+', 'c', '*', 'd'])

intermediate_code_generation(semantic_output)