# ===============================================================
#   Sistema de Automação Digital
# ===============================================================
#   Desenvolvido por: Caroline Rodrigues
#   Disciplina: Algoritmos e Lógica de Programação
#   Curso: Graduação Tecnológica em Inteligência Artificial 
#          e Automação Digital – UniFECAF + Rocketseat
#   Data: Outubro/2025
# ---------------------------------------------------------------
#   Descrição:
#   Solução de automação digital que auxilia no controle de produção 
#   e qualidade das peças fabricadas em uma linha de montagem.
#
#   O sistema é capaz de:
#   • Receber os dados de cada peça produzida (ID, peso, cor e comprimento);
#   • Avaliar automaticamente se a peça está aprovada ou reprovada, 
#     de acordo com critérios de qualidade pré-definidos:
#       - Peso entre 95g e 105g
#       - Cor azul ou verde
#       - Comprimento entre 10cm e 20cm
#   • Armazenar as peças aprovadas em caixas de capacidade limitada 
#     (10 peças por caixa);
#   • Fechar a caixa quando atingir a capacidade máxima e iniciar uma nova;
#   • Gerar relatórios consolidados com:
#       - Total de peças aprovadas
#       - Total de peças reprovadas e o motivo da reprovação
#       - Quantidade de caixas utilizadas
# ===============================================================

import os
from typing import Dict, List, Tuple

# ---------------------------------------------------------------
#   Códigos ANSI para colorir texto no terminal
# ---------------------------------------------------------------
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
RESET = "\033[0m"

# ---------------------------------------------------------------
#   Constantes de Qualidade
# ---------------------------------------------------------------
PESO_MIN = 95
PESO_MAX = 105
CORES_VALIDAS = ("azul", "verde")
COMP_MIN = 10
COMP_MAX = 20
CAPACIDADE_CAIXA = 10

# ---------------------------------------------------------------
#   Variáveis globais
# ---------------------------------------------------------------
pecas_aprovadas: List[Dict] = []
pecas_reprovadas: List[Dict] = []
caixas_fechadas: List[List[Dict]] = []
caixa_atual: List[Dict] = []
id_atual = 1


# ---------------------------------------------------------------
def limpa_tela() -> None:
    """Limpa o terminal (Windows ou Linux)."""
    os.system('cls' if os.name == 'nt' else 'clear')


# ---------------------------------------------------------------
def exibir_cabecalho(titulo: str) -> None:
    """Exibe um cabeçalho formatado."""
    limpa_tela()
    print(f"{AZUL}{'=' * 50}{RESET}")
    print(f"{AZUL}{titulo.center(50)}{RESET}")
    print(f"{AZUL}{'=' * 50}{RESET}\n")


# ---------------------------------------------------------------
def avaliar_peca(peso: float, cor: str, comprimento: float) -> Tuple[str, str]:
    """
    Avalia se a peça está aprovada ou reprovada conforme os critérios de qualidade.
    
    Args:
        peso: Peso da peça em gramas
        cor: Cor da peça (azul ou verde)
        comprimento: Comprimento da peça em cm
    
    Returns:
        Tupla (status, motivo) onde status é "Aprovada" ou "Reprovada"
    """
    motivos = []
    
    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"Peso fora do padrão ({PESO_MIN}-{PESO_MAX}g)")
    
    if cor not in CORES_VALIDAS:
        motivos.append(f"Cor inválida (aceitas: {', '.join(CORES_VALIDAS)})")
    
    if not (COMP_MIN <= comprimento <= COMP_MAX):
        motivos.append(f"Comprimento fora do padrão ({COMP_MIN}-{COMP_MAX}cm)")
    
    if motivos:
        return "Reprovada", " | ".join(motivos)
    
    return "Aprovada", ""


# ---------------------------------------------------------------
def fechar_caixa_atual() -> None:
    """Fecha a caixa atual e inicia uma nova."""
    global caixa_atual, caixas_fechadas
    
    if caixa_atual:
        caixas_fechadas.append(caixa_atual.copy())
        print(f"\n{AMARELO}{'🎁' * 25}{RESET}")
        print(f"{AMARELO}Caixa #{len(caixas_fechadas)} fechada com {len(caixa_atual)} peças!{RESET}")
        print(f"{AMARELO}{'🎁' * 25}{RESET}")
        caixa_atual.clear()


