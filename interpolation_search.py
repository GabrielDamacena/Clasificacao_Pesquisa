def interpolation(chave,ini,fim,lista):
    meio = ini +((fim - ini) * (chave-lista[ini])) / (lista[fim] - lista[ini])

    print(meio)

