import csv
from Converter.ConvertHelper import ConvertHelper

#with open('detection_results.csv', 'r') as csvfile:
with open(ConvertHelper.DetectionResultFilePath, 'r') as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')
  next(readCSV)

  with open('outputCSV/exported.csv', 'a+', newline='') as output:
    csv_writer = csv.writer(output, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for line in readCSV:
      print(line)
      name = '"' + line[0].replace(' ', '%20') + '"'
      labelWithoutScore = '"' + line[6].split(' ')[0] + '"'
      csv_writer.writerow([name, line[2], line[3], line[4], line[5], labelWithoutScore])