import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class Categorical:
  data=0
  def __init__(self,data):
    self.data=self.data
  
  def hotEncoding(self,colname):
    self.data[colname]=self.data[colname].astype('category')
    newcol=colname+"_new"
    #Assigning numerical values and storing it in another columns
    self.data[newcol]=self.data[colname].cat.codes
    #Create an instance of One-hot-encoder
    enc=OneHotEncoder()
    enc_data=pd.self.dataFrame(enc.fit_transform(self.data[[newcol]]).toarray())
    #Merge with main
    New_df=self.data.join(enc_data)

    return self.self.data
 
