# Para dados numéricos, o pandas utiliza o valor de ponto flutuante NaN (Not a Number) para representá-los. Esse valor é chamado de valor de
# sentinela, e pode ser facilmente detectado: 

string_data = pd.series(['aardvark', 'artichoke', np.nan, 'avocado'])

string_data #Out:   0        aardvark
#                   1        arti.choke
#                   2        NaN
#                   3        avocado
#                   dtype:   object
string_data.isnull()  # Out:    0       False
#                               1       False
#                               2       True
#                               3       False
#                               dtype:  bool 
