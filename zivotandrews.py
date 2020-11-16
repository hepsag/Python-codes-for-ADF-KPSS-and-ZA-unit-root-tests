import numpy as np
import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('canada.xlsx')
df = pd.DataFrame(data, columns= ['interest','inflation'])
from statsmodels.tsa.stattools import zivot_andrews
def zivot_andrews_test(timeseries):
    print('Results of Zivot-Andrews Test:')
    zatest = zivot_andrews(timeseries, regression='ct', autolag='AIC')
    zaoutput = pd.Series(zatest[0:5], index=['Test Statistic','p-value','Critical Values','Lags Used','Break Time'])
    print (zaoutput)
zivot_andrews_test(data['inflation'])
