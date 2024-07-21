frutas = ('maçã', 'laranja', 'uva', 'pera',)
frutas[1] # laranja
frutas[-3] # Laranja

letras = tuple("Python")
numeros = tuple([1,2,3,4,5])

pais = ('Brasil',) # Colocar a virgula no final como boas práticas

matriz = (
    (1, 'a', 2),
    ('b', 3, 4),
    (6, 5, 'c'),
)

matriz[0] # (1, 'a', 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # 'c'

# Fatiamento
###  
# S - Start
# S - Stap
# S - Stop

tupla = ('p', 'y', 't', 'h', 'o', 'n',)

tupla[2:] # Do terceiro elemento em diante
tupla[:2] # Do terceiro para trás (1, 2)
tupla[1:3] # Entre o segundo e o quarto (2, 3)
tupla[0:3:2] # Do primeiro elemento ao indice 3, pulando de 2 em 2
tupla[::] # Do inicio ao fim
tupla[::-1] # Pegando a ordem invertida

# Enumerate
for indice in enumerate(tupla):
    print(f'{indice}') 

print(tupla.count('t'))
print(tupla.index('p'))
print(len(tupla))