class Jogo:
    def __init__(self, jogo_id, titulo, desenvolvedor, preco, generos):
        self.jogo_id = jogo_id
        self.titulo = titulo
        self.desenvolvedor = desenvolvedor
        self.preco = preco
        self.generos = generos  


class NoJogo:
    def __init__(self, jogo):
        self.jogo = jogo
        self.esquerda = None
        self.direita = None


class ArvoreJogos:
    def __init__(self):
        self.raiz = None

    def inserir(self, jogo):
        novo_no = NoJogo(jogo)
        if not self.raiz:
            self.raiz = novo_no
        else:
            self._inserir_recursivo(self.raiz, novo_no)

    def _inserir_recursivo(self, atual, novo_no):
        if novo_no.jogo.preco < atual.jogo.preco:
            if atual.esquerda:
                self._inserir_recursivo(atual.esquerda, novo_no)
            else:
                atual.esquerda = novo_no
        else:
            if atual.direita:
                self._inserir_recursivo(atual.direita, novo_no)
            else:
                atual.direita = novo_no

    def buscar_por_preco(self, preco):
        return self._buscar_preco_recursivo(self.raiz, preco)

    def _buscar_preco_recursivo(self, atual, preco):
        if not atual:
            return []
        if atual.jogo.preco == preco:
            return [atual.jogo]
        elif preco < atual.jogo.preco:
            return self._buscar_preco_recursivo(atual.esquerda, preco)
        else:
            return self._buscar_preco_recursivo(atual.direita, preco)

    def busca_por_faixa_preco(self, preco_minimo, preco_maximo):
        jogos = []
        self._buscar_faixa_recursivo(self.raiz, preco_minimo, preco_maximo, jogos)
        return jogos

    def _buscar_faixa_recursivo(self, atual, preco_minimo, preco_maximo, jogos):
        if not atual:
            return
        if preco_minimo <= atual.jogo.preco <= preco_maximo:
            jogos.append(atual.jogo)
        if preco_minimo < atual.jogo.preco:
            self._buscar_faixa_recursivo(atual.esquerda, preco_minimo, preco_maximo, jogos)
        if atual.jogo.preco < preco_maximo:
            self._buscar_faixa_recursivo(atual.direita, preco_minimo, preco_maximo, jogos)


class HashGeneros:
    def __init__(self):
        self.genero_para_jogos = {}

    def adicionar_jogo(self, jogo):
        for genero in jogo.generos:
            if genero not in self.genero_para_jogos:
                self.genero_para_jogos[genero] = []
            self.genero_para_jogos[genero].append(jogo.jogo_id)

    def obter_jogos(self, genero):
        return self.genero_para_jogos.get(genero, [])


class MotorBuscaJogos:
    def __init__(self):
        self.catalogo_jogos = ArvoreJogos()
        self.generos = HashGeneros()

    def adicionar_jogo(self, jogo):
        self.catalogo_jogos.inserir(jogo)
        self.generos.adicionar_jogo(jogo)

    def buscar_por_preco(self, preco):
        return self.catalogo_jogos.buscar_por_preco(preco)

    def buscar_por_faixa_preco(self, preco_minimo, preco_maximo):
        return self.catalogo_jogos.busca_por_faixa_preco(preco_minimo, preco_maximo)

    def buscar_por_genero(self, genero):
        return self.generos.obter_jogos(genero)


def menu_principal():
    motor = MotorBuscaJogos()

    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Adicionar Jogo")
        print("2. Buscar por Preço")
        print("3. Buscar por Faixa de Preço")
        print("4. Buscar por Gênero")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n=== ADICIONAR JOGO ===")
            jogo_id = int(input("ID do jogo: "))
            titulo = input("Título do jogo: ")
            desenvolvedor = input("Desenvolvedor: ")
            preco = float(input("Preço: "))
            generos = input("Gêneros (separados por vírgula): ").split(",")
            generos = [g.strip() for g in generos]
            novo_jogo = Jogo(jogo_id, titulo, desenvolvedor, preco, generos)
            motor.adicionar_jogo(novo_jogo)
            print(f"Jogo '{titulo}' adicionado com sucesso!")

        elif escolha == "2":
            print("\n=== BUSCAR POR PREÇO ===")
            preco = float(input("Digite o preço: "))
            jogos = motor.buscar_por_preco(preco)
            if jogos:
                print(f"Jogos com preço R${preco}: {[j.titulo for j in jogos]}")
            else:
                print(f"Nenhum jogo encontrado com preço R${preco}.")

        elif escolha == "3":
            print("\n=== BUSCAR POR FAIXA DE PREÇO ===")
            preco_minimo = float(input("Preço mínimo: "))
            preco_maximo = float(input("Preço máximo: "))
            jogos = motor.buscar_por_faixa_preco(preco_minimo, preco_maximo)
            if jogos:
                print(f"Jogos entre R${preco_minimo} e R${preco_maximo}: {[j.titulo for j in jogos]}")
            else:
                print(f"Nenhum jogo encontrado na faixa de preço.")

        elif escolha == "4":
            print("\n=== BUSCAR POR GÊNERO ===")
            genero = input("Digite o gênero: ")
            jogo_ids = motor.buscar_por_genero(genero)
            if jogo_ids:
                print(f"Jogos do gênero '{genero}': {jogo_ids}")
            else:
                print(f"Nenhum jogo encontrado no gênero '{genero}'.")

        elif escolha == "5":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")



menu_principal()
