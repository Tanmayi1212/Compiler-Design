class Optimizer:
    def optimize(self, icg):
        optimized = []

        for line in icg:
            parts = line.split()

            if len(parts) == 5 and parts[2].isdigit() and parts[4].isdigit():
                left = int(parts[2])
                right = int(parts[4])
                op = parts[3]

                if op == "+":
                    val = left + right
                elif op == "-":
                    val = left - right
                elif op == "*":
                    val = left * right
                elif op == "/":
                    if right == 0:
                        optimized.append(line)
                        continue
                    val = left // right
                else:
                    optimized.append(line)
                    continue

                optimized.append(f"{parts[0]} = {val}")
            else:
                optimized.append(line)

        return optimized
