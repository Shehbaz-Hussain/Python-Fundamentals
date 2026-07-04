# Mutable vs immutable example

numbers = [1, 2, 3]
numbers.append(4)

text = "hello"
# text[0] = "H"  # This would raise an error

print(numbers)
print(text)

# Expected output:
# [1, 2, 3, 4]
# hello

# Explanation:
# Lists are mutable, while strings are immutable.

# Time complexity: O(1) for append.
# Memory notes: Changing a list modifies the same object in place.