# ---------------------------------------------------------------
def cadastrar_peca() -> None:
    """Recebe os dados da peça, avalia e armazena nas listas correspondentes."""
    global id_atual, caixa_atual
    
    exibir_cabecalho("📦 CADASTRO DE NOVA PEÇA")

    # Coleta e validação de dados numéricos
    try:
        peso = float(input(f"{CIANO}Digite o peso da peça (em gramas): {RESET}"))
        if peso <= 0:
            raise ValueError("Peso deve ser positivo")
            
        comprimento = float(input(f"{CIANO}Digite o comprimento da peça (em cm): {RESET}"))
        if comprimento <= 0:
            raise ValueError("Comprimento deve ser positivo")
            
    except ValueError as e:
        print(f"\n{VERMELHO}❌ Erro: {e}. Digite apenas números válidos e positivos.{RESET}")
        input("\nPressione Enter para voltar ao menu...")
        return

    # Validação da cor
    cor = input(f"{CIANO}Digite a cor da peça (azul ou verde): {RESET}").strip().lower()

    # Avaliação da peça
    status, motivo = avaliar_peca(peso, cor, comprimento)

    peca = {
        "ID": id_atual,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": status,
        "motivo": motivo
    }

    # Armazenamento conforme o status
    print(f"\n{'-' * 50}")
    if status == "Aprovada":
        pecas_aprovadas.append(peca)
        caixa_atual.append(peca)
        print(f"{VERDE}✅ Peça #{id_atual} APROVADA e armazenada na caixa atual.{RESET}")
        print(f"{VERDE}   Ocupação da caixa: {len(caixa_atual)}/{CAPACIDADE_CAIXA}{RESET}")

        # Verifica se a caixa está cheia
        if len(caixa_atual) == CAPACIDADE_CAIXA:
            fechar_caixa_atual()
    else:
        pecas_reprovadas.append(peca)
        print(f"{VERMELHO}❌ Peça #{id_atual} REPROVADA{RESET}")
        print(f"{VERMELHO}   Motivo: {motivo}{RESET}")

    print(f"{'-' * 50}")
    id_atual += 1
    input("\nPressione Enter para voltar ao menu...")


# ---------------------------------------------------------------
def listar_pecas() -> None:
    """Exibe todas as peças cadastradas, aprovadas e reprovadas."""
    exibir_cabecalho("📋 LISTA DE PEÇAS CADASTRADAS")

    if not pecas_aprovadas and not pecas_reprovadas:
        print(f"{AMARELO}⚠️  Nenhuma peça cadastrada ainda.{RESET}")
    else:
        # Peças Aprovadas
        print(f"{VERDE}✅ PEÇAS APROVADAS ({len(pecas_aprovadas)}):{RESET}")
        print(f"{'-' * 80}")
        if pecas_aprovadas:
            for p in pecas_aprovadas:
                print(f"ID: {p['ID']:3d} | Peso: {p['peso']:6.2f}g | "
                      f"Cor: {p['cor']:6s} | Comprimento: {p['comprimento']:5.2f}cm")
        else:
            print(f"{AMARELO}   Nenhuma peça aprovada ainda.{RESET}")

        # Peças Reprovadas
        print(f"\n{VERMELHO}❌ PEÇAS REPROVADAS ({len(pecas_reprovadas)}):{RESET}")
        print(f"{'-' * 80}")
        if pecas_reprovadas:
            for p in pecas_reprovadas:
                print(f"ID: {p['ID']:3d} | Peso: {p['peso']:6.2f}g | "
                      f"Cor: {p['cor']:6s} | Comprimento: {p['comprimento']:5.2f}cm")
                print(f"          Motivo: {p['motivo']}")
        else:
            print(f"{VERDE}   Nenhuma peça reprovada! Excelente qualidade!{RESET}")

    input("\nPressione Enter para voltar ao menu...")


