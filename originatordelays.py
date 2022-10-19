import tabula
import pandas as pd
import csv
df = tabula.read_pdf("delay.pdf", pages="all", lattice=True)
tabula.convert_into("delay.pdf", "delay.csv", output_format="csv", pages="all")

read_the_csv = pd.read_csv("delay.csv")
read_the_csv.fillna('', inplace=True)
print(read_the_csv.to_string())

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
    
    
    