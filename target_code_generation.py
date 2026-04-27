class CodeGenerator:
    def generate(self, icg):
        target = []

        for line in icg:
            parts = line.split()

            if parts[0] == "PRINT":
                target.append(f"OUT {parts[1]}")

            elif len(parts) == 3:
                target.append(f"SET {parts[0]} {parts[2]}")

            elif len(parts) == 5:
                target.append(f"LOAD {parts[2]}")
                target.append(f"ADD {parts[4]}")
                target.append(f"SAVE {parts[0]}")

        return target