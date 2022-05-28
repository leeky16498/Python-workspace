## 소수 체크 프로그램 ##

n = int(input("Please give me the number, I will check whether the number is prime or not."))
print("number we got is " + str(n))

def prime_checker(number):
    a = 0

    for i in range(1, number):
        if number % i == 0:
            a += 1

    print(a)
    if a >= 2:
        print("The number is not prime number")
    else:
        print("The number is prime number.")

prime_checker(n)