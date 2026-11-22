def lcm_brute(first, second):
    """Brute force: check multiples until the first common multiple is found."""
    steps = 0

    if first == 0 or second == 0:
        return 0, steps
    candidate = max(first, second)
    while True:
        steps = steps + 1
        if candidate % first == 0 and candidate % second == 0:
            return candidate, steps
        candidate = candidate + 1

def compare(first, second):
    l, steps = lcm_brute(first, second)
    print(f"lcm({first}, {second}) = {l}  brute-force steps: {steps}")

for first, second in [(16, 24), (24, 16), (12, 8), (1071, 462), (0, 5), (832040, 514229)]:
    compare(first, second)

print()
try:
    text = input("Type two whole numbers with a space between (or just press Enter to finish): ")
except EOFError:
    text = ""
parts = text.split()

if not parts:
    print("No numbers typed: Demo only.")
else:
    try:
        first, second = int(parts[0]), int(parts[1])
        if len(parts) != 2 or first < 0 or second < 0:
            print("Please type exactly two whole numbers, 0 or more.")
        else:
            compare(first, second)
    except (ValueError, IndexError):
        print("Please type exactly two whole numbers, 0 or more.")