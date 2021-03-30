# Task 1 — FizzBuzz task with numbers from 1 up to 100

result = []

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        result.append("FizzBuzz")
    elif num % 3 == 0:
        result.append("Fizz")
    elif num % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(num))

print(", ".join(result))
