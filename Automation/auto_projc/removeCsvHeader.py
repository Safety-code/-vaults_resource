import csv
from genericpath import exists
import os

# removeCsvHeader.py - Removes the header from all CSV files in the current working directory

os.mkdir('headerRemoved', exist_ok=True)

# Loop through the current working directory skipping non-csv files

for csvFilename in os.listdir('.csv'):
    continue  # skip non-csv files
print('Removing header from ' + csvFilename + '...')

# Read the CSV file in (skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue  #skip first row
    csvRows.append(row)
csvFileObj.close()

# WRITE OUT THE CSV FILE
csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
csvWriter = csv.writer(csvFileObj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()