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
        ja_esta_na_lista = False
        for outro_valor in dados_sem_repetidos:
            if valor == outro_valor:
                ja_esta_na_lista = True
                break
        if not ja_esta_na_lista:
            dados_sem_repetidos.append(valor)

    quantidade = len(dados_sem_repetidos)
    for i in range(quantidade):
        for j in range(0, quantidade - i - 1):
            atual = dados_sem_repetidos[j]
            proximo = dados_sem_repetidos[j + 1]
            if atual > proximo:
                dados_sem_repetidos[j], dados_sem_repetidos[j + 1] = proximo, atual

    sequencias_altas_possiveis = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]

    for sequencia in sequencias_altas_possiveis:
        todos_os_numeros_encontrados = True
        for numero in sequencia:
            encontrado_na_lista = False
            for valor in dados_sem_repetidos:
                if numero == valor:
                    encontrado_na_lista = True
                    break
            if not encontrado_na_lista:
                todos_os_numeros_encontrados = False
                break
        if todos_os_numeros_encontrados:
            return 30  

    return 0  

def calcula_pontos_full_house(dados):
    contagem = []
    for i in range(len(dados)):
        valor = dados[i]
        ja_foi_contado = False

        for j in range(len(contagem)):
            if contagem[j][0] == valor:
                contagem[j][1] += 1  
                ja_foi_contado = True
                break

        if not ja_foi_contado:
            contagem.append([valor, 1])

    achou_tres = False
    achou_dois = False

    for i in range(len(contagem)):
        quantidade = contagem[i][1]
        if quantidade == 3:  
            achou_tres = True
        elif quantidade == 2:  
            achou_dois = True

    if achou_tres and achou_dois:
        soma = 0
        for i in range(len(dados)):  
            soma += dados[i]
        return soma
    else:
        return 0

def calcula_pontos_quadra(dados):
    contagem = []
    for i in range(len(dados)):
        valor = dados[i]
        ja_foi_contado = False

        for j in range(len(contagem)):
            if contagem[j][0] == valor:
                contagem[j][1] += 1 
                ja_foi_contado = True
                break

        if not ja_foi_contado:
            contagem.append([valor, 1])

    for i in range(len(contagem)):
        if contagem[i][1] >= 4:  
            soma = 0
            for j in range(len(dados)):
                soma += dados[j]
            return soma

    return 0

def calcula_pontos_quina(dados):
    contagem = []
    for i in range(len(dados)):
        valor = dados[i]
        ja_foi_contado = False

        for j in range(len(contagem)):
            if contagem[j][0] == valor:
                contagem[j][1] += 1  
                ja_foi_contado = True
                break

        if not ja_foi_contado:
            contagem.append([valor, 1])

    for i in range(len(contagem)):
        if contagem[i][1] >= 5:
            return 50

    return 0

def calcula_pontos_regra_avancada(dados):
    lista_pontuacoes = []

    pontos_quina = calcula_pontos_quina(dados)
    if pontos_quina == 50:
        lista_pontuacoes.append(['cinco_iguais', 50])
    else:
        lista_pontuacoes.append(['cinco_iguais', 0])

    pontos_full_house = calcula_pontos_full_house(dados)
    lista_pontuacoes.append(['full_house', pontos_full_house])

    pontos_quadra = calcula_pontos_quadra(dados)
    lista_pontuacoes.append(['quadra', pontos_quadra])

    pontos_sequencia_alta = calcula_pontos_sequencia_alta(dados)
    lista_pontuacoes.append(['sequencia_alta', pontos_sequencia_alta])

    pontos_sequencia_baixa = calcula_pontos_sequencia_baixa(dados)
    lista_pontuacoes.append(['sequencia_baixa', pontos_sequencia_baixa])

    pontos_soma = calcula_pontos_soma(dados)
    lista_pontuacoes.append(['sem_combinacao', pontos_soma])

    dicionario_final = {}
    for i in range(len(lista_pontuacoes)):
        nome = lista_pontuacoes[i][0]
        valor = lista_pontuacoes[i][1]
        dicionario_final[nome] = valor

    return dicionario_final

def faz_jogada(dados, categoria, cartela_de_pontos):
    if categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
        numero = 0
        if categoria == "1":
            numero = 1
        elif categoria == "2":
            numero = 2
        elif categoria == "3":
            numero = 3
        elif categoria == "4":
            numero = 4
        elif categoria == "5":
            numero = 5
        elif categoria == "6":
            numero = 6
        cartela_de_pontos["regra_simples"][numero] = pontuacoes[numero]  
        pontuacoes = calcula_pontos_regra_simples(dados)
    else:
        pontuacoes = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos["regra_avancada"][categoria] = pontuacoes[categoria]
    return cartela_de_pontos

