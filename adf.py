import numpy as np
import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('canada.xlsx')
df = pd.DataFrame(data, columns= ['interest','inflation'])
from statsmodels.tsa.stattools import adfuller
def adf_test(timeseries):
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, regression='ct', autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
adf_test(data['inflation'])
