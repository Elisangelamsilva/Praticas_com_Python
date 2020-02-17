while True:
    minha_string2 = input('Digite uma frase: ')
    tamanho_string = len(minha_string2)

    contagem = 0
    letra = ''
    c = 0
    while c < tamanho_string:
        qtd_vezes_letra = minha_string2.count(minha_string2[c])

        if contagem < qtd_vezes_letra and minha_string2[c].strip():
            letra = minha_string2[c]
            contagem = qtd_vezes_letra

        #print(minha_string[c], conta)


        c += 1

    print(letra, contagem)