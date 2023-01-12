def ambiente():

    print("Esse é o nosso ambiente: \n")

    matriz = [[0, 0, 0, 1], [0, 0, 1, 1],
              [0, 1, 0, 0], [1, 0, 0, 1]]  # ambiente estático
    for l in range(0, 4):
        print(matriz[l])

    print("\n")

    print("Aqui vamos começar nossa aventura!\n")

    return matriz
