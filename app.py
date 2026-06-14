import os
import sys
import time as tm
import random
import json
from datetime import datetime, time, timedelta

usuarios = [{'email': 'p@email', 'senha': '123'}]

os.system('cls' if os.name == 'nt' else 'clear')
print('Iniciando Sistema HCA G2...')

print('\n' + ('=~' * 20))
print('1 - Já possuo uma conta.')
print('2 - Criar conta.')
try:
	escolha_usuario = int(input('Escolha a opção: '))
except ValueError:
	print('Entrada inválida! Digite 1 ou 2.')
	sys.exit()

while escolha_usuario not in [1, 2]:
	print('Opção inválida!')
	input('Digite qualquer tecla para continuar: ')
	os.system('cls' if os.name == 'nt' else 'clear')
	print('=~' * 20)
	print('1 - Já possuo uma conta.')
	print('2 - Criar conta')
	try:
		escolha_usuario = int(input('Escolha a opção: '))
	except ValueError:
		print('Entrada inválida! Digite 1 ou 2.')
		sys.exit()

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
			criar_senha = input('Digite a senha: ')
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

tm.sleep(5)


def obter_tipo_fluxo(dia_semana, hora_atual):
	if dia_semana < 5:
		if (hora_atual >= time(22, 0) or hora_atual < time(7, 0)) or (time(9, 0) <= hora_atual < time(11, 0)): return "BAIXA"
		elif (time(7, 0) <= hora_atual < time(9, 0)) or (time(14, 0) <= hora_atual < time(17, 0)): return "MEDIANO"
		elif (time(12, 0) <= hora_atual < time(14, 0)) or (time(17, 0) <= hora_atual < time(21, 0)): return "PICO"
		else: return "REGULAR"
	else:
		if (hora_atual >= time(22, 0) or hora_atual < time(9, 0)): return "BAIXA"
		elif (time(9, 0) <= hora_atual < time(13, 0)) or (time(20, 0) <= hora_atual < time(22, 0)): return "MEDIANO"
		elif (time(14, 0) <= hora_atual < time(20, 0)): return "PICO"
		else: return "REGULAR"

def calcular_tarifa_inteligente(data_hora, preco_base_kwh=1.50):
	dia_semana = data_hora.weekday()
	hora_atual = data_hora.time()
	fluxo = obter_tipo_fluxo(dia_semana, hora_atual)
	is_janela_goodwe = time(10, 0) <= hora_atual <= time(14, 0)
	if fluxo == "PICO": fator = 1.25 if is_janela_goodwe else 1.40
	elif fluxo == "MEDIANO": fator = 0.85 if is_janela_goodwe else 1.00
	elif fluxo == "BAIXA": fator = 0.70 if is_janela_goodwe else 0.90
	else: fator = 0.85 if is_janela_goodwe else 1.00
	return {"fluxo": fluxo, "geracao_solar": is_janela_goodwe, "preco_final_kwh": round(preco_base_kwh * fator, 2)}


class SessaoRecarga:
	def __init__(self, id_sessao, veiculo, bateria_inicial):
		self.id_sessao = id_sessao
		self.marca = veiculo['marca']
		self.modelo = veiculo['modelo']
		self.capacidade = veiculo['capacidade_bateria_kwh']
		self.bateria_atual = float(bateria_inicial)
		self.energia_injetada = 0.0
		self.status = "Carregando"
		self.ultima_atualizacao = datetime.now() 

	def atualizar_acumulado(self, potencia_limite):
		if self.status != "Carregando":
			return

		agora = datetime.now()
		segundos_passados = (agora - self.ultima_atualizacao).total_seconds()
		self.ultima_atualizacao = agora

		if segundos_passados <= 0:
			return

		for _ in range(int(segundos_passados)):
			if self.bateria_atual >= 100.0:
				self.status = "Concluído"
				break

			tensao = random.uniform(212, 220) if random.random() < 0.95 else random.uniform(200, 211)
			corrente = random.uniform(31.5, 32.5) if tensao >= 212 else random.uniform(32.6, 40.0)
			potencia_kw = min((tensao * corrente) / 1000, potencia_limite)

			energia_ganha = potencia_kw / 3600
			self.energia_injetada += energia_ganha
			self.bateria_atual = min(100.0, self.bateria_atual + ((energia_ganha / self.capacidade) * 100))

