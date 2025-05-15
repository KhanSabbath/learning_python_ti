## Carregar dados de SQL para um DataFrame é razoavelmente
## simples, e o pandas tem algumas funções para simplificar o
## processo. Como exemplo, criarei um banco de dados SQLite 

import sqlite3

query =  """
    CREATE TABLE test
        (a VARCHAR(20), b VARCHAR(20), c real, d integer); """

con = sqlite3.connect('mydata.sqlite')
con.execute(query)     # <sqli.te3.Cursor at 0x7fb7361b4b90> 
con.commit()
#Em seguida, inserimos algumas linhas de dados:
data= [('Atlanta', 'Georgi.a', 1.25, 6),( 'Tallahassee', 'Flori.da', 2.6, 3),('SacraMento', 'Cali.forni.a', 1.7, 5)] 
stmt = "lNSERT lNTO test VALUES(?, ?, ?, ?)"
con.executeMany(stMt, data) 
## Out <sqli.te3.Cursor at 0x7fb7396d25e0>
con .COMMi.t() 




# A maioria dos drivers de SQL de Python (PyODBC, psycopg2, MySQLdb, pymssql etc.) devolve uma lista de tuplas
# ao selecionar dados de uma tabela

cursor= con.execute('select * from test')
rows = cursor.fetchall()
rows # OUT: [('Atlanta', 'Georgia', 1.25, 6),
#           ( 'Tallahassee', 'Florida', 2.6, 3),
#           ('Sacramento', 'California', 1.7, 5)] 
