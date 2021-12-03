import os

with open(os.path.expanduser("data/day3"), "r") as f:
    lines = f.readlines()


n = len(lines)
n_columns = len(lines[0]) - 1  # no newline character
gamma = []
for col in range(n_columns):
    to_append = int(sum([int(line[col] == "0") for line in lines]) > (n / 2))
    gamma.append(to_append)

assert len(gamma) == n_columns

epsilon = [str(1 - value) for value in gamma]
epsilon = "".join(epsilon)
gamma = [str(value) for value in gamma]
gamma = "".join(gamma)
int(gamma, 2) * int(epsilon, 2)
