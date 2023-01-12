from time import sleep

delay = 1


def heroi(matriz):
    valor = 2
    for i in range(0, 4):
        for j in range(0, 4):
            matriz[i][j] += valor
            for l in range(0, 4):
                print(matriz[l])
            if (matriz[i][j] == 2):
                print(f"Heroi está na posição [{i}][{j}]")
                print("Esse local não há monstros, vamos seguir em frente.\n")
                matriz[i][j] = 0
                sleep(delay)
            if (matriz[i][j] == 3):
                print(f"Heroi está na posição [{i}][{j}]")
                print("Encontramos um monstro! Vamos lutar!")
                print("AAAAAAAAAAAAAAAAAA")
                sleep(delay)
                matriz[i][j] = 0
                print("O monstro foi derrotado!\n")

    print("Nossa aventura foi concluída! Não existem mais monstros por aqui.")
