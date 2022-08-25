from cgi import print_arguments
import csv

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)

# #print(exampleData)
# print(exampleData[0][1])

# Reading Data from reader objects in a for loop

# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + '' +str(row))
# print(exampleReader)

# #Writer objects
outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputResults = outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham', 'Hello, world!'])

print(outputWriter)
# outputReader = csv.reader(outputResults)
# output = list(outputReader)
# print(output)
# outputFile.close()

#  The delimiter and lineterminator Keyword Arguments
csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvOutput1 = csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvOutput2 = csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvOutput3 = csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
print(csvOutput1)
print(csvOutput2)
print(csvOutput3)
csvFile.close()

