temp_count = 1

def generate_temp():
    global temp_count
    t = f"t{temp_count}"
    temp_count += 1
    return t


def intermediate_code_generation(semantic_output):
    print("\n----- ICG Phase -----\n")

    left, tokens = semantic_output
    tac = []

    while len(tokens) > 1:
        for i in range(len(tokens)):
            if tokens[i] in ["*", "/"]:
                t = generate_temp()
                tac.append(f"{t} = {tokens[i-1]} {tokens[i]} {tokens[i+1]}")
                tokens = tokens[:i-1] + [t] + tokens[i+2:]
                break
        else:
            for i in range(len(tokens)):
                if tokens[i] in ["+", "-"]:
                    t = generate_temp()
                    tac.append(f"{t} = {tokens[i-1]} {tokens[i]} {tokens[i+1]}")
                    tokens = tokens[:i-1] + [t] + tokens[i+2:]
                    break

    tac.append(f"{left} = {tokens[0]}")

    print("TAC:")
    for line in tac:
        print(line)

    return tac