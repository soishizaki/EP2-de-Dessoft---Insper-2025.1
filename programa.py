from funcoes import *

cartela_de_pontuação = {
    'regra_simples': {
        1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}
imprime_cartela(cartela_de_pontuação)

categs_regra_simples = ['1', '2', '3', '4', '5', '6']
categs_regra_avançada = [
    'sem_combinacao', 'quadra', 'full_house',
    'sequencia_baixa', 'sequencia_alta', 'cinco_iguais'
]

rodada = 0
while rodada < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogando = True

    while jogando:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        a = input()

        while a not in ['0', '1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            a = input()
        if a == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            b = int(input())
            dados_rolados, dados_guardados = guardar_dado(dados_rolados, dados_guardados, b)
        elif a == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            b = int(input())
            dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, b)
        elif a == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
        elif a == '4':
            imprime_cartela(cartela_de_pontuação)
        elif a == '0':
            dados_finais = dados_guardados + dados_rolados
            validacao = False
            print("Digite a combinação desejada:")
            while not validacao:
                d = input()
                if d in categs_regra_simples:
                    n = int(d)
                    if cartela_de_pontuação['regra_simples'][n] == -1:
                        cartela_de_pontuação = faz_jogada(dados_finais, d, cartela_de_pontuação)
                        validacao = True
                    else:
                        print("Essa combinação já foi utilizada.")
                elif d in categs_regra_avançada:
                    if cartela_de_pontuação['regra_avancada'][d] == -1:
                        cartela_de_pontuação = faz_jogada(dados_finais, d, cartela_de_pontuação)
                        validacao = True
                    else:
                        print("Essa combinação já foi utilizada.")
                else:
                    print("Combinação inválida. Tente novamente.")
            jogando = False
    rodada += 1

imprime_cartela(cartela_de_pontuação)
total_pontos = 0
pontos_bonus = 0

for valor in cartela_de_pontuação['regra_simples'].values():
    if valor != -1:
        total_pontos += valor
        pontos_bonus += valor
for valor in cartela_de_pontuação['regra_avancada'].values():
    if valor != -1:
        total_pontos += valor
if pontos_bonus >= 63:
    total_pontos += 35

print(f"Pontuação total: {total_pontos}")
