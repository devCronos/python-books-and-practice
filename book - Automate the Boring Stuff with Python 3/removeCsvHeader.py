__author__ = 'Cronos'
import csv
import os

os.chdir('C:\\Users\\Cronos\\Downloads\\Compressed\\automate_online-materials')
os.makedirs('headerRemoved', exist_ok=True)
for csvFname in os.listdir('.'):
    if not csvFname.endswith('.csv'):
        continue
    print('Removing header from ' + csvFname + '...')
    csvRows = []
    csvFobj = open(csvFname)
    readerO = csv.reader(csvFobj)
    for row in readerO:
        if readerO.line_num == 1:
            continue
        csvRows.append(row)
    csvFobj.close()
    csvFobj = open(os.path.join('headerRemoved', csvFname), 'w', newline='')
    csvWriter = csv.writer(csvFobj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFobj.close()