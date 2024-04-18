import pandas as pd

class Impute:

    @staticmethod
    def fillwithmean(data, colname):
        try:
            data[colname] = data[colname].fillna(data[colname].mean())
        except KeyError:
            raise KeyError(f"colname \"{colname}\" is not present in given CSV file")
        except TypeError:
            raise TypeError(f"colname \"{colname}\" has not proper data type. try on another column")
        return data

    @staticmethod
    def fillwithmedian(data, colname):
        try:
            data[colname] = data[colname].fillna(data[colname].median())
        except KeyError:
            raise KeyError(f"colname \"{colname}\" is not present in given CSV file")
        except TypeError:
            raise TypeError(f"colname \"{colname}\" has not proper data type. try on another column")
        return data

    @staticmethod
    def fillwithmode(data, colname):
        try:
            data[colname] = data[colname].fillna(data[colname].mode()[0])
        except KeyError:
            raise KeyError(f"colname \"{colname}\" is not present in given CSV file")
        except TypeError:
            raise TypeError(f"colname \"{colname}\" has not proper data type. try on another column")
        return data

    @staticmethod
    def removecol(data, colname):
        try:
            data.drop(colname.split(" "), axis=1, inplace=True)
        except KeyError:
            raise KeyError(f"colname \"{colname}\" is not present in given CSV file")
        return data

    @staticmethod
    def nullValues(data):
        nullValues = {}
        for col in data.columns.values:
            nullValues[col] = sum(pd.isnull(data[col]))
        return nullValues
        
