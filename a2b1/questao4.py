num = int(input('Informe um número: '))
fatorial = 1
for j in range (num,1,-1):
    fatorial = fatorial*j
    print( num,'! é = :', fatorial)