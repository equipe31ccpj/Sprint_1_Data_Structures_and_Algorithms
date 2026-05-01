import os
import sys
import time

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
	criar_email = input('Digite seu e-mail: ')
	tipo_conta = input('Digite o tipo da sua conta: ')
	criar_senha = input('Digite a senha: ')
	conf_senha = input('Digite novamente a senha: ')

	if criar_senha != conf_senha:
		while criar_senha != conf_senha:
			print('Senhas diferentes! Corrija.')
			entrar_senha = input('Digite a senha: ')
			conf_senha = input('Digite novamente a senha: ')

	os.system('cls' if os.name == 'nt' else 'clear')
	print('INFORMAÇÕES DO DISPOSITIVO')
	print('=~' * 20)
	endereco = input('Digite o endereço da instalção do carrgador: ')
	num_serie = input('Digite o número de série: ')
	cod_verificacao = input('Digite o código de verificação: ')
	tipo_estacao = input('Digite o tipo de estação: ')

	usuario['email'] = criar_email
	usuario['tipo de conta'] = tipo_conta
	usuario['senha'] = criar_senha
	usuario['endereço'] = endereco
	usuario['número de série'] = num_serie
	usuario['código de verificação'] = cod_verificacao
	usuario['tipo de estação'] = tipo_estacao
	usuarios.append(usuario)
	print('Conta criada com sucesso!')
	time.sleep(5)	
else:
	pass

entrar = False


while not entrar:
	os.system('cls' if os.name == 'nt' else 'clear')
	print('Entrar na conta.')
	entrar_email = input('Digite seu e-mail: ')
	entrar_senha = input('Digite a senha: ')

	conf_entrar_email = False
	conf_entrar_senha = False

	for usuario in usuarios:
		if entrar_email == usuario['email']:
			conf_entrar_email = True
			if entrar_senha == usuario['senha']:
				conf_entrar_senha = True
				break
	if conf_entrar_email == True and conf_entrar_senha == True:
		entrar = True
	else:		
		encerrar = False	
		while not encerrar:
			novamente = input('e-mail ou senha incorretas! Deseja tentar novamente: ')
			if novamente.lower() == 'sim':
				break
			elif novamente.lower() == 'não':
				print('Saindo do sistema.')
				time.sleep(5)
				sys.exit()
			else:
				print('repsosta não válida, tente novamente.')
				time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')
print('Entrada bem sucedida!')
