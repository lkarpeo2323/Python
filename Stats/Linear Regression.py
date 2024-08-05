from scipy import stats
import pandas as pd

data  = pd.read_excel('Mom_with_word_counts.xlsx')
under = data['Clicks']
over = data['Word Count']

slope, intercept, r, p, std_err = stats.linregress(under, over)

print('r is:',r)
print('p is:', p)
