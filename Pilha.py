class Pilha:
    
    def __init__(self):
        self.pilha = []
        self.len_pilha = 0
    
    def inserir(self,i):
        self.pilha.append(i)
        self.len_pilha += 1

    def remover(self):
        if(not self.vazia()):
            self.pilha.pop(self.len_pilha - 1)
            self.len_pilha -= 1
    
    def topo(self):
        if(not self.vazia()):
            return self.pilha[-1]
        print("Pilha vazia")
    
    def vazia(self):
        if(self.len_pilha == 0):
            return True
        return False
    
    def tamanho(self):
        return self.len_pilha
    

ch = Pilha()
ch.inserir(1)
ch.inserir(2)
ch.inserir(3)
#print(ch.topo())
ch.remover()
print(ch.topo())