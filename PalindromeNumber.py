def reverse_number(n):
    """Reverse the digits of a whole number n (0 or more). Returns (reversed, steps)."""
    reversed_number = 0
    steps = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        reversed_number = reversed_number * 10 + digit
        steps = steps + 1
    return reversed_number, steps

def is_palindrome(n):
    """True if n reads the same backwards. A negative number never does."""
    if n < 0:
        return False
    return reverse_number(n)[0] == n

def report(number):
    if number < 0:
        print(number, "is not a palindrome: the minus cannot be read backwards.")
        return
    rev, steps = reverse_number(number)
    word = "is" if is_palindrome(number) else "is not"
    print(number, "reversed is", rev, "after", steps, "digit step(s):", number, word, "a palindrome")

for number in [121, 12321, 120, 7, 0, -121]:
    report(number)

print()
try:
    text = input("Type a whole number to check (or just press Enter to finish): ").strip()
except EOFError:
    text = ""
if text == "":
    print("No number typed: demo only.")
else:
    try:
        report(int(text))
    except ValueError:
        print(repr(text), "is not a whole number. Type digits only, for example 1331.")
