f= open('fitasdna.txt', 'r')
fita = f.readline
fita = f.readline
fita = f.readline
for linha in f:
   if 'A' in linha:
      fita = f.readline().replace('A','T')
   elif 'T' in linha:
        fita = f.readline().replace('T','A')
   elif 'C' in linha:
      fita = f.readline().replace('C','G')
   else:
       fita = f.readline().replace('G','C')
print(fita)