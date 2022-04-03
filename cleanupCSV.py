import csv

alphabetCSV = "steno-alphabet.csv"
newAlphabetCSV = "steno-alphabet.csv.new"
with open(alphabetCSV, newline ='') as csvFile:
    csvReader = csv.DictReader(csvFile)
    with open(newAlphabetCSV, mode='x') as newCSVFile:
        csvWriter = csv.DictWriter(newCSVFile, fieldnames=csvReader.fieldnames)
        for row in csvReader:
            # Get rid of any whitespace in the raw steno
            row["raw steno"] = row["raw steno"].replace(" ", "")
            csvWriter.writerow(row)
