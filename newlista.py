import tabula
df = tabula.read_pdf("rampschedule.pdf", pages='all')[0]
tabula.convert_into("rampschedule.pdf", "rampcsv.csv", output_format="csv", pages="all")
print(df)