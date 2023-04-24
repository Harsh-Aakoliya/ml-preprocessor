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
        self.original_data = 0
        self.compressed_data = 0

    def save(self, saveData):
        toBeDownloaded = {}
        for column in saveData.columns.values:
            toBeDownloaded[column] = saveData[column]

        newFileName = "processed.csv"
        pd.DataFrame(saveData).to_csv(newFileName, index=False)

    def fillwithmean(self, columns):
        self.data = Impute.fillwithmean(self.data, columns)
        return self

    def fillwithmedian(self, columns):
        self.data = Impute.fillwithmedian(self.data, columns)
        return self

    def fillwithmode(self, columns):
        self.data = Impute.fillwithmode(self.data, columns)
        return self

    def fillwithmode(self, columns):
        self.data = Impute.fillwithmode(self.data, columns)
        return self

    def removeColumn(self, column):
        self.data = Impute.removecol(self.data, column)
        return self

    def nullValues(self):
        return = Impute.nullValues(self.data)
    
    def standardizeColumn(self, columns):
        self.data = Standardization.column(self.data, columns)
        return self

    def standardizeData(self):
        self.data = Standardization.completeData(self.data)
        return self

    def normalizeColumn(self, columns):
        self.data = Normalization.column(self.data, columns)
        return self

    def normalizeData(self):
        self.data = Normalization.completeData(self.data)
        return self
    
    def categoricalEncoding(self, column):
        self.data = Categorical.hotEncoding(self.data, column)
        return self
    
    def decimalScaleColumn(self, columns):
        self.data = DecimalScaling.column(self.data, columns)
        return self

    def decimalScaleData(self):
        self.data = DecimalScaling.completeData(self.data)
        return self
    
    def compressLossy(self, clusters):
        self.compressed_data = Compression.lossy(self.data, clusters)
        return self
    def compressNonLossy(self, components):
        self.compressed_data, self.original_data = Compression.lossy(self.data, components)
        return self