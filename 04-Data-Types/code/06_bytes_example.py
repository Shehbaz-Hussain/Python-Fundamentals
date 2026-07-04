# Bytes and bytearray example

binary_data = b"hello"
mutable_binary = bytearray(b"hello")

print(binary_data)
print(mutable_binary)
mutable_binary[0] = 72
print(mutable_binary)

# Expected output:
# b'hello'
# bytearray(b'hello')
# bytearray(b'Hello')

# Explanation:
# Bytes are immutable, while bytearray is mutable.

# Time complexity: O(1)
# Memory notes: Byte arrays store raw binary values.
