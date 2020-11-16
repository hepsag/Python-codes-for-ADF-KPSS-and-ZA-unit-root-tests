import numpy as np
import pandas as pd
import statsmodels.api as sm
data = pd.read_excel('canada.xlsx')
df = pd.DataFrame(data, columns= ['interest','inflation'])
from statsmodels.tsa.stattools import kpss
def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='ct', nlags="auto")
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Truncation Lag'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print (kpss_output)
kpss_test(data['interest'])
