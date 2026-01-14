import csv

# with open("3/3.4/0/example.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

students = [
    ["Greg", "Dean", 70, 80, 90],
    ["Wirt", "Wood", 80, 80.2, 80]
]

with open("3/3.4/0/example.csv", "a") as f:
    writer = csv.writer(f)
    for student in students:
        print(student)
        writer.writerow(student)

# with open("3/3.4/0/example.csv", "a") as f:
#     writer = csv.writer(f)
#     writer.writerows(students)