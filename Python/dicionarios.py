# Conjunto não ordenado com Chave e Valor
# {Chave: Valor}
# Chave: precisa ser um objeto imutável, tupla, string, etc

pessoa = {'nome': 'Vinicios', 'idade': 21}
pessoa = dict(nome='Vinicios', idade=21)

# Adicionar nova chave
pessoa['telefone'] = '7777-9999'

dados = {'nome': 'Vinicios', 'idade': 21, 'telefone': '7777-9999'}

# Aninhar dicionários
contatos = {
    'email@email': {'nome': 'Vinicios', 'idade': 21, 'telefone': '7777-9999'},
    'email2@email': {'nome': 'Vinicios', 'idade': 21, 'telefone': '7777-9999'},
    'email3@email': {'nome': 'Vinicios', 'idade': 21, 'telefone': '7777-9999'}
}

# Acessar dicionários aninhados listando as chaves que desejo acessar
telefone = contatos['email2@email']['telefone']
print(telefone)

# Percorrendo todos os valores do dicionário
for chave, valor in contatos.items():
    print(chave, valor)

# Acessar valores dos dicionários
dados['nome']
dados['idade']
dados['telefone']

# Substituir os valores do dicionário
dados['nome'] = 'Lucas'
dados['idade'] = 22

# Copy - cópia do dicionário
copia = contatos.copy()

# Clear - limpar o dicionário
#limpo = contatos.clear()

# fromkeys - criar chaves no dicionário
dict.fromkeys(['nome', 'telefone'])
dict.fromkeys(['nome', 'telefone'], 'vazio')

# Get - acessar valores dentro do dicionário quando não sabemos se a chave existe ou não
contatos.get('chave')
contatos.get('chave', {})

# Items - retorna uma lista de tuplas
print(contatos.items())

# Keys - retorna as chaves do dict
print(contatos.keys())

# Pop - excluir o valor de uma chave
print(contatos.pop('chave', 'Não encontrou'))

# Popitem - ele retira os itens na sequencia
#contatos.popitem()

# Setdefaoult - substituir caso não exita a chave
contatos.setdefault('nome', 'Adriana')

# Update - atualiza o dict com outro dict

# Values - retorna apenas os valores
print(contatos.values())

# Verificar se determinado valor e  uma chave dentro do dict
resultado = 'email@email' in contatos
print(resultado)

resultado = 'email@email' in contatos['email@email']
print(resultado)

# Del - tirar valores do dict
del contatos['email3@email']['telefone']
del contatos['email@email']

print(contatos)