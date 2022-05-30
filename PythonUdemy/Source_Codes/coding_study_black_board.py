
id_list = ["muzi", "frodo", "apeach", "neo"]
reports = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

new_dict = {}

for id in id_list:
    for report in reports:
        new_dict[id] = report.split()

print(new_dict)