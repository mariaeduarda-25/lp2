import csv
with open('notasurfes.csv', 'r') as notas:
    leitura= csv.reader(notas)
    for linha in leitura:
        print(linha)

 soma=quant= media=maior=menor=0
 numero = 0
 soma= soma += num
 quant= += 1

 media = soma/quant

 if quant == 1:
     maior = menor = num
else:
    if num > maior:
        maior = num
    if num < menor:
        menor = num