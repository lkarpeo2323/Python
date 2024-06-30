from scipy.stats import skew, skewtest
import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
iris_dataframe = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Calculate skewness and perform skewness test for 'petal length (cm)'
variable = iris_dataframe['petal length (cm)']
s = skew(variable)
zscore, pvalue = skewtest(variable)

# Print the results
print('Skewness: %0.3f | z-score: %0.3f | p-value: %0.3f' % (s, zscore, pvalue))
