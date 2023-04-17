import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
class Catagorical:
   data=0
  def __init__(self,data):
    self.data=data
  
  def hotEncoding(self,colname):
    data[colname]=data[colname].astype('category')
    newcol=colname+"_new"
    #Assigning numerical values and storing it in another columns
    data[newcol]=data[colname].cat.codes
    #Create an instance of One-hot-encoder
    enc=OneHotEncoder()
    enc_data=pd.DataFrame(enc.fit_transform(data[[newcol]]).toarray())
    #Merge with main
    New_df=data.join(enc_data)
 
