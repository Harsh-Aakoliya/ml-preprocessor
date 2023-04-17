import sys
import pandas as pd

class DataInput:
    def inputFunction(self, filepath):
        #check the extension of the file
        # try:
        #     fileExtension = filepath.split(".")
        #     if fileExtension != '.csv':
        #         raise Exception("File extension invalid")
        # except:
        #     raise Exception("Error occured while searching for file")

        #read csv file into data
        try:
            data = pd.read_csv(filepath)
        except:
            print("Error! The file doesn't exist or it's empty")

        #lowercase
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
            
        return data