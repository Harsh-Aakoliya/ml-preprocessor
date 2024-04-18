import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Normalization:

    @staticmethod
    def column(data, columns):
        for column in columns:
            try:
                minValue = data[column].min()
                maxValue = data[column].max()
                data[column] = (data[column] - minValue)/(maxValue - minValue)
            except:
                raise Exception("Invalid!")
        return data

    @staticmethod  
    def completeData(data):
        try:
            scaler = MinMaxScaler().fit(data)
            data = pd.DataFrame(scaler.transform(data), columns=data.columns)
        except:
            raise Exception("Invalid!")
        return data

