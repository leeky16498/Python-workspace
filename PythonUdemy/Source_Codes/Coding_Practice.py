## 소수 체크 프로그램 ##

# n = int(input("Please give me the number, I will check whether the number is prime or not."))
# print("number we got is " + str(n))
#
# def prime_checker(number):
#     a = 0
#
#     for i in range(1, number):
#         if number % i == 0:
#             a += 1
#
#     print(a)
#
#     if a >= 2:
#         print("The number is not prime number")
#     else:
#         print("The number is prime number.")
#
# prime_checker(n)

### 비밀 경매 프로그램 코딩 ###

from replit import clear
from time import *
import math

user_info = {}

for i in range(3):
    user_name = input("What is your name?")
    user_price = int(input("What is your price?")) 
    user_info[user_name] = user_price
    clear()

print(user_info)

prices = list(user_info.values())
users = list(user_info.keys())

winner_price = max(prices)
print(winner_price)
## 배열에서 최대값 조회

winner_price_index = prices.index(winner_price)
print(winner_price_index)
## index 메서드를 통해 최대값 인덱스를 조회

winner_user_name = users[winner_price_index]
print("Winner of bid is " + winner_user_name)

## 경매 프로그램 코딩 완료

