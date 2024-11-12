class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}"

class NoBST:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if self.raiz is None:
            self.raiz = NoBST(produto)
        else:
            self._inserir(self.raiz, produto)

    def _inserir(self, no_atual, produto):
        if produto.id < no_atual.produto.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoBST(produto)
            else:
                self._inserir(no_atual.esquerda, produto)
        elif produto.id > no_atual.produto.id:
            if no_atual.direita is None:
                no_atual.direita = NoBST(produto)
            else:
                self._inserir(no_atual.direita, produto)

    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, no_atual, id):
        if no_atual is None:
            return None
        if no_atual.produto.id == id:
            return no_atual.produto
        elif id < no_atual.produto.id:
            return self._buscar(no_atual.esquerda, id)
        else:
            return self._buscar(no_atual.direita, id)

    def remover(self, id):
        self.raiz = self._remover(self.raiz, id)

    def _remover(self, no_atual, id):
        if no_atual is None:
            return no_atual
        if id < no_atual.produto.id:
            no_atual.esquerda = self._remover(no_atual.esquerda, id)
        elif id > no_atual.produto.id:
            no_atual.direita = self._remover(no_atual.direita, id)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            menor_no = self._encontrar_menor(no_atual.direita)
            no_atual.produto = menor_no.produto
            no_atual.direita = self._remover(no_atual.direita, menor_no.produto.id)
        return no_atual

    def _encontrar_menor(self, no_atual):
        while no_atual.esquerda is not None:
            no_atual = no_atual.esquerda
        return no_atual

    def listar_em_ordem(self):
        produtos = []
        self._listar_em_ordem(self.raiz, produtos)
        return produtos

    def _listar_em_ordem(self, no_atual, produtos):
        if no_atual is not None:
            self._listar_em_ordem(no_atual.esquerda, produtos)
            produtos.append(no_atual.produto)
            self._listar_em_ordem(no_atual.direita, produtos)

# Criação da árvore
arvore_produtos = ArvoreBST()

# Inserindo produtos
arvore_produtos.inserir(Produto(30, "Produto A", "Descrição A", 50.0))
arvore_produtos.inserir(Produto(20, "Produto B", "Descrição B", 30.0))
arvore_produtos.inserir(Produto(40, "Produto C", "Descrição C", 70.0))

# Buscando um produto
produto = arvore_produtos.buscar(20)
if produto:
    print("Produto encontrado:", produto)
else:
    print("Produto não encontrado.")

# Listando produtos em ordem crescente de ID
print("Produtos em ordem crescente:")
for prod in arvore_produtos.listar_em_ordem():
    print(prod)

# Removendo um produto
arvore_produtos.remover(20)
print("Após remoção do produto com ID 20:")
for prod in arvore_produtos.listar_em_ordem():
    print(prod)
