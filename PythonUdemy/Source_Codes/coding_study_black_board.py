num1 = input("첫 숫자")
num2 = input("둘째 숫자")
num_range = list(range(int(num1), int(num2)))
print(num_range)
odd_in_num_range = []

for number in num_range:
    if number%2 == 1:
        odd_in_num_range.append(number)

print(odd_in_num_range)
print(sum(odd_in_num_range))