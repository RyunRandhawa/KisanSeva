import csv
with open("compresult.csv","r") as fh:
    creader = csv.reader(fh)
    for rec in creader:
        print(rec)