# ---------------------------------------------------------------
def remover_peca() -> None:
    """Permite remover uma peça pelo ID."""
    global pecas_aprovadas, pecas_reprovadas, caixa_atual

    exibir_cabecalho("🗑️  REMOÇÃO DE PEÇA")

    if not pecas_aprovadas and not pecas_reprovadas:
        print(f"{AMARELO}⚠️  Nenhuma peça cadastrada para remover.{RESET}")
        input("\nPressione Enter para voltar ao menu...")
        return

    try:
        id_remover = int(input(f"{CIANO}Digite o ID da peça que deseja remover: {RESET}"))
    except ValueError:
        print(f"\n{VERMELHO}❌ ID inválido. Digite apenas números.{RESET}")
        input("\nPressione Enter para voltar ao menu...")
        return

    # Remove de todas as listas onde estiver
    removida = False
    peca_removida = None
    
    for lista in [pecas_aprovadas, pecas_reprovadas, caixa_atual]:
        for peca in lista:
            if peca["ID"] == id_remover:
                peca_removida = peca
                lista.remove(peca)
                removida = True
                break
        if removida:
            break

    if removida:
        print(f"\n{VERDE}✅ Peça #{id_remover} removida com sucesso!{RESET}")
        print(f"   Status: {peca_removida['status']}")
    else:
        print(f"\n{AMARELO}⚠️  Nenhuma peça encontrada com o ID {id_remover}.{RESET}")

    input("\nPressione Enter para voltar ao menu...")


# ---------------------------------------------------------------
def listar_caixas() -> None:
    """Exibe todas as caixas fechadas."""
    exibir_cabecalho("📦 CAIXAS FECHADAS")

    if not caixas_fechadas:
        print(f"{AMARELO}⚠️  Nenhuma caixa foi fechada ainda.{RESET}")
        if caixa_atual:
            print(f"\n{CIANO}ℹ️  Caixa atual em andamento: {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças{RESET}")
    else:
        for i, caixa in enumerate(caixas_fechadas, start=1):
            print(f"\n{AZUL}📦 Caixa #{i} ({len(caixa)} peças){RESET}")
            print(f"{'-' * 80}")
            for p in caixa:
                print(f"  ID: {p['ID']:3d} | Cor: {p['cor']:6s} | "
                      f"Peso: {p['peso']:6.2f}g | Comp: {p['comprimento']:5.2f}cm")
        
        if caixa_atual:
            print(f"\n{CIANO}ℹ️  Caixa atual em andamento: {len(caixa_atual)}/{CAPACIDADE_CAIXA} peças{RESET}")

    input("\nPressione Enter para voltar ao menu...")


