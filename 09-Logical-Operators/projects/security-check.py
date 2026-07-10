# Project: Security Access Checker
# --------------------------------
# Objective:
# Determine whether a person is allowed to enter a secure area.
#
# Concepts Used:
# - Variables
# - Input and Output
# - Comparison Operators
# - Logical Operators (or, not)
#
# Note:
# This project uses only concepts covered up to Module 09.

print("===== Security Access Checker =====")

has_id_card = input("Do you have an ID card? (yes/no): ")
has_access_card = input("Do you have an access card? (yes/no): ")

print()

access_granted = (
    has_id_card == "yes" or
    has_access_card == "yes"
)

print("Has ID Card:", has_id_card)
print("Has Access Card:", has_access_card)

print()

print("ID Card Available:", has_id_card == "yes")
print("Access Card Available:", has_access_card == "yes")

print()

print("Access Granted:", access_granted)
print("Access Denied:", not access_granted)


# Sample Output 1:

# ===== Security Access Checker =====
# Do you have an ID card? (yes/no): yes
# Do you have an access card? (yes/no): no

# Has ID Card: yes
# Has Access Card: no

# ID Card Available: True
# Access Card Available: False

# Access Granted: True
# Access Denied: False

# Sample Output 2:

# ===== Security Access Checker =====
# Do you have an ID card? (yes/no): no
# Do you have an access card? (yes/no): no

# Has ID card: no
# Has Access Card: no

# ID card Available: False
# Access Card Available: False

# Access Granted: False
# Access Denied: True
