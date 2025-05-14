## As três linhas de código abaixo mostram como importar  e imprimir um excel com a biblioteca pandas
xlsx = pd.ExcelFile('./exemples/ex1.xlsx')
pd.read_excel(xlsx, 'sheet1')
frame
#out:   a  b  c  d  message
#    0  1  2  3  4  hello 
#    1  5  6  7  8  world
#    2  9  10 11 12 foo 

## Para escrever dados do pandas para o formato Excel
writer = pdExcelWriter('exemples/ex2.xlsx')
frame.to_excel(writer, 'sheet1')
writer.save()  #ou#  frame.to_excel('exemple/ex2.xlsx)

