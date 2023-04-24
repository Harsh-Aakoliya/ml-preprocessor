import pandas as pd
# from datadescription import DataDescription
from sklearn.preprocessing import MinMaxScaler

class Normalization:

    def __init__(self, data):
        self.data = data
    
    def column(self, columns):
        for column in columns:
            try:
                minValue = self.data[column].min()
                maxValue = self.data[column].max()
                self.data[column] = (self.data[column] - minValue)/(maxValue - minValue)
            except:
                raise Exception("Invalid!")
        return self.data
            
    def completeData(self):
        try:
            self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
        except:
            raise Exception("Invalid!")
        return self.data