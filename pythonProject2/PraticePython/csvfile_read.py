import csv

# Writing the csv file data
# with open("name.csv",'w', newline="") as f:
#     thewriter = csv.writer(f)
#
#     thewriter.writerow(['col1', 'col2' , 'col3'])
#     for i in range(1,10):
#         thewriter.writerow(['Vaishu', "Vijay", "Vyshureddy"])


# Read csv file data

with open('demo.csv') as f:
    read = csv.DictReader(f)

    for i in read:
        print(i)

f.close()