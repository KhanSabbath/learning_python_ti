import numpy as np
import pandas as pd
#from pandas import Series, DataFrame

obj = pd.Series([4, 7, -5, 3])
print(obj)  #Out:   0    4
            #       1    7
            #       2   -5
            #       3    3
            #       dtype: int64
obj2=pd.Series([4,5,8,-1], index=['a','g','t','i'])
print(obj2) #Out:   a  4
            #       g  5
            #       t  8
            #       i -1
            #       dtype: int64
print(obj2.index)   #Out: index[('a','g','t','i'), dtype:'object']
print(obj2[obj2>0]) #Ele printaria somente 3 valores da serie e seus tipos
print(np.exp(obj2)) #Out:   d 403.428793
                    #       b 1096.633158
                    #       a 0.006738
                    #       e 20.085537
                    #       dtype: float64
print( )
print( '----------')
print( )

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'], 'year':[2000,2001,2002,2000,2001,2002], 'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
data=pd.DataFrame(data)

###----------------------------------

obj3=pd.Series(['blue','yellow','red'], index=[1,3,4])
print(obj3.reindex(range(6), method='ffill'))   # Ele completa  


#pip install pandas.datareader
import pandas_datareader .data as web
all_data = {ticker: web.get_data_yahoo(ticker)
    for ticker in [ 'AAPL ', ' IBM ', 'MSFT' , 'GOOG'] }
price = pd.DataFrame({ticker : data['Adj Close']
    for ticker, data in all_data.items()})
volume = pd.DataFraMe({ticker: data[ 'Volume']
for ticker , data in all_data.iteMs()})

