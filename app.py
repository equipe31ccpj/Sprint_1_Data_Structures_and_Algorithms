import os

usuarios = []

os.system('cls' if os.name == 'nt' else 'clear')
print('Iniciando Sistema HCA G2...')


print('\n' + ('=~' * 20))
print('1 - Já possuo uma conta.')
print('2 - Criar conta.')
escolha_usuario = int(input('Escolha a opção: '))

while escolha_usuario not in [1, 2]:
	print('Opção inválida!')
	input('Digite qualquer tecla para continuar: ')
	os.system('cls' if os.name == 'nt' else 'clear')
	print('=~' * 20)
	print('1 - Já possuo uma conta.')
	print('2 - Criar conta')
	escolha_usuario = int(input('Escolha a opção: '))

if escolha_usuario == 2:
	usuario = {}

	print('Antes de iniciar a criação da conta, certifique-se que o PowerGrid esteja conectado a uma rede Wi-Fi!\n')

	os.system('cls' if os.name == 'nt' else 'clear')
	print('PERFIL DO USUÀRIO')
	print('=~' * 20)
	email = input('Digite seu e-mail: ')
	tipo_conta = input('Digite o tipo da sua conta: ')
	senha = input('Digite a senha: ')
	conf_senha = input('Digite novamente a senha: ')

	if senha != conf_senha:
		while senha != conf_senha:
			print('Senhas diferentes! Corrija.')
			senha = input('Digite a senha: ')
			conf_senha = input('Digite novamente a senha: ')

	os.system('cls' if os.name == 'nt' else 'clear')
	print('INFORMAÇÕES DO DISPOSITIVO')
	print('=~' * 20)
	endereco = input('Digite o endereço da instalção do carrgador: ')
	num_serie = input('Digite o número de série: ')
	cod_verificacao = input('Digite o código de verificação: ')
	tipo_estacao = input('Digite o tipo de estação: ')

	usuario['e-mail'] = email
	usuario['tipo de conta'] = tipo_conta
	usuario['senha'] = senha
	usuario['endereço'] = endereco
	usuario['número de série'] = num_serie
	usuario['código de verificação'] = cod_verificacao
	usuario['tipo de estação'] = tipo_estacao
	usuarios.append(usuario)

else:
	print(1)		
