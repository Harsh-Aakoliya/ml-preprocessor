import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

class DecimalScaling:

    @staticmethod
    def column(data, columns):
        for column in columns:
            try:
                # Compute the scaling factor
                k = int(np.ceil(np.log10(np.max(np.abs(column)))))

                # Normalize the column using decimal scaling
                normalized_col = column / (10 ** k)

                #Replace column
                data[column] = normalized_col
            except:
                raise Exception("Invalid!")
        return data
    
    @staticmethod
    def completeData(data):
        try:
            # Compute the scaling factor for each column
            k = np.ceil(np.log10(np.max(np.abs(data), axis=0)))

            # Normalize the dataset using decimal scaling
            normalized_data = data / (10 ** k)
        except:
            raise Exception("Invalid!")
        return data
        
