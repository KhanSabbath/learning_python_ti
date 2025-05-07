##  EXERCÍCIO 1
#from datetime import datetime, timedelta
#data=datetime.now()
#datafutura=data+timedelta(2)
#print(f'a data adual é: {data}')
#print(f'a data daqui a dois dias será: {datafutura}')



##  EXERCÍCIO 2
#frase='Exercício de Java'
#print(frase.replace('Java', 'Python'))



##  EXERCÍCIO 3
#def par_impar(num):
#    if num % 2 == 0:
#        return f'é par'
#    return f'é impar'
#num=print(input("digite um número: "))
#print(par_impar(num))



##  EXERCÍCIO 4
#sequence = [1, 2, 0, 4, 6, 5, 2, 1]
#total_until_5 = 0
#for value in sequence:
#    print (f'índice: {value}')
#    if value == 5:
#        break
#    print(f'verificando acréssimo antes: {total_until_5}')
#    total_until_5 += value
#    print(f'verificando acréssimo depois: {total_until_5}')


##  FOR - EXEMPLO LAÇO
#for i in range(4):
#    for j in range(4):
#        if j>i:
#            break
#        print((i,j))  #OUT: ((0, 0)(1, 0)(1, 1)(2, 0)(2, 1)(2, 2)(3, 0)(3, 1)(3, 2)(3, 3))



##  EXEMPLO LAÇO
#x=250
#total=0
#while x>0:
#    if total>500:
#        break
#    total += x
#    x=x//2
#    print(f'x={x} e total={total}')
#
#b = [ 'saw' , 'SfTla l l' , ' He' , 'foxes' , 'si.x' ]
#b.sort(key=len)



##  REGEX  -  EXEMPLO
#states=[' Alabama', 'Geogia!!','Georgia', 'georgia', 'FlOrida', 'south carolina##', 'West virginia']
#import re
#def clean_strings(strings):
#    result=[]
#    for value in strings:
#        value=value.strip()
#        value=re.sub('[!#?]', '', value)
#        value=value.title()
#        result.append(value)
#    return result
#
#print(clean_strings(states))



##    Lambda
#def soma(a):
#    return a*2
## a função acima é equivalente a abaixo:
#equivalente=lambda soma: a*2



##   Geradores 1#
#dic={'antonio':1,'beto':2,'cláudio':3,'diego':4}
#for i in dic:
#    print(i)
#dic_interativo= iter(dic)
#print(dic_interativo)   # isso printa o código do objeto, fica feio
#print(list(dic_interativo))    # assim printatemos o conteúdo do dic

##  Geradores 2#
#def squares(n=10):
#    print('Generating squares from 1 to {0}'.format(n**2))
#    for i in range(1, n+1):
#        yield i**2
###  Quando charmarmos a função, nada será gerado sem pedirmos, por exemplo:
#gen = squares()
#print(gen)  # aqui será printando o código do objetos
###  Só será gerado se execurtamos assim:
#for x in gen:
#    print(x, end=' ')   # OUT: 1 4 9 16 25 36 49 64 81 100

##Arquivos e o sistema operacional
#path='exemplos/segismundo.txt'
#lines=[x.rstrip() for x in open[path]]   #r = right strip() ou seja: limpar tudo q seja espaço ou em branco à direita
#f = open(path)
##f=open(path, 'w' )   # CUIDADO!!! ESSE COMANDO SOBRESCREVE TUDO NO PATH
#print(f)    # não dá! precisa alguma forma declara um "r" no comando
#for line in f:
#    pass
#lines=[x.rstrip() for x in open(path)]
#print(lines)
#f.close() #LIBERA O ESPAÇO, TBM PODE SER USADO COM O SEGUINTE COMANDO:
#with open(path) as f:
#    lines=[x.rstrip for x in f]  #"   olá".lstrip()  # Resultado: "olá"

## Numpay                                               #    Sem Numpy
import numpy as np                                      #
#My_arr = np.arange(1000000)                             #
#my_list=list(range(1000000))                            #
#%time for _ in range(10): My_arr2 = My_arr * 2          #  %time for _ in range(10): my_list2 = [x*2 for x in my_list]
##OUT: CPU tiMes: user 20 Ms, sys: 10 Ms, total: 30 MS   # OUT: CPU ti.l'les: user 680 l'lS, sys: 180 l'lS, total: 860 l'lS
##     Wall tiMe: 31.3 MS                                # Wall ti.l'le: 861 l'lS

#data=np.random.randn(2,3)   
#print(data)                    # OUT:  [[ 0.123, -1.456,  0.789],              #operações podem escalares e matriciais podem ser realizadas sobre os objetos
                                # OUT:   [ 1.234, -0.567, -0.890]]              # exemplo: data*2    #ou#   data+data

datal= [6, 7.5, 8, 0, 1]
arr1 = np.array(datal)
#print(arr1)
data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
#print(arr2)                 # podemos saber quantas dimensões há em arr2 com o comando:      arr2.ndim  #out: 2
                            # tbm podemos saber quantas linhas/col com o comando:           arr2.shape  #out:(2,4)

#print(arr2.mean(axis=1))

data3= ([1,2,3],[4,5,6],[7,8,9])   #isso é uma tupla
data4= np.array([[1,1,-2],[2,3,4],[4,3,2]])  #isso é uma array de inteiros
try:
    print(np.det(data3))    #não é possível calcular a determinante de uma matriz de tuplas
except:
    print('erro com data3')

try: 
    print(f'a determinante é: {np.linalg.det(data4)}')
except:
    print('Erro com data4')

    
