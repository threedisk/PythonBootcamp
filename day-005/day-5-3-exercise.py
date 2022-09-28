sum_of_even=0
sum_of_odd=0
for number in range(1,101):
    if number % 2 == 0:
        sum_of_even += number
    else:
        sum_of_odd += number

print(f"Sum of Even number :{sum_of_even}.")
print(f"Sum of Odd number :{sum_of_odd}.")