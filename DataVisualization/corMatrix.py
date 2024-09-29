import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from sklearn.linear_model import LinearRegression

# reads csv as a pandas data frame
df = pd.read_csv('data.csv',
                 header=None,
                 sep=',')

# marks columns with abbreviations
df.columns = ['REACT', 'CMMNT', 'SHARE', 'LIKES', 'LOVES']

# generates and prints correlation matrix
corr_matrix = df.corr()
print(corr_matrix)

# plots and displays a heat-map based on correlation matrix values
sb.heatmap(corr_matrix, annot=True, cmap="Blues")
plt.show()

# plots and displays 5 box plots based on all 5 columns of the df
b_plot = df.boxplot()
b_plot.plot()
plt.show()

# plost and displays 5 histograms based on all 5 columns of the df
hist = df.hist(bins=100, layout=(1, 5), figsize=(12, 4))
plt.show()

lr = LinearRegression()

X = df.loc[:, 'REACT'].values.reshape(-1, 1)
Y = df.loc[:, 'LIKES'].values.reshape(-1, 1)
lr.fit(X, Y)
y_predictor = lr.predict(X)

df.plot.scatter('REACT', 'LIKES')
plt.plot(X, y_predictor, color='red')
plt.show()

# second regression line
X = df.loc[:, 'SHARE'].values.reshape(-1, 1)
Y = df.loc[:, 'CMMNT'].values.reshape(-1, 1)
lr.fit(X, Y)
y_predictor = lr.predict(X)

df.plot.scatter('SHARE', 'CMMNT')
plt.plot(X, y_predictor, color='red')
plt.show()

# third regression line
# X is same as above
Y = df.loc[:, 'LOVES'].values.reshape(-1, 1)
lr.fit(X, Y)
y_predictor = lr.predict(X)

df.plot.scatter('SHARE', 'LOVES')
plt.plot(X, y_predictor, color='red')
plt.show()
