from scipy.stats import skew, skewtest
import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
iris_dataframe = pd.DataFrame(data=iris.data, columns=iris.feature_names)


print(iris_dataframe.corr()) #Correlation
print(iris_dataframe.cov() )#Covariance


