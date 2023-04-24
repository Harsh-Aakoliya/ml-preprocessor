import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

class Categorical:

  @staticmethod
  def hotEncoding(data,colname):

    # Perform one-hot encoding on the 'gender' column
    one_hot = pd.get_dummies(data[colname])

    # Add the one-hot encoded columns to the original dataframe
    data = pd.concat([data, one_hot], axis=1)

    # Drop the original 'gender' column
    data.drop(colname, axis=1, inplace=True)

    # Create a OneHotEncoder object
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')

    # Fit the encoder to the categorical data
    encoder.fit(data[cat_cols])

    # Transform the categorical columns into one-hot encoded columns
    onehot = encoder.transform(data[cat_cols])

    # Convert the one-hot encoded data into a pandas DataFrame
    onehot_data = pd.DataFrame(onehot, columns=encoder.get_feature_names(cat_cols))

    # Concatenate the one-hot encoded data with the original DataFrame
    data_encoded = pd.concat([data, onehot_data], axis=1)

    # Drop the original categorical columns from the DataFrame
    data_encoded.drop(cat_cols, axis=1, inplace=True)

    return data