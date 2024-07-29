# Eliminar registros duplicados/repetidos dentro de uma lista 
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

