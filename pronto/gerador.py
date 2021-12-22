import random

menor = int(input('Digite a quantida de jogos de 1 a 30: '))
maior = int(input('Digite a quantida de jogos de 31 a 60: '))
todos = int(input('Digite a quantida de jogos de 1 a 60 numeros: '))


with open('sorteio_aleatorio.txt', 'w') as arquivo:
    # menor
    arquivo.write(f'{menor}x Jogos de 1 a 30\n')
    for i in range(menor):
        sorteio = []
        for j in range(6):
            sorteio.append(random.randint(1, 30))
        sorteio.sort()
        arquivo.write(f'Jogo {i+1}: {sorteio}\n')

    # maior
    arquivo.write(f'\n{maior}x Jogos de 31 a 60\n')
    for i in range(maior):
        sorteio = []
        for j in range(6):
            sorteio.append(random.randint(31, 60))
        sorteio.sort()
        arquivo.write(f'Jogo {i+1}: {sorteio}\n')

    # todos
    arquivo.write(f'\n{todos}x Jogos de 1 a 60 numeros\n')
    for i in range(todos):
        sorteio = []
        for j in range(6):
            sorteio.append(random.randint(1, 60))
        sorteio.sort()
        arquivo.write(f'Jogo {i+1}: {sorteio}\n')

    print('Jogos gerados com sucesso!')
a = input('Pressione ENTER para sair')