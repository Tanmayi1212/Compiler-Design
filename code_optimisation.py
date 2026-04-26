# =========================================
# CODE OPTIMIZATION PHASE
# Input  : TAC (list of strings)
# Output : Optimized TAC
# =========================================

def parse_tac(tac_lines):
    icg = []
    for line in tac_lines:
        parts = line.split()

        if len(parts) == 3:  # a = b
            icg.append(("=", parts[2], "", parts[0]))
        else:  # t1 = a + b
            icg.append((parts[3], parts[2], parts[4], parts[0]))

    return icg


def format_tac(icg):
    output = []
    for op, a1, a2, res in icg:
        if op == "=":
            output.append(f"{res} = {a1}")
        else:
            output.append(f"{res} = {a1} {op} {a2}")
    return output


# ----------------------------
# 1. Constant Folding
# ----------------------------
def constant_folding(icg):
    new_icg = []
    for op, a1, a2, res in icg:
        if a1.isdigit() and a2.isdigit():
            val = eval(f"{a1}{op}{a2}")
            new_icg.append(("=", str(val), "", res))
        else:
            new_icg.append((op, a1, a2, res))
    return new_icg


# ----------------------------
# 2. Constant Propagation
# ----------------------------
def constant_propagation(icg):
    values = {}
    new_icg = []

    for op, a1, a2, res in icg:
        if a1 in values:
            a1 = values[a1]
        if a2 in values:
            a2 = values[a2]

        if op == "=" and a1.isdigit():
            values[res] = a1
        else:
            values.pop(res, None)

        new_icg.append((op, a1, a2, res))

    return new_icg


# ----------------------------
# 3. Common Subexpression Elimination
# ----------------------------
def cse(icg):
    expr_map = {}
    new_icg = []

    for op, a1, a2, res in icg:
        key = (op, a1, a2)

        if op in ["+", "-", "*", "/"]:
            if key in expr_map:
                new_icg.append(("=", expr_map[key], "", res))
            else:
                expr_map[key] = res
                new_icg.append((op, a1, a2, res))
        else:
            new_icg.append((op, a1, a2, res))

    return new_icg


# ----------------------------
# 4. Dead Code Elimination
# ----------------------------
def dead_code_elimination(icg):
    used = set()
    new_icg = []

    for op, a1, a2, res in reversed(icg):
        if res in used or op == "=":
            new_icg.append((op, a1, a2, res))

            if not a1.isdigit():
                used.add(a1)
            if not a2.isdigit():
                used.add(a2)

    return list(reversed(new_icg))


# ----------------------------
# MAIN OPTIMIZER FUNCTION
# ----------------------------
def optimize_tac(tac_lines):
    print("\n----- Code Optimization Phase -----\n")

    icg = parse_tac(tac_lines)

    icg = constant_folding(icg)
    icg = constant_propagation(icg)
    icg = cse(icg)
    icg = dead_code_elimination(icg)

    optimized = format_tac(icg)

    print("Optimized TAC:\n")
    for line in optimized:
        print(line)

    return optimized


# =========================================
# SAMPLE INPUT (TEST CASE)
# =========================================

# if __name__ == "__main__":

#     tac = [
#         "t1 = 2 + 3",      # constant folding
#         "t2 = t1 + 4",     # propagation
#         "t3 = 2 + 3",      # CSE
#         "t4 = t3 + 4",     # propagation
#         "t5 = a + b",      # normal
#         "t6 = a + b",      # CSE
#         "a = t2",          # used
#         "b = 10"           # dead code (will be removed)
#     ]

#     print("Original TAC:\n")
#     for line in tac:
#         print(line)

#     optimize_tac(tac)
