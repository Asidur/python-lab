num = int(input("Enter a number: "))
order = len(str(num))
sum_arm = sum(int(digit) ** order for digit in str(num))

if num == sum_arm:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")