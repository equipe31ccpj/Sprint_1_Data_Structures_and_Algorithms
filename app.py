import os
import sys
import time as tm
import random
import json
from datetime import datetime, time, timedelta

usuarios = [
    {
        'email': 'p@email', 
        'senha': '123', 
        'endereço': 'rua 123', 
        'número de série': '456', 
        'código de verificação': '789', 
        'tipo de estação': 'Vaeículo'
    }
]


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
	usuario['senha'] = criar_senha
	usuario['endereço'] = endereco
	usuario['número de série'] = num_serie
	usuario['código de verificação'] = cod_verificacao
	usuario['tipo de estação'] = tipo_estacao
	usuarios.append(usuario)
	print('Conta criada com sucesso!')
	tm.sleep(5)	
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
			novamente = input('e-mail ou senha incorretas! Deseja tentar novamente(sim, não): ')
			if novamente.lower() == 'sim':
				break
			elif novamente.lower() == 'não':
				print('Saindo do sistema.')
				tm.sleep(5)
				sys.exit()
			else:
				print('repsosta não válida, tente novamente.')
				tm.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')
print('Entrada bem sucedida!')

print('Conecte o carregador no dispositivo!')
tm.sleep(5)

print('Estabelecendo conexão com dispositivo!')
with open('veiculos.json', 'r', encoding='utf-8') as arquivo:
    lista_veiculos = json.load(arquivo)
tm.sleep(1)
print('Conexão realizada')

veiculo = random.choice(lista_veiculos)

bateria_atual = random.randint(10, 80)
marca = veiculo['marca']
modelo = veiculo['modelo']
capacidade = veiculo['capacidade_bateria_kwh']

print(f"[DADOS DETECTADOS] {marca} {modelo} | Bateria Atual: {bateria_atual}%")

porcentagem_faltante = 100 - bateria_atual
energia_necessaria = (porcentagem_faltante / 100) * capacidade

potencia_carregador = 22
tempo_estimado_horas = energia_necessaria / potencia_carregador

print(f'Tempo estimado em horas: {tempo_estimado_horas:.2f}')


energia_realmente_injetada = 0
segundos_decorridos = 0
while bateria_atual < 100:
	tm.sleep(1)
	segundos_decorridos += 1
	if random.random() < 0.95:
		tensao = random.uniform(212, 220)
		tensao_normal = True
	else:
		tensao = random.uniform(200, 211)
		tensao_normal = False

	if not tensao_normal:
		corrente = random.uniform(32.6, 40.0)
	else:
		corrente = random.uniform(31.5, 32.5)

	potencia_real_w = tensao * corrente
	potencia_real_kw = potencia_real_w / 1000

	if potencia_real_kw > 8.8:
		print('Sobrecarga no sistema! Carregamento interrompido para manutenção.')
		tm.sleep(5)
		break
	else:
		pass

	if potencia_real_kw > 7.15:
		temperatura = random.uniform(70.0, 95.0)
	else:
		temperatura = random.uniform(30.0, 45.0)

	energia_ganha_kwh = potencia_real_kw / 3600
	energia_realmente_injetada += energia_ganha_kwh
	porcentagem_ganha = (energia_ganha_kwh / capacidade) * 100
	bateria_atual += porcentagem_ganha

	if bateria_atual > 100.0:
		bateria_atual = 100.0
	
print('Carregamento concluido')


def obter_tipo_fluxo(dia_semana, hora_atual):
    if dia_semana < 5:
        if (time(22, 0) <= hora_atual or hora_atual < time(7, 0)) or (time(9, 0) <= hora_atual < time(11, 0)):
            return "BAIXA"
        elif (time(7, 0) <= hora_atual < time(9, 0)) or (time(14, 0) <= hora_atual < time(17, 0)):
            return "MEDIANO"
        elif (time(12, 0) <= hora_atual < time(14, 0)) or (time(17, 0) <= hora_atual < time(21, 0)):
            return "PICO"
        else:
            return "REGULAR"

    else:
        if (time(22, 0) <= hora_atual or hora_atual < time(9, 0)):
            return "BAIXA"
        elif (time(9, 0) <= hora_atual < time(13, 0)) or (time(20, 0) <= hora_atual < time(22, 0)):
            return "MEDIANO"
        elif (time(14, 0) <= hora_atual < time(20, 0)):
            return "PICO"
        else:
            return "REGULAR"


def calcular_tarifa_inteligente(data_hora, preco_base_kwh):
    dia_semana = data_hora.weekday()
    hora_atual = data_hora.time()
    
    fluxo = obter_tipo_fluxo(dia_semana, hora_atual)
    is_janela_goodwe = time(10, 0) <= hora_atual <= time(14, 0)

    if fluxo == "PICO":
        fator = 1.25 if is_janela_goodwe else 1.40
        
    elif fluxo == "MEDIANO":
        fator = 0.85 if is_janela_goodwe else 1.00
        
    elif fluxo == "BAIXA":
        fator = 0.70 if is_janela_goodwe else 0.90
        
    else:
        fator = 0.85 if is_janela_goodwe else 1.00

    preco_final = preco_base_kwh * fator
	
    return {
		"fluxo": fluxo,
		"geracao_solar": is_janela_goodwe,
		"fator_multiplicador": fator,
		"preco_final_kwh": round(preco_final, 2)
	}

preco_base = 1.50  
    
data_ancora = datetime(2026, 5, 18, 0, 0)
dias_aleatorios = random.randint(0, 6)      
minutos_aleatorios = random.randint(0, 1439)

data_randomica = data_ancora + timedelta(days=dias_aleatorios, minutes=minutos_aleatorios)

hora_inicio = data_ancora + timedelta(days=dias_aleatorios, minutes=minutos_aleatorios)
hora_saida = hora_inicio + timedelta(seconds=segundos_decorridos)
    

valor_por_kwh = calcular_tarifa_inteligente(hora_inicio, preco_base)
preco_kwh_momento = valor_por_kwh['preco_final_kwh']

custo_total = energia_realmente_injetada * preco_kwh_momento	

print('\n\n' + '='*10 + ' RELATÓRIO FINAL ' + '='*10)
print(f'Veículo Detectado:      {marca} {modelo}')
print(f'Status de carregamento: {bateria_atual:.1f}%')
print(f'Hora de entrada:         {hora_inicio.strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Hora de saída:          {hora_saida.strftime("%d/%m/%Y %H:%M:%S")}')
print(f'Faixa de Fluxo da Rede: {valor_por_kwh["fluxo"]} (Incentivo Solar GoodWe: {"Ativo" if valor_por_kwh["geracao_solar"] else "Inativo"})')
print(f'Energia Consumida:      {energia_realmente_injetada:.2f} kWh')
print(f'Preço do kWh no momento: R$ {preco_kwh_momento:.2f}')
print(f'Custo total da recarga: R$ {custo_total:.2f}')
print('=' * 37)