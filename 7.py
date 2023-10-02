Nome = str(input('Digite seu nome: '))
Email = str(input('Digite seu email: '))
Idade = int(input('Digite sua idade: '))
if Idade < 18:
    print('Você é de menor, não pode entrar no site')
if Idade >= 18:
    print('Parabéns, seja bem vindo ao site!')