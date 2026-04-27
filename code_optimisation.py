class Optimizer:
    def optimize(self, icg):
        optimized = []

        for line in icg:
            parts = line.split()

            if len(parts) == 5 and parts[2].isdigit() and parts[4].isdigit():
                val = int(parts[2]) + int(parts[4])
                optimized.append(f"{parts[0]} = {val}")
            else:
                optimized.append(line)

        return optimized
