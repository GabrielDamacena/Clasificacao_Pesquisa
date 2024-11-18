class File:
    """Classe que representa um arquivo com informações associadas."""
    def __init__(self, name, path, size):
        self.name = name
        self.path = path
        self.size = size

    def __str__(self):
        return f"Nome: {self.name}, Caminho: {self.path}, Tamanho: {self.size} KB"


class HashTable:
    """Implementação da tabela hash com encadeamento separado."""
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Função hash que gera um índice baseado no nome do arquivo."""
        return sum(ord(c) for c in key) % self.size

    def add_file(self, file):
        """Adiciona um arquivo à tabela hash."""
        index = self._hash(file.name)
        for item in self.table[index]:
            if item.name == file.name:
                print(f"Erro: Um arquivo com o nome '{file.name}' já existe.")
                return
        self.table[index].append(file)
        print(f"Arquivo '{file.name}' adicionado com sucesso.")

    def find_file(self, name):
        """Busca um arquivo pelo nome."""
        index = self._hash(name)
        for file in self.table[index]:
            if file.name == name:
                return file
        return None

    def remove_file(self, name):
        """Remove um arquivo pelo nome."""
        index = self._hash(name)
        for i, file in enumerate(self.table[index]):
            if file.name == name:
                del self.table[index][i]
                print(f"Arquivo '{name}' removido com sucesso.")
                return
        print(f"Erro: Arquivo '{name}' não encontrado.")

    def list_files(self):
        """Lista todos os arquivos armazenados na tabela hash."""
        print("Arquivos armazenados:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Índice {i}:")
                for file in bucket:
                    print(f"  {file}")
        print()


# Exemplo de uso
if __name__ == "__main__":
    # Criação da tabela hash
    hash_table = HashTable()

    # Adicionando arquivos
    hash_table.add_file(File("relatorio.pdf", "/documentos/relatorio.pdf", 1024))
    hash_table.add_file(File("foto.jpg", "/imagens/foto.jpg", 2048))
    hash_table.add_file(File("dados.csv", "/planilhas/dados.csv", 512))
    hash_table.add_file(File("backup.zip", "/backup/backup.zip", 4096))

    # Busca pelo arquivo "dados.csv"
    file = hash_table.find_file("dados.csv")
    if file:
        print("Arquivo encontrado:")
        print(file)
    else:
        print("Arquivo 'dados.csv' não encontrado.")

    # Remove o arquivo "foto.jpg"
    hash_table.remove_file("foto.jpg")

    # Lista todos os arquivos restantes
    hash_table.list_files()
