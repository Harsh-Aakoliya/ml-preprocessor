from datainput import DataInput
from standardization import Standardization
from normalization import Normalization
from impute import Impute
from categorical import Categorical
import pandas as pd

class Preprocessor:

    data = 0

    def __init__(self, filepath):
        self.data = DataInput().inputFunction(filepath)
        self.impute = Impute(self.data)
        self.standardization = Standardization(self.data)
        self.normalization = Normalization(self.data)
        self.categorical = Categorical(self.data)

    def printData(self):
        print(self.data)

    def save(self, saveData):
        toBeDownloaded = {}
        for column in saveData.columns.values:
            toBeDownloaded[column] = saveData[column]

        newFileName = "processed.csv"
<<<<<<< HEAD
        pd.DataFrame(saveData).to_csv(newFileName, index=False)



ps = Preprocessor("file.csv")
data = ps.impute.fillwithmode("marks")
ps.save(data)
        
=======
        pd.DataFrame(saveData).to_csv(newFileName, index=False)
>>>>>>> f455259 (added extra features)
