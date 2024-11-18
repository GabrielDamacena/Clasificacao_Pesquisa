class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}
    
    def _hash(self, key):
        """Função hash simples baseada no resto da divisão."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insere um valor na hash table."""
        index = self._hash(key)
        self.table[index].append((key, value))
    
    def search(self, key):
        """Procura por uma chave na hash table."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None  # Retorna None se a chave não for encontrada
    
    def remove(self, key):
        """Remove uma chave e seu valor da hash table."""
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]

# Exemplo de uso
htable = SimpleHashTable(10)
htable.insert("Alice", 25)
htable.insert("Bob", 30)
htable.insert("Charlie", 35)

print(htable.search("Alice"))  # Saída: 25
htable.remove("Alice")
print(htable.search("Alice"))  # Saída: None


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        """Função hash simples baseada no resto da divisão."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insere um valor na hash table usando lista encadeada."""
        index = self._hash(key)
        new_node = Node(key, value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next is not None:
                if current.key == key:  # Atualiza o valor se a chave já existe
                    current.value = value
                    return
                current = current.next
            current.next = new_node
    
    def search(self, key):
        """Procura por uma chave na hash table."""
        index = self._hash(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None  # Retorna None se a chave não for encontrada
    
    def remove(self, key):
        """Remove uma chave e seu valor da hash table."""
        index = self._hash(key)
        current = self.table[index]
        prev = None
        while current is not None:
            if current.key == key:
                if prev is None:  # O nó a ser removido é o primeiro
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

# Exemplo de uso
htable = LinkedHashTable(10)
htable.insert("Alice", 25)
htable.insert("Bob", 30)
htable.insert("Charlie", 35)

print(htable.search("Alice"))  # Saída: 25
htable.remove("Alice")
print(htable.search("Alice"))  # Saída: None
