# =========================================
# TARGET CODE GENERATION PHASE
# Input  : Optimized TAC (list of strings)
# Output : Assembly-like Code
# =========================================

class TargetCodeGenerator:
    def __init__(self):
        self.reg_count = 1
        self.var_to_reg = {}

    def get_register(self):
        reg = f"R{self.reg_count}"
        self.reg_count += 1
        return reg

    def generate(self, tac_lines):
        print("\n----- Target Code Generation Phase -----\n")

        target_code = []

        for line in tac_lines:
            parts = line.split()

            # Case 1: a = b
            if len(parts) == 3:
                lhs = parts[0]
                rhs = parts[2]

                # If rhs already stored in register
                if rhs in self.var_to_reg:
                    target_code.append(f"MOV {lhs}, {self.var_to_reg[rhs]}")
                else:
                    target_code.append(f"MOV {lhs}, {rhs}")

            # Case 2: t1 = a + b
            else:
                lhs = parts[0]
                op1 = parts[2]
                operator = parts[3]
                op2 = parts[4]

                reg = self.get_register()

                # Use register if already computed
                op1_val = self.var_to_reg.get(op1, op1)
                op2_val = self.var_to_reg.get(op2, op2)

                if operator == "+":
                    instr = "ADD"
                elif operator == "-":
                    instr = "SUB"
                elif operator == "*":
                    instr = "MUL"
                elif operator == "/":
                    instr = "DIV"

                target_code.append(f"{instr} {reg}, {op1_val}, {op2_val}")

                # Store result in register map
                self.var_to_reg[lhs] = reg

        print("Target Code:\n")
        for line in target_code:
            print(line)

        return target_code
    
# if __name__ == "__main__":

#     optimized_tac = [
#         "t1 = 5",
#         "t2 = 5 + 4",
#         "t3 = t1",
#         "t4 = t2",
#         "t5 = a + b",
#         "t6 = t5",
#         "a = t2",
#         "b = 10"
#     ]

#     print("Optimized TAC:\n")
#     for line in optimized_tac:
#         print(line)

#     tcg = TargetCodeGenerator()
#     tcg.generate(optimized_tac)