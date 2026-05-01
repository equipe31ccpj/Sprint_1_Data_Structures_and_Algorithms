import os

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

if escolha_usuario == 1:
	print(1)
else:
	print(2)		
