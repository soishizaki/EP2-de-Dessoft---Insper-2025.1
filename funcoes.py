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
    pontuacoes = {face: 0 for face in range(1, 7)}  
    for valor in dados:
        if 1 <= valor <= 6:
            pontuacoes[valor] += valor

    return pontuacoes

