import pandas as pd

data = pd.read_csv("python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/NYC_data.csv")
print(data)

fur_data = data["Primary Fur Color"]
count = fur_data.count()
print(fur_data)
print(count)

fur_data_sorts = data["Primary Fur Color"].to_list()
fur_data_sorts = set(fur_data_sorts)
fur_data_sorts = list(fur_data_sorts)
print(fur_data_sorts)

fur_data_count = list(fur_data.value_counts())
# gray_count = len(data[data["Primary fur color"] == "gray"])
print(fur_data_count)

new_dict = {
    "Primary_furs" : fur_data_sorts[:-1],
    "counts" : list(fur_data_count)
}

print(new_dict)

data1 = pd.DataFrame(new_dict)
print(data1)
data1.to_csv("python_udemy/bootcamp_Angela/Source_Codes/PANDAS_boot/NYC_new_data.csv")