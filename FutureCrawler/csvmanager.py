import csv

class CsvManager(object):

    def __init__(self, file_path):
        self.file = file_path
        self.keys = []

    def getKeys(self, sampleObj):
        for key in sampleObj:
            self.keys.append(key)
            

    def updateCSV(self, data):
        with open(self.file, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|')

            # re-add header as the first row
            csvwriter.writerow(self.keys)

            for obj in range(len(data)):
                row = []
                for key in range(len(self.keys)):
                    row.append(data[obj][self.keys[key]])
                csvwriter.writerow(row)
        csvfile.close()