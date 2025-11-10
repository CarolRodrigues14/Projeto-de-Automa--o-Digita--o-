# 🏭 Protótipo de Automação Digital — Empresa Fictícia *PeçaCerta*

## 📋 Sobre o Projeto

Este protótipo foi desenvolvido para a **empresa fictícia PeçaCerta**, com o objetivo de demonstrar uma solução de **automação digital aplicada ao controle de produção e qualidade** de peças em linhas de montagem industriais.

O sistema automatiza a inspeção que antes era feita manualmente — eliminando atrasos, falhas humanas e altos custos operacionais.

---

## 🎯 Problema Resolvido

As indústrias enfrentam desafios no controle de qualidade manual:

- ⏱️ Atrasos na inspeção  
- ❌ Falhas humanas na conferência  
- 💰 Alto custo operacional  
- 📊 Dificuldade em gerar relatórios consolidados  

---

## ✨ Funcionalidades

O protótipo oferece:

1. **📦 Cadastro de Peças** – Registro de peças com ID, peso, cor e comprimento  
2. **✅ Avaliação Automática** – Classificação de peças conforme critérios definidos  
3. **📋 Listagem de Peças** – Visualização das aprovadas e reprovadas  
4. **🗑️ Remoção de Peças** – Exclusão de registros pelo ID  
5. **📦 Gestão de Caixas** – Armazenamento automático em caixas de 10 unidades  
6. **📊 Relatórios Detalhados** – Estatísticas completas de produção e qualidade  

---

## ⚙️ Critérios de Qualidade

Uma peça é **aprovada** quando atende simultaneamente aos seguintes critérios:

| Critério | Valor Aceitável |
|----------|----------------|
| **Peso** | 95g a 105g |
| **Cor** | Azul ou Verde |
| **Comprimento** | 10cm a 20cm |

Qualquer desvio resulta em **reprovação**, com motivo detalhado.

---

## 🚀 Como Executar

### 🧩 Pré-requisitos

- Python 3.10 ou superior  
- Terminal/Prompt de Comando  

### ▶️ Passo a Passo

```bash
git clone https://github.com/CarolRodrigues14/Projeto-de-Automa--o-Digita--o-
cd gestao_qualidade.py

Depois, navegue pelo menu interativo (opções 0 a 5).

💻 Exemplos de Uso
Exemplo 1 – Cadastro de Peça Aprovada

📦 CADASTRO DE NOVA PEÇA
Digite o peso da peça (em gramas): 100
Digite o comprimento da peça (em cm): 15
Digite a cor da peça (azul ou verde): azul

✅ Peça #1 APROVADA e armazenada na caixa atual.
   Ocupação da caixa: 1/10

Exemplo 2 – Cadastro de Peça Reprovada

📦 CADASTRO DE NOVA PEÇA
Digite o peso da peça (em gramas): 110
Digite o comprimento da peça (em cm): 12
Digite a cor da peça (azul ou verde): vermelho

❌ Peça #2 REPROVADA
   Motivo: Peso fora do padrão (95-105g) | Cor inválida (aceitas: azul, verde)

Exemplo 3 – Fechamento Automático de Caixa

✅ Peça #10 APROVADA e armazenada na caixa atual.
   Ocupação da caixa: 10/10

🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁
Caixa #1 fechada com 10 peças!
🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁

Exemplo 4 – Relatório Final

📊 RELATÓRIO FINAL DE PRODUÇÃO

RESUMO GERAL DA PRODUÇÃO
──────────────────────────────────────────────────
Total de peças processadas: 25
Peças aprovadas: 20 (80.0%)
Peças reprovadas: 5 (20.0%)

ARMAZENAMENTO
──────────────────────────────────────────────────
Caixas fechadas: 2
Peças na caixa atual: 0/10

ANÁLISE DE REJEIÇÕES
──────────────────────────────────────────────────
• Peso fora do padrão (95-105g): 3 peça(s)
• Cor inválida (aceitas: azul, verde): 2 peça(s)

ESTATÍSTICAS DE PEÇAS APROVADAS
──────────────────────────────────────────────────
Peso médio: 99.85g
Comprimento médio: 14.32cm
Distribuição de cores:
  • Azul: 12 peça(s)
  • Verde: 8 peça(s)

🏗️ Estrutura do Código

sistema.py
├── Importações e Configurações
├── Constantes de Qualidade
├── Variáveis Globais
├── Funções Utilitárias
│   ├── limpa_tela()
│   └── exibir_cabecalho()
├── Funções de Negócio
│   ├── avaliar_peca()
│   ├── fechar_caixa_atual()
│   ├── cadastrar_peca()
│   ├── listar_pecas()
│   ├── remover_peca()
│   ├── listar_caixas()
│   └── gerar_relatorio()
└── Função Principal
    └── main()

🧠 Lógica e Boas Práticas

🧱 Estruturas de Dados

   Listas: Armazenamento de peças e caixas

   Dicionários: Representação de cada peça

   Tuplas: Retorno de múltiplos valores (status, motivo)

🔁 Estruturas de Controle

   Condicionais (if/elif/else): Validação de critérios

   Laços (for): Iteração sobre listas

   Match/Case: Menu interativo moderno (Python 3.10+)

🧩 Funções e Organização

   Modularização: Cada função tem uma tarefa específica

   Type Hints: Facilita leitura e manutenção

   Docstrings: Documentação inline de cada função

💡 Boas Práticas

   ✅ Constantes centralizadas

   ✅ Validação de entrada e tratamento de exceções

   ✅ Cores ANSI para feedback visual

   ✅ Interface limpa e intuitiva

🎨 Melhorias Implementadas (Versão 2.0)
💻 Interface

🎨 Emojis para visualização agradável

📊 Estatísticas detalhadas no relatório

🎯 Feedback visual aprimorado

⚙️ Funcionalidades

📈 Percentuais de aprovação e reprovação

📏 Médias de peso e comprimento

🔍 Análise de motivos de rejeição

ℹ️ Exibição da caixa em andamento

🧱 Código

🏗️ Type hints

🔧 Constantes organizadas

📝 Função main()

✅ Validação de valores positivos

🎯 Melhor formatação de saídas

🔮 Possíveis Expansões Futuras
🏭 Integração Industrial

🔌 Conexão com sensores IoT

📡 API REST para integração com outros sistemas

💾 Banco de dados para persistência

🤖 Inteligência Artificial

📊 Análise preditiva de qualidade

🎯 Machine Learning para previsão de defeitos

🖥️ Interface Gráfica

🌐 Dashboard web em tempo real

📱 Aplicativo mobile para gestores

📈 Gráficos interativos

⚙️ Automação Avançada

🏗️ Controle de múltiplas linhas

📦 Integração com estoque

🚚 Rastreamento até expedição

👩‍💻 Autora

Caroline Rodrigues
Graduanda em Inteligência Artificial e Automação Digital
UniFECAF + Rocketseat

📚 Disciplina

Algoritmos e Lógica de Programação
