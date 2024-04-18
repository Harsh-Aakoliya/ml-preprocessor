import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

class Compression:

    @staticmethod
    def nonLossy(data, components):
        try:
            # Select only numerical columns from data
            numerical_data = data.select_dtypes(include=[np.number])

            # Instantiate a PCA object with the desired number of components
            pca = PCA(n_components=components)

            # Fit and transform the numerical data using PCA
            compressed_data = pca.fit_transform(numerical_data)

            # Inverse transform the compressed data to obtain the original numerical data
            original_numerical_data = pca.inverse_transform(compressed_data)

            # Replace the numerical columns in the original data with the compressed numerical data
            original_data = data.copy()
            original_data[numerical_data.columns] = original_numerical_data

        except:
            raise Exception("Invalid!")
        return compressed_data, original_data

    @staticmethod
    def lossy(data, clusters):
        try:
            # Select only numerical columns
            numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
            numerical_data = data[numerical_cols]

            # Instantiate a KMeans object with the desired number of clusters
            kmeans = KMeans(n_clusters=clusters)

            # Fit the numerical data using KMeans
            kmeans.fit(numerical_data)

            # Quantize the numerical data by replacing each feature with the nearest cluster center
            compressed_data = kmeans.cluster_centers_[kmeans.predict(numerical_data)]

            # Combine the compressed numerical data with the non-numerical columns
            compressed_data = pd.concat([data.drop(columns=numerical_cols), pd.DataFrame(compressed_data, columns=numerical_cols)], axis=1)
        except:
            raise Exception("Invalid!")
        return compressed_data


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

class Categorical:

  @staticmethod
  def hotEncoding(data, colname):
    # Perform one-hot encoding on the column
    one_hot = pd.get_dummies(data[colname])

    # Add the one-hot encoded columns to the original dataframe
    data = pd.concat([data, one_hot], axis=1)

    # Drop the original column
    data.drop(colname, axis=1, inplace=True)

    # Check if the column exists before fitting the encoder
    if colname in data.columns:
        # Create a OneHotEncoder object
        encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')

        # Fit the encoder to the categorical data
        encoder.fit(data[[colname]])

        # Transform the categorical columns into one-hot encoded columns
        onehot = encoder.transform(data[[colname]])

        # Convert the one-hot encoded data into a pandas DataFrame
        onehot_data = pd.DataFrame(onehot, columns=encoder.get_feature_names([colname]))

        # Concatenate the one-hot encoded data with the original DataFrame
        data_encoded = pd.concat([data, onehot_data], axis=1)

        # Drop the original categorical columns from the DataFrame
        data_encoded.drop(colname, axis=1, inplace=True)

        return data_encoded
    else:
        return data


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
            scaler = MinMaxScaler().fit(data.select_dtypes(include=[np.number]))
            data[data.select_dtypes(include=[np.number]).columns] = scaler.transform(data.select_dtypes(include=[np.number]))
        except:
            raise Exception("Invalid!")
        return data


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
        numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
        try:
            data[numeric_cols] = pd.DataFrame(StandardScaler().fit_transform(data[numeric_cols]))
        except:
            raise Exception("Invalid!")
        return data

class DataInput:
    def inputFunction(self, filepath):

        #read csv file into data
        try:
            data = pd.read_csv(filepath)
        except:
            print("Error! The file doesn't exist or it's empty")

        #lowercase
        for column in data.columns.values:
            data.rename(columns = {column : column.lower()}, inplace = True)
            
        return data

class Preprocessor:

    data = 0

    def __init__(self, filepath):
        self.data = DataInput().inputFunction(filepath)
        self.original_data = 0
        self.compressed_data = 0

    def save(self):
        toBeDownloaded = {}
        for column in self.data.columns.values:
            toBeDownloaded[column] = self.data[column]

        newFileName = "processed.csv"
        pd.DataFrame(self.data).to_csv(newFileName, index=False)

    def fillwithmean(self, column):
        self.data = Impute().fillwithmean(self.data, column)
        return self

    def fillwithmedian(self, column):
        self.data = Impute().fillwithmedian(self.data, column)
        return self

    def fillwithmode(self, column):
        self.data = Impute().fillwithmode(self.data, column)
        return self

    def removeColumn(self, column):
        self.data = Impute().removecol(self.data, column)
        return self

    def nullValues(self):
        return Impute().nullValues(self.data)
    
    def standardizeColumn(self, columns):
        self.data = Standardization().column(self.data, columns)
        return self

    def standardizeData(self):
        self.data = Standardization().completeData(self.data)
        return self

    def normalizeColumn(self, columns):
        self.data = Normalization().column(self.data, columns)
        return self

    def normalizeData(self):
        self.data = Normalization().completeData(self.data)
        return self
    
    def categoricalEncoding(self, column):
        self.data = Categorical().hotEncoding(self.data, column)
        return self
    
    def decimalScaleColumn(self, columns):
        self.data = DecimalScaling().column(self.data, columns)
        return self

    def decimalScaleData(self):
        self.data = DecimalScaling().completeData(self.data)
        return self
    
    def compressLossy(self, clusters):
        return Compression().lossy(self.data, clusters)

    def compressNonLossy(self, components):
        return Compression().nonLossy(self.data, components)

ps = Preprocessor("file.csv")
print(ps.nullValues())
# ps.fillwithmean("salary")
# ps.fillwithmedian("salary")
# ps.fillwithmode("salary")
# ps.removeColumn("city")
# ps.normalizeData()
# ps.normalizeColumn(["experience"])
# ps.categoricalEncoding("gender")
print(ps.compressLossy(2))



#another examples.
from rhinorefine import Preprocessor
preprocessor = Preprocessor('file.csv')



# TODO: Fill with mean, median and mode 
# preprocessor.fillwithmean("age")
# preprocessor.fillwithmedian("age")
# preprocessor.fillwithmode("age")


#TODO: Removing columns
# preprocessor.removeColumn("age")


#TODO: finding null values
#so it will print all the null values from giving csv file
# print(preprocessor.nullValues())

#TODO: standerisation all the columns
# preprocessor.standardizeColumn(["age"])
# preprocessor.standardizeData()


#TODO: it will normalize all the columns between [0,1]
# preprocessor.normalizeColumn(['age'])
# print(preprocessor.normalizeData())


#TODO: categorical encoding i.e. onehot encoding
# preprocessor.categoricalEncoding("gender")



preprocessor1=Preprocessor("temp.csv")
#TODO: K means clustering algorithm. no of clusters we have to pass as an argument
# print(preprocessor1.compressLossy(3))
 
#TODO: PCA as an argument we have to pass no of dimension in which we have to reduce
print(preprocessor1.compressNonLossy(2))


#finally for saving processed csv file
preprocessor.save()
print(ps.compressNonLossy(2)[0],ps.compressNonLossy(2)[1])
ps.save()
