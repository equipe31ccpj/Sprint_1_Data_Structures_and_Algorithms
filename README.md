# Sistema HCA G2 — Smart Charging Simulator 🔋🚗

O **HCA G2** é uma aplicação em Python voltada para a simulação, monitoramento e bilhetagem inteligente de estações de carregamento para veículos elétricos (VE). O ecossistema simula o comportamento elétrico e térmico de uma recarga residencial/comercial em tempo real, integrando autenticação e cálculo de **tarifa dinâmica** baseado em faixas de fluxo da rede e incentivos de geração de energia solar microgerada.

---

## 🚀 Funcionalidades Principais

*   **Módulo de Autenticação Interativo:** Login seguro e criação de novas contas diretamente pelo terminal com validações nativas para tratamento de erros (impede falhas caso o usuário digite texto em campos numéricos).
*   **Telemetria Dinâmica de Recarga:** Simulação contínua e realista segundo a segundo de grandezas físicas:
    *   Tensão alternada ($200\text{V}$ a $220\text{V}$) com flutuações de ruído na rede.
    *   Corrente elétrica adaptada à integridade da tensão (até $40\text{A}$).
    *   Cálculo em tempo real de Potência Ativa ($\text{kW}$) e energia acumulada ($\text{kWh}$).
*   **Proteção Ativa e Segurança Elétrica:** Monitoramento térmico indireto e proteção de sobrecorrente/sobrecarga. O sistema interrompe o fornecimento e aciona um bloqueio de segurança caso a potência real ultrapasse a barreira crítica de $8.8\text{kW}$.
*   **Algoritmo de Tarifa Inteligente:** Sistema adaptativo de cobrança indexado pelo dia da semana e hora de início do carregamento:
    *   Separação automatizada em fluxos: `BAIXA`, `REGULAR`, `MEDIANO` e `PICO`.
    *   **Incentivo Solar GoodWe:** Identificação da janela de pico de geração solar das 10h às 14h, aplicando descontos exclusivos no multiplicador de preço por kWh.

---

## 🛠️ Arquitetura de Dados Local

O script opera 100% com módulos padrão do ecossistema Python (sem dependências externas), mas necessita obrigatoriamente de uma base relacional local em formato JSON chamada `veiculos.json` alocada no mesmo diretório de execução.

### Formato esperado para o `veiculos.json`:
```json
[
  {
    "marca": "BYD",
    "modelo": "Dolphin Plus",
    "capacidade_bateria_kwh": 60.48
  },
  {
    "marca": "GWM",
    "modelo": "Ora 03 GT",
    "capacidade_bateria_kwh": 63.0
  },
  {
    "marca": "Volvo",
    "modelo": "EX30",
    "capacidade_bateria_kwh": 69.0
  }
]

| Categoria de Fluxo | Janela Horária Comum            | Fator Padrão | Fator c/ Incentivo Solar (10h - 14h) |
| **BAIXA**          | Madrugadas / Início da Manhã    | 0.90         | 0.70                                 |
| **REGULAR**        | Horários intermediários         | 1.00         | 0.85                                 |
| **MEDIANO**        | Transições de fluxo comercial   | 1.00         | 0.85                                 |
| **PICO**           | Horários de retorno residencial | 1.40         | 1.25                                 |

💻 Como Rodar o Projeto
Siga as etapas abaixo no terminal do seu sistema operacional:

Clone ou salve o arquivo do projeto: Certifique-se de que o script Python e o arquivo veiculos.json estejam na mesma pasta.

Abra o terminal na raiz desta pasta instalada.

Execute a aplicação utilizando o interpretador do Python 3:

python nome_do_seu_script.py

4. **Credenciais de Teste Padrão:**
   * **E-mail:** `p@email`
   * **Senha:** `123`

---

## 📊 Exemplo de Saída (Relatório Final)

```text
========== RELATÓRIO FINAL ==========
Veículo Detectado:      BYD Dolphin Plus
Status de carregamento: 100.0%
Hora de entrada:         19/05/2026 11:15:23
Hora de saída:          19/05/2026 11:16:05
Faixa de Fluxo da Rede: REGULAR (Incentivo Solar GoodWe: Ativo)
Energia Consumida:      23.14 kWh
Preço do kWh no momento: R$ 1.28
Custo total da recarga: R$ 29.62
=====================================