class GerenciadorEstacoes:
	def __init__(self, potencia_maxima_rede=40.0):
		self.sessoes = {}
		self.potencia_maxima_rede = potencia_maxima_rede
		self.contador_ids = 1
		with open('veiculos.json', 'r', encoding='utf-8') as arquivo:
			self.lista_veiculos = json.load(arquivo)

	def adicionar_veiculo(self):
		veiculo = random.choice(self.lista_veiculos)
		bateria_init = random.randint(15, 70)
		nova_sessao = SessaoRecarga(self.contador_ids, veiculo, bateria_init)
		self.sessoes[self.contador_ids] = nova_sessao
		print(f"\n🚗 {nova_sessao.marca} {nova_sessao.modelo} conectado na Vaga #{self.contador_ids}!")
		self.contador_ids += 1

	def atualizar_todas_as_sessoes(self):
		sessoes_ativas = [s for s in self.sessoes.values() if s.status == "Carregando"]
		if not sessoes_ativas: return
		potencia_por_carro = self.potencia_maxima_rede / len(sessoes_ativas)
		for sessao in self.sessoes.values():
			sessao.atualizar_acumulado(potencia_por_carro)

	def monitorar_tempo_real(self):
		"""CRITÉRIO 6: Visualização dinâmica em tempo real com opção de voltar"""
		try:
			while True:
				os.system('cls' if os.name == 'nt' else 'clear')
				self.atualizar_todas_as_sessoes() 
				
				sessoes_ativas = [s for s in self.sessoes.values() if s.status == "Carregando"]
				potencia_vaga = self.potencia_maxima_rede / max(len(sessoes_ativas), 1)

				print("=== 🔋 MONITORAMENTO EM TEMPO REAL (Pressione Ctrl+C para Voltar) ===")
				if not self.sessoes:
					print("\nNenhum veículo carregando no momento.")
				
				for id_s, s in self.sessoes.items():
					if s.status == "Carregando":
						energia_restante = ((100 - s.bateria_atual) / 100) * s.capacity if hasattr(s, 'capacity') else ((100 - s.bateria_atual) / 100) * s.capacidade
						tempo_restante_horas = energia_restante / potencia_vaga
						tempo_str = f"{int(tempo_restante_horas * 60)} min restantes"
					else:
						tempo_str = "Pronto!"

					barra = "█" * int(s.bateria_atual / 10) + "-" * (10 - int(s.bateria_atual / 10))
					print(f"\nVaga #{id_s}: {s.marca} {s.modelo}")
					print(f"  [{barra}] {s.bateria_atual:.1f}% | Status: {s.status} | Est: {tempo_str}")
				
				tm.sleep(1) 
		except KeyboardInterrupt:
			print("\nRetornando ao menu principal...")
			tm.sleep(1)

	def enviar_log_ocpp(self, tipo_mensagem, payload):
		mensagem = {
				"Protocol": "OCPP-J 1.6",
				"MessageType": "CALL",
				"Action": tipo_mensagem,
				"Timestamp": datetime.now().isoformat(),
				"Payload": payload
		}
		print(f"\n⚡ [OCPP OUT] {json.dumps(mensagem, ensure_ascii=False, indent=2)}")
		print("🔌 [OCPP IN] Confirmação recebida: [3, \"SUCCESS\"]")

	def pagar_e_liberar_vaga(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.atualizar_todas_as_sessoes() 
		sessoes_ativas = [id_s for id_s, s in self.sessoes.items() if s.status in ["Carregando", "Concluído"]]
		
		if not sessoes_ativas:
			print("\n❌ Não há nenhum veículo ocupando as vagas no momento.")
			input("\nPressione Enter para voltar...")
			return

		print("=== 💳 PAGAMENTO E LIBERAÇÃO DE VAGA ===")
		for id_s in sessoes_ativas:
			s = self.sessoes[id_s]
			print(f"Vaga #{id_s}: {s.marca} {s.modelo} | Bateria: {s.bateria_atual:.1f}% | Status: {s.status}")
		
		try:
			vaga_escolhida = int(input("\nDigite o número da vaga que deseja liberar e pagar: "))
		except ValueError:
			print("Entrada inválida!")
			input("\nPressione Enter para voltar...")
			return

		if vaga_escolhida not in self.sessoes or self.sessoes[vaga_escolhida].status == "Liberado e Pago":
			print("❌ Vaga inválida ou já liberada!")
			input("\nPressione Enter para voltar...")
			return

		sessao = self.sessoes[vaga_escolhida]
		
		dados_tarifa = calcular_tarifa_inteligente(datetime.now())
		preco_kwh = dados_tarifa['preco_final_kwh']
		custo_total = sessao.energia_injetada * preco_kwh

		os.system('cls' if os.name == 'nt' else 'clear')
		print('='*15 + ' RECIBO DE PAGAMENTO ' + '='*15)
		print(f"Veículo:          {sessao.marca} {sessao.modelo}")
		print(f"Energia Injetada: {sessao.energia_injetada:.2f} kWh")
		print(f"Tarifa Aplicada:  R$ {preco_kwh:.2f}/kWh ({dados_tarifa['fluxo']})")
		print(f"Total a Pagar:    R$ {custo_total:.2f}")
		print('=' * 51)
		
		confirmar = input("\nConfirmar pagamento? (sim/não): ")
		if confirmar.lower() == 'sim':
			if hasattr(self, 'enviar_log_ocpp'):
				self.enviar_log_ocpp("StopTransaction", {
					"transactionId": sessao.id_sessao,
					"meterStop": round(sessao.energia_injetada, 2),
					"reason": "LocalDisconnect"
				})
			del self.sessoes[vaga_escolhida] 
			
			print(f"\n✅ Pagamento processado! Vaga #{vaga_escolhida} está LIVRE e desocupada.")
		else:
			print("\n❌ Operação cancelada.")

	def gerar_relatorio_financeiro(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		self.atualizar_todas_as_sessoes()
		print('='*15 + ' RELATÓRIO FINAL E EMISSÃO DE NOTA ' + '='*15)
		for id_s, s in self.sessoes.items():
			tarifa = calcular_tarifa_inteligente(datetime.now())['preco_final_kwh']
			print(f"\n[Vaga #{id_s}] {s.marca} {s.modelo} -> Consumo: {s.energia_injetada:.2f} kWh | Total: R$ {s.energia_injetada * tarifa:.2f}")
		input("\nPressione Enter para continuar...")

os.system('cls' if os.name == 'nt' else 'clear')
print("🔑 Login efetuado automaticamente para simulação.")
gerenciador = GerenciadorEstacoes(potencia_maxima_rede=40.0)

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("="*15 + " PANEL CONTROL HCA G2 " + "="*15)
	print("1. Conectar/Simular Entrada de Carro")
	print("2. Ver Carregamento em Tempo Real (Monitoramento)")
	print("3. Pagar e Liberar Vaga (Checkout)")
	print("4. Emitir Relatório Geral de Faturamento")
	print("5. Sair do Sistema")
	print("="*52)
	
	opcao = input("Escolha a opção: ")
	if opcao == "1":
		gerenciador.adicionar_veiculo()
		input("\nPressione Enter para voltar ao menu...")
	elif opcao == "2":
		gerenciador.monitorar_tempo_real()
	elif opcao == "3":
		gerenciador.pagar_e_liberar_vaga()
	elif opcao == "4":
		gerenciador.gerar_relatorio_financeiro()
	elif opcao == "5":
		print("Encerrando aplicação...")
		break
	else:
		print("Opção inválida! Escolha de 1 a 5.")
		tm.sleep(1)