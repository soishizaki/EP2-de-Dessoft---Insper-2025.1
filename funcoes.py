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