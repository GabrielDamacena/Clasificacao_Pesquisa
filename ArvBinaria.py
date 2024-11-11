class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ABB:
    def __init__(self):
        self.raiz = None

    # Função para criar um nó
    def criar_no(self, valor):
        return No(valor)

    # Função para inserir um valor na árvore
    def inserir(self, raiz, valor):
        if raiz is None:
            return self.criar_no(valor)
        
        if valor < raiz.valor:
            raiz.esquerda = self.inserir(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.inserir(raiz.direita, valor)
        
        return raiz

    # Função para impressão em Pré-ordem
    def imprimir_pre_ordem(self, raiz):
        if raiz is not None:
            print(raiz.valor, end=" ")
            self.imprimir_pre_ordem(raiz.esquerda)
            self.imprimir_pre_ordem(raiz.direita)

    # Função para impressão em Ordem Simétrica (in-order)
    def imprimir_ordem_simetrica(self, raiz):
        if raiz is not None:
            self.imprimir_ordem_simetrica(raiz.esquerda)
            print(raiz.valor, end=" ")
            self.imprimir_ordem_simetrica(raiz.direita)

    # Função para impressão em Pós-ordem
    def imprimir_pos_ordem(self, raiz):
        if raiz is not None:
            self.imprimir_pos_ordem(raiz.esquerda)
            self.imprimir_pos_ordem(raiz.direita)
            print(raiz.valor, end=" ")

    # Função para buscar um valor na árvore
    def buscar(self, raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        
        if valor < raiz.valor:
            return self.buscar(raiz.esquerda, valor)
        
        return self.buscar(raiz.direita, valor)

    # Função para encontrar o nó com o valor mínimo
    def minimo(self, raiz):
        while raiz.esquerda is not None:
            raiz = raiz.esquerda
        return raiz

    # Função para deletar um nó
    def deletar(self, raiz, valor):
        if raiz is None:
            return raiz
        
        if valor < raiz.valor:
            raiz.esquerda = self.deletar(raiz.esquerda, valor)
        elif valor > raiz.valor:
            raiz.direita = self.deletar(raiz.direita, valor)
        else:
            # Caso 1: Nó com um único filho ou sem filho
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            
            # Caso 2: Nó com dois filhos
            temp = self.minimo(raiz.direita)
            raiz.valor = temp.valor
            raiz.direita = self.deletar(raiz.direita, temp.valor)

        return raiz

    # Função para iniciar as operações
    def inserir_raiz(self, valor):
        self.raiz = self.inserir(self.raiz, valor)

    def imprimir(self, tipo="ordem_simetrica"):
        if tipo == "pre_ordem":
            self.imprimir_pre_ordem(self.raiz)
        elif tipo == "pos_ordem":
            self.imprimir_pos_ordem(self.raiz)
        else:
            self.imprimir_ordem_simetrica(self.raiz)
        print()

# Exemplo de uso do TAD de ABB
if __name__ == "__main__":
    arvore = ABB()

    # Inserindo elementos na árvore
    arvore.inserir_raiz(50)
    arvore.inserir_raiz(30)
    arvore.inserir_raiz(20)
    arvore.inserir_raiz(40)
    arvore.inserir_raiz(70)
    arvore.inserir_raiz(60)
    arvore.inserir_raiz(80)

    # Impressões de diferentes percursos
    print("Impressão em Pré-ordem:")
    arvore.imprimir(tipo="pre_ordem")

    print("Impressão em Ordem Simétrica (in-order):")
    arvore.imprimir(tipo="ordem_simetrica")

    print("Impressão em Pós-ordem:")
    arvore.imprimir(tipo="pos_ordem")

    # Buscando um valor na árvore
    valor = 40
    resultado = arvore.buscar(arvore.raiz, valor)
    if resultado:
        print(f"O valor {valor} foi encontrado na árvore.")
    else:
        print(f"O valor {valor} não foi encontrado na árvore.")

    # Deletando um valor
    valor_deletar = 20
    print(f"Deletando o valor {valor_deletar}...")
    arvore.raiz = arvore.deletar(arvore.raiz, valor_deletar)

    print("Impressão após remoção de 20 em Ordem Simétrica:")
    arvore.imprimir(tipo="ordem_simetrica")
