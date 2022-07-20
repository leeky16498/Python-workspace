from brisque import BRISQUE 
import csv

i = 0
field_name = ["index", "brisque_score"]

with open("brisque_scores", "w") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
    csv_writer.writeheader()

for i in range(1801):
    obj = BRISQUE("/Users/kyungyunlee/Desktop/PYTHON_FOLDER/THESIS_EXAMPLES/MY_MODEL/Frame_image/0piece_middle" + str(i) + ".jpg")
    
    with open('brisque_scores.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=field_name)
        
        info = {
            'index' : i,
            'brisque_score' : obj.score()
        }
        
        csv_writer.writerow(info)
    print(obj.score())
