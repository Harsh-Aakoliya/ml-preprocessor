import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

class DecimalScaling:

    def __init__(self, data):
        self.data = data
    
    def column(self, columns):
        for column in columns:
            try:
                # Compute the scaling factor
                k = int(np.ceil(np.log10(np.max(np.abs(column)))))

                # Normalize the column using decimal scaling
                normalized_col = column / (10 ** k)

                #Replace column
                self.data[column] = normalized_col
            except:
                raise Exception("Invalid!")
        return self.data
            
    def completeData(self):
        try:
            # Compute the scaling factor for each column
            k = np.ceil(np.log10(np.max(np.abs(self.data), axis=0)))

            # Normalize the dataset using decimal scaling
            normalized_data = self.data / (10 ** k)
        except:
            raise Exception("Invalid!")
        return self.data