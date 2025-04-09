def is_perfect(number):
    if number < 1:
        return False
    total = sum(i for i in range(1, number) if number % i == 0)
    return total == number

print(is_perfect(28)) 