# ---------------------------------------------------------------
def gerar_relatorio() -> None:
    """Gera um resumo geral da produção com estatísticas detalhadas."""
    exibir_cabecalho("📊 RELATÓRIO FINAL DE PRODUÇÃO")

    total_aprovadas = len(pecas_aprovadas)
    total_reprovadas = len(pecas_reprovadas)
    total_pecas = total_aprovadas + total_reprovadas
    total_caixas = len(caixas_fechadas)

    # Resumo Geral
    print(f"{AZUL}{'─' * 50}{RESET}")
    print(f"{AZUL}RESUMO GERAL DA PRODUÇÃO{RESET}")
    print(f"{AZUL}{'─' * 50}{RESET}")
    print(f"Total de peças processadas: {total_pecas}")
    print(f"Peças aprovadas: {VERDE}{total_aprovadas}{RESET} "
          f"({(total_aprovadas/total_pecas*100 if total_pecas > 0 else 0):.1f}%)")
    print(f"Peças reprovadas: {VERMELHO}{total_reprovadas}{RESET} "
          f"({(total_reprovadas/total_pecas*100 if total_pecas > 0 else 0):.1f}%)")
    
    # Informações de Armazenamento
    print(f"\n{AZUL}{'─' * 50}{RESET}")
    print(f"{AZUL}ARMAZENAMENTO{RESET}")
    print(f"{AZUL}{'─' * 50}{RESET}")
    print(f"Caixas fechadas: {AMARELO}{total_caixas}{RESET}")
    print(f"Peças na caixa atual: {len(caixa_atual)}/{CAPACIDADE_CAIXA}")
    
    # Análise de Rejeição
    if pecas_reprovadas:
        print(f"\n{AZUL}{'─' * 50}{RESET}")
        print(f"{AZUL}ANÁLISE DE REJEIÇÕES{RESET}")
        print(f"{AZUL}{'─' * 50}{RESET}")
        
        motivos_count = {}
        for p in pecas_reprovadas:
            motivo = p['motivo']
            motivos_count[motivo] = motivos_count.get(motivo, 0) + 1
        
        for motivo, count in sorted(motivos_count.items(), key=lambda x: x[1], reverse=True):
            print(f"• {motivo}: {count} peça(s)")
    
    # Estatísticas de Qualidade (se houver peças aprovadas)
    if pecas_aprovadas:
        pesos = [p['peso'] for p in pecas_aprovadas]
        comps = [p['comprimento'] for p in pecas_aprovadas]
        
        print(f"\n{AZUL}{'─' * 50}{RESET}")
        print(f"{AZUL}ESTATÍSTICAS DE PEÇAS APROVADAS{RESET}")
        print(f"{AZUL}{'─' * 50}{RESET}")
        print(f"Peso médio: {sum(pesos)/len(pesos):.2f}g")
        print(f"Comprimento médio: {sum(comps)/len(comps):.2f}cm")
        print(f"Distribuição de cores:")
        cores = {}
        for p in pecas_aprovadas:
            cores[p['cor']] = cores.get(p['cor'], 0) + 1
        for cor, qtd in cores.items():
            print(f"  • {cor.capitalize()}: {qtd} peça(s)")

    print(f"\n{AZUL}{'─' * 50}{RESET}")
    input("\nPressione Enter para voltar ao menu...")


# ===============================================================
#   PROGRAMA PRINCIPAL
# ===============================================================
def main():
    """Função principal do programa."""
    limpa_tela()
    print(f"{AZUL}{'=' * 60}{RESET}")
    print(f"{AZUL}{'BEM-VINDO AO SISTEMA PEÇACERTA':^60}{RESET}")
    print(f"{AZUL}{'=' * 60}{RESET}")
    print(f"\n{CIANO}Sistema de Automação Digital para Controle de Qualidade{RESET}")
    print(f"{CIANO}Desenvolvido para otimizar inspeção e armazenamento{RESET}\n")
    input("Pressione Enter para continuar...")

    while True:
        limpa_tela()
        print(f"{AZUL}{'=' * 50}{RESET}")
        print(f"{AZUL}{'MENU PRINCIPAL':^50}{RESET}")
        print(f"{AZUL}{'=' * 50}{RESET}\n")
        print(f"{CIANO}1.{RESET} 📦 Cadastrar nova peça")
        print(f"{CIANO}2.{RESET} 📋 Listar peças aprovadas/reprovadas")
        print(f"{CIANO}3.{RESET} 🗑️  Remover peça cadastrada")
        print(f"{CIANO}4.{RESET} 📦 Listar caixas fechadas")
        print(f"{CIANO}5.{RESET} 📊 Gerar relatório final")
        print(f"{CIANO}0.{RESET} 🚪 Sair")

        escolha = input(f"\n{CIANO}Digite o número da opção desejada: {RESET}").strip()

        match escolha:
            case '1':
                cadastrar_peca()
            case '2':
                listar_pecas()
            case '3':
                remover_peca()
            case '4':
                listar_caixas()
            case '5':
                gerar_relatorio()
            case '0':
                limpa_tela()
                print(f"{VERDE}{'=' * 50}{RESET}")
                print(f"{VERDE}Encerrando o Sistema PeçaCerta...{RESET}")
                print(f"{VERDE}Obrigado por usar nosso sistema!{RESET}")
                print(f"{VERDE}{'=' * 50}{RESET}")
                break
            case _:
                print(f"\n{VERMELHO}❌ Opção inválida! Tente novamente.{RESET}")
                input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()