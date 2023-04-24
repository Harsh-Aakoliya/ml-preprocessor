import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class Categorical:
  data=0
  def __init__(self,data):
    self.data=data
  
  def hotEncoding(self,colname):

    # Perform one-hot encoding on the 'gender' column
    one_hot = pd.get_dummies(self.data[colname])

    # Add the one-hot encoded columns to the original dataframe
    self.data = pd.concat([self.data, one_hot], axis=1)

    # Drop the original 'gender' column
    self.data.drop(colname, axis=1, inplace=True)

    return self.data