num = int(input("limit of numbers?"))

for num in range(num):
    if "3" in list(str(num)):
        print("==")
    elif "6" in list(str(num)):
        print("==")
    elif "9" in list(str(num)):
        print("==")
    else:
        print(num)