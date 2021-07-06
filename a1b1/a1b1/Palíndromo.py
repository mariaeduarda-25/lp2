p1=input('Informe uma palavra: ')
p2=p1 [::-1]
tam= len(p1)
cont=0
for i in range(len(p1)):
    if p2[i] == p1[i]:
       cont = cont + 1 
if cont == len(p1):
   print('A palavra é um palíndromo')
else: 
    print('Não é um palíndromo')