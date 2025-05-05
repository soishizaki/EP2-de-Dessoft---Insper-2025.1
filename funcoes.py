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

def calcula_pontos_soma(dados):
    total = 0  
    for valor in dados:
        total += valor  
    return total

def calcula_pontos_sequencia_baixa(dados):
    dados_unicos = []
    for valor in dados:
        duplicado = False
        for item in dados_unicos:
            if item == valor:
                duplicado = True
                break
        if not duplicado:
            dados_unicos.append(valor)
    n = len(dados_unicos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dados_unicos[j] > dados_unicos[j + 1]:
                dados_unicos[j], dados_unicos[j + 1] = dados_unicos[j + 1], dados_unicos[j]
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for seq in sequencias:
        contem_todos = True
        for numero in seq:
            encontrado = False
            for dado in dados_unicos:
                if dado == numero:
                    encontrado = True
                    break
            if not encontrado:
                contem_todos = False
                break
        if contem_todos:
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    dados_sem_repetidos = []
    for valor in dados:
        for outro_valor in dados_sem_repetidos:
            if valor == outro_valor:
                break 
        else:
            dados_sem_repetidos.append(valor)

    quantidade = len(dados_sem_repetidos)
    for i in range(quantidade):
        for j in range(0, quantidade - i - 1):
            atual = dados_sem_repetidos[j]
            proximo = dados_sem_repetidos[j + 1]
            if atual < proximo:  
                dados_sem_repetidos[j], dados_sem_repetidos[j + 1] = proximo, atual

    sequencias_altas_possiveis = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]

    for sequencia in sequencias_altas_possiveis:
        todos_os_numeros_encontrados = True
        for numero in sequencia:
            if numero not in dados:  
                todos_os_numeros_encontrados = False
                break
        if todos_os_numeros_encontrados:
            return 30

    return 0
