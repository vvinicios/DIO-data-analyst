# Eliminar registros duplicados/repetidos dentro de uma lista 
# Conjunto sempre representados por {}
print(set([1, 2, 3, 1, 3, 4]))

print(set("abacaxi"))

print(set(('Palio', 'Gol', 'Celta', 'Palio')))

# Converter valores do SET em uma lista para acessar itens atraves do index
carros = set(('Palio', 'Gol', 'Celta', 'Palio'))

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Set: trabalhando com conjuntos
conjunto_a = {1,2,3,4,5,6,7,8,9,0}
conjunto_b = {2,4,6,8,0}

conjunto_uniao = conjunto_a.union(conjunto_b) # Método de uniao

conjunto_intersection = conjunto_a.intersection(conjunto_b) # Dados em comum

conjunto_difference = conjunto_a.difference(conjunto_b) # Apenas valores diferentes

print(f''' \n Todos numeros juntos: {conjunto_uniao} \n Números que aparecem nos dois conjuntos: {conjunto_intersection} \n Números únicos nos 3 conjuntos: {conjunto_difference} \n'''
      )

# Para acessar um conjunto é preciso transformar-lo em lista
lista_a = list(conjunto_a)
print(lista_a)

# ADD - adicionar elementos não existentes
sorteio = {1, 23, 77, 0, 99, 89, 123, 321}
sorteio.add(23)
sorteio.add(21)

# Clear - limpar o conjunto
sorteio.clear()

# Copy - criar uma cópia do conjunto
sorteio.copy()

# Discart - remover um valor específico, se passar valor que existe ele descarta, caso contrário ele roda
sorteio.discart(1)

# POP - eliminar o primeiro valor
sorteio.pop()

# Remove - remove o retira o elemento específico, caso não exita ele retorna um erro
sorteio.remove(45)

# Len - informar o tamanho do conjunto
len(sorteio)

# Verificar valor específico
1 in sorteio # True
10 in sorteio # False