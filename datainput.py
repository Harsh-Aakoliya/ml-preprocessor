from os import path
import sys
import pandas as pd

class DataInput:

    def inputFunction(self):
        #check the extension of the file
        try:
            file = sys.argv[1]
            fileExtension = path.splitext(sys.argv[1])
            if fileExtension != '.csv':
                raise SystemExit("File extension invalid")
        except:
            print("Error occured while searching for file")

        #read csv file into data
        try:
            data = pd.read_csv(file)
        except:
            print("Error! The file doesn't exist or it's empty")

        #lowercase
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)