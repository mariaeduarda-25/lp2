dicionário= {'UUU':'Fenil-alanina', 'UUC':'Fenil-alanina',
    'UUA':'Leucina', 'UUG':'Leucina','CUU':'Leucina', 'CUC':'Leucina','CUA':'Leucina', 'CUG':'Leucina',
    'AUU':'Isoleucina', 'AUC':'Isoleucina','AUA':'Isoleucina','AUG':'start codon',
    'GUU':'Valina', 'GUG':'Valina','GUA':'Valina', 'GUC':'Valina',
    'UCU':'Serina', 'UCC':'Serina','UCA':'Serina','UCG':'Serina',
    'CCU':'Prolina','CCC':'Prolina', 'CCA':'Prolina','CCG':'Prolina',
    'ACU':'Treonina','ACC':'Treonina', 'ACA':'Treonina','ACG':'Treonina',
    'GCU':'Alanina','GCC':'Alanina', 'GCA':'Alanina','GCG':'Alanina',
    'UAU':'Tirosina','UAC':'Tirosina', 'UAA':'Stop codon','UAG':'Stop codon',
    'CAU':'Histidina', 'CAC':'Histidina','CAA':'Glutamina','CAG':'Glutamina',
    'AAU':'Asparagina','AAC':'Asparagina','AAA':'Lisina', 'AAG':'Lisina',
    'GAU':'Acido aspartico', 'GAC':'Acido aspartico','GAA':'Acido Glutamico', 'GAG':'Acido Glutamico',
    'UGU':'Cysteine','UGC':'Cysteine', 'UGA':'Stop codon','UGG':'Tryptophan',
    'CGU':'Arginina','CGC':'Arginina', 'CGA':'Arginina','CGG':'Arginina',
    'AGU':'Serina', 'AGC':'Serina','AGA':'Arginina', 'AGG':'Arginina',
    'GGU':'Glicina', 'GGC':'Glicina','GGA':'Glicina','GGG':'Glicina'}
from os import replace
with open('fitasdna.txt', 'r') as fitas: 
    arquivo = fitas.readlines()
print (arquivo)
i=0
while i < len(arquivo):
    y = arquivo[i]
    w1= y.replace('A','U')
    w2 = w1.replace('T','A')
    w3 = w2.replace('G','C')
    w4 = w3.replace('C','G')
    w4 = w4.upper()
    j=3
    print('\n')
    print('Aminoácidos sintetizados:',(i))
    while j < len(w4):
        x1= ''
        x1 = w4[j-3]
        x1 += w4[j-2]
        x1 += w4[j-1]
        print (dicionário[x1])
        j+=1
    i=i+1