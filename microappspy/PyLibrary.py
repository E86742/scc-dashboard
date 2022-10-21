import PyPDF2
import csv
import pandas as pd

pdfData = []
with open('RAMP.pdf', 'rb') as f:
    with open('RAMPCSV.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        pdfReader = PyPDF2.PdfFileReader(f)
        for page in pdfReader.pages:
            x = page.extractText()
            csv_writer.writerow([x])
df = pd.read_csv('RAMPCSV.csv', index_col=0)

print(df.to_string())
f.close()
csvfile.close()
