import csv

list_of_lines = []
new_list = []
last_list = []
with open('RAMPSchedule.pdf.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        list_of_lines.append(row)
    for item in list_of_lines[169:]:
        new_list.append(item)
    # for new_item in list_of_lines[:289]:
    #     last_list.append(new_item)
    print(new_list)
    # print(last_list)
        