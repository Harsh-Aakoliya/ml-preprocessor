from datainput import DataInput
from standardization import Standardization
from normalization import Normalization
from impute import Impute
from categorical import Categorical
from decimalscaling import DecimalScaling
from compression import Compression
import pandas as pd

class Preprocessor:

    data = 0

    def __init__(self, filepath):
        self.data = DataInput().inputFunction(filepath)
        self.impute = Impute(self.data)
        self.standardization = Standardization(self.data)
        self.normalization = Normalization(self.data)
        self.categorical = Categorical(self.data)
        self.decimalscaling = DecimalScaling(self.data)
        self.compression = Compression(self.data)


    def printData(self):
        print(self.data)

    def save(self, saveData):
        toBeDownloaded = {}
        for column in saveData.columns.values:
            toBeDownloaded[column] = saveData[column]

        newFileName = "processed.csv"
        pd.DataFrame(saveData).to_csv(newFileName, index=False)



ps = Preprocessor("file.csv")
#data = ps.standardization.column("age")
#data = ps.standardization.column("income")
data = ps.normalization.completeData()
data = ps.decimalscaling.completeData()
data = ps.compression.lossy(2)
ps.save(data)