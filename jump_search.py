import math

def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Tamanho do salto
    prev = 0

    # Pular blocos até que o elemento buscado seja menor que o atual ou o fim da lista seja alcançado
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1  # Elemento não está presente

    # Busca linear dentro do bloco
    for i in range(prev, min(step, n)):
        if arr[i] == x:
            return i  # Elemento encontrado

    return -1  # Elemento não está presente

# Exemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 15
resultado = jump_search(arr, x)

if resultado != -1:
    print(f"Elemento encontrado no índice {resultado}")
else:
    print("Elemento não encontrado")
