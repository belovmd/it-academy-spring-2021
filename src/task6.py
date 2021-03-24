input_number = int(input("Input number: "))
straight_number = input_number
reverse_number = 0

while straight_number > 0:
    next_digit = straight_number % 10
    straight_number = straight_number // 10
    reverse_number = reverse_number * 10
    reverse_number = reverse_number + next_digit

if input_number == reverse_number:
    print("Number is palindrome!")
else:
    print("Number is NOT palindrome!")
