
# ******************************
# Make your Code
# ******************************

numbers = []
for i in range(5):
    num = int(input("Enter num: "))
    numbers.insert(i, num)

numbers.sort()
print(numbers[1] + numbers[2] + numbers[3])