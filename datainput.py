import pandas as pd

class DataInput:
    def inputFunction(self, filepath):

        #read csv file into data
        try:
            data = pd.read_csv(filepath)
        except:
            print("Error! The file doesn't exist or it's empty")

        #lowercase
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
            
        return data