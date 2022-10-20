import tabula
import pandas as pd
import csv
df = tabula.read_pdf("delay.pdf", pages="all")
tabula.convert_into("delay.pdf", "delay.csv", output_format="csv", pages="all")


new_csv = []
with open('delay.csv','r') as csvfile:
    #reader can iterate over lines of csv file
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for i in row:
            if row[0] == 'DEN' or row[0] =='':
                print(row)
                # new_csv.append(row)
            else:
                print('fail')


csvfile.close()
    # reading first row of field names
    # fields = csvreader.__next__()
    # print('Field Names\n-----------')
    # for field in fields:
    #     print("%8s"%field, end='')
    # print('\nRows\n------------------')
    # # reading rows
    # for row in csvreader:
    #     # access and print each field value of row
    #     for col in row:
    #         print("%8s"%col, end='')
    #     print('\n')



# pd.options.display.max_rows = 9999
# read_the_csv.fillna('', inplace=True)

# read_the_csv = pd.read_csv("delay.csv") 
# usecols=['Orig', 'Dest', 'Flt', 'Aircraft', 'Final', 'Final LS', 'Doors', 'Total PAX', 'Sched', 'Doors.1', 'Out', 'Doors.2', 'Out.1', 'Delay', 'Delay Code & Remarks'])

# new_list = []
# for i in read_the_csv:
#     new_list.append(i)
# print(read_the_csv.to_string())
    
# for index, row in read_the_csv.iterrows():
    # print(index, row)
          
          
        #   , row['Dest'], row['Flt'], row['Aircraft'], row['Final'], row['Final LS'], row['Doors'], row['Total PAX'], row['Sched'], row['Doors.1'], row['Out'], row['Doors.2'], row['Out.1'], row['Delay'], row['Delay Code & Remarks'])
    
    
    
    
    
    
    
# print(read_the_csv)
# data_top = read_the_csv.head()
# print(data_top)
# for col in read_the_csv.columns:
#     print(col)

# Check if DEN is in the first part of the row
# print(read_the_csv.to_string())




# for row in read_the_csv:
#     if row[:3] == 'DEN' or row[:3] == '':
#         print(row)
        # print(row)

# print(read_the_csv.keys())
# print(read_the_csv.to_string())

# new_report = []
# with open('delay.csv') as csvfile:
#     writefile = csv.reader(csvfile)
#     for row in writefile:
#         print(row)

# print(read_the_csv)

# for index, row in read_the_csv.iterrows():
#     print(index, row)
    
# with open('delay.csv', newline='') as csvfile:
#     writefile = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in writefile:
#         print(row)
            
# csvfile.close()
    
    
    