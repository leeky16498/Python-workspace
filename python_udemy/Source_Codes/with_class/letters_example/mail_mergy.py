
with open("python_udemy/Source_Codes/with_class/letters_example/invited_names.txt", mode="r") as file:
    contents = file.read()
    list = contents.split()
    print(list)

name_list = list

for name in name_list:
    with open(f"/Users/kyungyunlee/Desktop/PYTHON/python_udemy/Source_Codes/with_class/letters_example/letters/{name}.txt", mode="w") as file:
        file.write(f"Hey! {name}! This is the mail for you! please check it right away!")