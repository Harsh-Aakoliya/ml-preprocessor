import pandas as pd
# from datadescription import DataDescription
from sklearn.preprocessing import StandardScaler

class Standardization:

    def __init__(self, data):
        self.data = data
    
    def column(self, columns):
        for column in columns:
            try:
                mean = self.data[column].mean()
                standard_deviation = self.data[column].std()
                self.data[column] = (self.data[column] - mean)/(standard_deviation)
            except:
                raise Exception("Invalid....")
        return self.data
            
    def completeData(self):
        try:
            self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
        except:
            raise Exception("Invalid!")
        return self.data