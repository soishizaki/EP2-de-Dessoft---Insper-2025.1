import random

def rolar_dados(quantidade):
    resultados = []
    for _ in range(quantidade):
        resultado = random.randint(1, 6)  
        resultados.append(resultado)
    return resultados

def guardar_dado(dados_rolados, dados_guardados, indice_para_guardar):
    dado_escolhido = dados_rolados.pop(indice_para_guardar)
    dados_guardados.append(dado_escolhido)
    return [dados_rolados, dados_guardados]

def remover_dado(dados_rolados, dados_guardados, indice_para_remover):
    dado = dados_guardados.pop(indice_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_guardados]

def calcula_pontos_regra_simples(dados):
    pontuacoes = {}
    for face in range(1, 6): 
        soma_face = sum(dado for dado in dados if dado == face)
        pontuacoes[face] = soma_face

    return pontuacoes

