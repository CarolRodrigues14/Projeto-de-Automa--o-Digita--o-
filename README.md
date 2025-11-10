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
git clone https://github.com/seu-usuario/prototipo-automacao-pecacerta.git
cd prototipo-automacao-pecacerta
python sistema.py
