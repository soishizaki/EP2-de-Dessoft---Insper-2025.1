#Nesse exercício vamos tentar ir passo a passo para tentar evitar erros. 

from os import remove
from funcoes import rolar_dados, guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, calcula_pontos_quadra, calcula_pontos_quina, calcula_pontos_regra_avancada, faz_jogada, imprime_cartela

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

categs_regra_simples = ['1', '2', '3', '4', '5', '6']
categs_regra_avançada = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

rodada = 0
while rodada < 12:
    dados_rolados = rolar_dados(6)
    dados_guardados = []
    rerrolagens = 0
    jogando = True
    while jogando:
        print(f'Dados rolados: {dados_rolados}')
        print(f'Dados guardados: {dados_guardados}')
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        a = input()
        opcoes = False
        while not opcoes:
            for opcao in ['0', '1', '2', '3', '4']:
                if a == opcao:
                    opcoes = True
            if not opcoes:
                print("Opção inválida. Tente novamente:")
                a = input()

            if a == '1':
                print("Digite o índice do dado que quer guardar (0 a 5):")
                b = int(input())
                resultado = guardar_dado(dados_rolados, dados_guardados, b)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]

            elif a == '2':
                print("Digite o índice do dado que quer remover dos guardados (0 a 5):")
                b = int(input())
                resultado = remove(dados_rolados, dados_guardados, b)
                dados_rolados = resultado[0]
                dados_guardados = resultado[1]
            
            elif a == '3':
                if rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    quantidade = 0
                    for dado in dados_rolados:
                        quantidade = 1
                    dados_rolados = rolar_dados(quantidad)
                    rerrolagens += 1

            elif a == '4':
                imprime_cartela(cartela_de_pontuação)

            elif a == '0':
                dados_finais = []
                for c in dados_guardados:
                    dados_finais.append(c)
                for c in dados_rolados:
                    dados_finais.append(c)
                print("Digite a combinação desejada:")
                d = input()
                validacao = False
                while not validacao:
                    simples = False
                    for e in categs_regra_simples:
                        if d == e:
                            simples = True
                    avancada = False
                    for d in categs_regra_avançada:
                        if d == e:
                            avancada = True


                            
                


