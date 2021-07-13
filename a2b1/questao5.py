num = int(input('Informe um número: '))
v= []
i = 1
while i != num:
    h = 0
    for j in range(1, i+1): 
        if (i % j == 0)and(i!=2):
            h = h + 1
if h==2:
    v.append(i)
    i = i + 1
    print('Os números primos  entre 1 e ',num,'são:',v)