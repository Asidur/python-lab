s = input("Enter a string: ")
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
