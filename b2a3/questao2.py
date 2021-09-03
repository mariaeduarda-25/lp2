N, M = [int(j) for j in input().split()]
I, R = [int(j) for j in input().split()]

contaminado = []
contaminado.append(I)

for j in range(1,M+1):
    evento = [int(j) for j in input().split()[1:]]
    if(j > R-1):
        if any(p in contaminado for p in evento):
            contaminado.extend([p for p in evento if p not in contaminado])
print('Contaminados: ', len( contaminado))