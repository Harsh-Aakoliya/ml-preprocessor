import pandas as pd

class Impute:
  data=0

  def __init__(self,data):
    self.data=data
    
  def fillwithmean(self,colname):
    try:
      self.data[colname]=self.data[colname].fillna(self.data[colname].mean())
    except KeyError:
      raise KeyError("colname \"",colname,"\" is not present in given CSV file")
    except TypeError:
      raise TypeError("colname \"",colname,"\" has not proper data type. try on another column")
    return self.data

  def fillwithmedian(self,colname):
    try:
      self.data[colname]=self.data[colname].fillna(self.data[colname].median())
    except KeyError:
      raise KeyError("colname \"",colname,"\" is not present in given CSV file")
    except TypeError:
      raise TypeError("colname \"",colname,"\" has not proper data type. try on another column")
    return self.data

  def fillwithmode(self,colname):
    try:
      self.data[colname]=self.data[colname].fillna(self.data[colname].mode()[0])
    except KeyError:
      raise KeyError("colname \"",colname,"\" is not present in given CSV file")
    except TypeError:
      raise TypeError("colname \"",colname,"\" has not proper data type. try on another column")
    return self.data
    
  def removecol(self,colname):
    try:
      self.data.drop(colname.split(" "), axis = 1, inplace = True)
    except KeyError:
      raise KeyError("colname \"",colname,"\" is not present in given CSV file")
    return self.data

  def nullValues(self):
    nullValues={}
    for col in self.data.columns.values:
      nullValues[col]=sum(pd.isnull(self.data[col]))
    return nullValues
