def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:   # Check if the number is even
            total += num
    return total

numbers = [12, 7, -6, 15, 0, 18, -3, 10, 22, -5, 14]
result = sum_even_numbers(numbers)
print("Sum of even numbers:", result)
