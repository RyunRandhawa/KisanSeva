import csv
with open("compresult.csv", "r", newline='\r\n') as fh:
    creader = csv.reader(fh)
    for rec in creader:
        print(rec)