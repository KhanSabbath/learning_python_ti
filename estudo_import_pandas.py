#df = pd.read_csv('exemples/ex1.csv')
    #outros comandos são:
    # read_table
        # _fwf
        # _clipboard
        # _hdf
        # _html
        # _json
        # _msgpack
        # _pickle
        # ...

#Seja um arquivo 
#examples/ex1.csv           #localização do arquivo e seu nome
#a, b, c, d, message        #conteúdo
#1, 2, 3, 4, hello
#5, 6, 7, 8, world
#9, 10, 11, 12, foo
#teste

#!cat examples/ex1.csv      #Este comando imprime o conteudo puro do arquivo na tela  #por algum motivo está com problemas
df=pd.read_csv('example/ex2.csv')
print(df)

#Seja um arquivo 
#examples/ex2.csv            #localização do arquivo e seu nome
#1, 2, 3, 4, hello           #conteúdo sem um cabeçalho
#5, 6, 7, 8, world
#9, 10, 11, 12, foo

!cat examples/ex2.csv       # Este comando imprime na tela o conteúdo puro do arquivo
df2=pd.read_csv('example/ex2.csv', header=None) #opção com cabeçalho 'default'
print(df2)
# O que é printado:
#      0   1   2   3   4
#   0  1   2   3   4   hello
#   1  5   6   7   8   world
#   2  9   10  11  12  foo

#Seja a list oriunda de um arquivo desorgonizada
list(open('examples/ex3.txt'))
#Out:   [' A B C\n',
#       'aaa -0.264438 -1.026059 -0.619500\n',
#       'bbb 0.927272 0.302904 -0.032399\n',
#       'ccc -0.264273 -0.386314 -0.217601\n',
#       'ddd -0.871858 -0.348382 1.100491\n'] 

## É possível organizar a lista desorganizada com base nos espaçamentos
## ela fica assim:
result=pd.read_table('examples/ex3.txt',sep='\s+')
print result
#           A           B           C
#   aaa     0.264438    -1.026059   0.619500
#   bbb     0.927272    0.302904    0.032399
#   ccc     0.264273    0.386314    0.217601
#   ddd     0.871858    0.348382    1.100491

