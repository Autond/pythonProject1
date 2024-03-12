import csv

test_data = [
    ['Name' ,'Age','city']
    ['Alice',30,'ny']
]

with open('mydata.csv','w') as file:
    writer = csv.writer(file)
    for data in test_data:
        writer.writerow(data)