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

telefone = contatos['email2@email']['telefone']
print(telefone)

# Percorrendo todos os valores do dicionário
for chave, valor in contatos.items():
    print(chave, valor)

