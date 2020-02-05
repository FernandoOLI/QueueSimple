print("------------ exemplo de fila com vetores ---------")
fila = [10, 20, 30, 40, 50]
print("------------fila com valores---------")
print(fila)
print("---------------------------------")
fila.append(60)
print("------------ inserindo valor 60 no fim da fila ---------")
print(fila)
print("---------------------------------")
print("------------ removendo o primeiro elemento da fila ---------")
print(fila.pop(0)) # remove o primeiro elemento da lista
print("---------------------------------")
print("------------ imprimindo fila ---------")
print(fila)
print("---------------------------------")
print("------------ removendo o primeiro elemento da fila ---------")
print(fila.pop(0)) # remove o primeiro elemento da lista
print("---------------------------------")
print("------------ imprimindo fila ---------")
print(fila)
print("---------------------------------")
print("------------ removendo o primeiro elemento da fila ---------")
print(fila.pop(0)) # remove o primeiro elemento da lista
print("---------------------------------")
print("------------ imprimindo fila ---------")
print(fila)
print("---------------------------------")

print("------------ exemplo de fila com classe---------")
class Queue:
    def __init__(self):
       self.items = []

    def isEmpty(self):
       return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q=Queue()
print("------------ imprimindo fila ---------")
print(q.items)
print("---------------------------------")
print("------------ inserindo valor na fila ---------")
q.enqueue(4)
print(q.items)
print("---------------------------------")
print("------------ inserindo valor na fila ---------")
q.enqueue('dog')
print(q.items)
print("---------------------------------")
print("------------ inserindo valor na fila ---------")
q.enqueue(True)
print(q.items)
print("---------------------------------")
print("------------ tamanho da fila ---------")
print(q.size())
print("---------------------------------")
print("------------ removendo valor da fila ---------")
print(q.dequeue())
print(q.items)
print("---------------------------------")
