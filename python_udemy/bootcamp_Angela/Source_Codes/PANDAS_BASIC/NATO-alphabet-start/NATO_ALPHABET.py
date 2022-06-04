import pandas as pd

keys = pd.read_csv("/Users/kyungyunlee/Desktop/PYTHON/python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/NATO-alphabet-start/nato_phonetic_alphabet.csv")
print(keys)

new_dict = dict()

for (index, row) in keys.iterrows():
    new_dict[row.letter] = row.code

print(new_dict)

text = input("What is your name? ")
text = list(text.upper())

print(text)

new_letter = []

for letter in text:
    new_letter.append(new_dict[letter])

print(new_letter)