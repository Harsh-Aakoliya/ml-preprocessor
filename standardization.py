import pandas as pd
from sklearn.preprocessing import StandardScaler

class Standardization:

    @staticmethod
    def column(data, columns):
        for column in columns:
            try:
                mean = data[column].mean()
                standard_deviation = data[column].std()
                data[column] = (data[column] - mean)/(standard_deviation)
            except:
                raise Exception("Invalid....")
        return data
            
    @staticmethod
    def completeData(data):
        try:
            data = pd.DataFrame(StandardScaler().fit_transform(data))
        except:
            raise Exception("Invalid!")
        return data