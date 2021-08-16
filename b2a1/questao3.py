from os import replace
with open('fitasdna.txt', 'r') as v: 
    r = v.readlines()
print (r)
i=0
while i < len(r):
    x = r[i]
    j1 = x.replace('A','U')
    j2 = j1.replace('T','A')
    j3 = j2.replace('G','C')
    j4 = j3.replace('C','G')
    print('\n')
    print(('Linha'),(i+1),('original: '),(x))
    print(('Transcrição linha'),(i+1),(':'),(j4.upper()))
    i=i+1