import csv
fh=open("compresult.csv","w")
cwriter=csv.writer(fh)
compdata=[['Name', 'Points', 'Rank'],
        ['Shradha', 4500,23],
        ['Nishchay',4800,31],
        ['Ali',4500,31],
        ['Adi',5100,14]]
cwriter.writerows(compdata)
fh.close()