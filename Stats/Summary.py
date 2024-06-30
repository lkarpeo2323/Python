import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    'Name' : ['Leo', 'Cooper', 'Carl', 'Annie'],
    'Age' : [19,48,27,21],
    'Gender' : ['M','M','M','F'],
    'Salary' : [50000,70000,60000,80000],
    'City' : ['Great Neck', 'Seattle', 'Kansas City', 'Miami']
    }

df = pd.DataFrame(data)

summary = df.describe(include='all')
print(summary)
    
