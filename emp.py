import os
import sys

class Empresa(object):

    def __init__(self):

        ## Inicializa o construtor e passa adiante.
        pass

    def pessoa(self):

         ## Aqui cria os parametros que serao usados nas outras funcoes

        count=0
        max = 5
        self.nome = input("Informe seu nome: ")
        self.idade = int(input("Informe sua idade: "))

        ## Aqui verifica se a idade eh menor que 0 ou maior que 90

        while(self.idade <= 0 or self.idade > 90):
            print("Idade invalida.Tente novamente.")
            self.idade = int(input("Informe sua idade: "))
            count+=1
        
        self.crachaID = input("Informe o ID do seu cracha: ")

        ## Aqui verifica se o numero maximo de caracteres definido em MAX

        while(len(self.crachaID) > max):
            print("ID do cracha invalido. Tente novamente")
            self.crachaID = input("Informe o ID do seu cracha: ")
            count+=1


        self.setor = int(input("Setor: 1 - T.I: "))
        

    def escolha(self):

        # #Aqui ira realizar a criacao de usuario

        if(self.setor == 1):
            print("Voce %s eh da T.I" % self.nome)
            print("\nCriacao de usuario\n")
            self.opcao = int(input("Deseja criar um usuario? 1 - Sim / 2 - Nao: "))
            try:
                if(self.opcao == 1):
                    self.usuario = input("Informe um usuario: ")
                    self.senha = input("Informe uma senha: ")
                if(self.opcao == 2):
                    print("Voce escolheu nao utilizar um usuario.")
                    print("Voce saiu.")
                    
            except ValueError:
                print("Nome de usuario ou senha invalido(s). Tente novamente.")

    def porta(self):

        ## Aqui sera a validacao do usuario e senha

        print("\nValidacao de usuario\n")
        count = 0
        self.usuarios = input("Informe um usuarios: ")
        self.senhas = input("Informe uma senhas: ")
        while(self.usuarios != self.usuario or self.senhas != self.senha):
            print("Usuario ou senha incorretos. Tente novamente")
            self.usuarios = input("Informe um usuario: ")
            self.senhas = input("Informe uma senha: ")
            count+=1

        if(self.usuarios == self.usuario):
            print("Usuario correto. Bem vindo %s" % self.usuarios)
    
    def criacaoArquivo(self):
        
        ## Pode ser adicionado w = escrita, r = leitura, x = execucao e a = append ou adicionar elementos.

        self.arquivo = open("Conversa.txt", "a")

        self.letra = input("Informe uma frase: ")

        ## com o comando write, este irá escrever no arquivo txt e saltar uma linha para o proximo.

        self.arquivo.write(str(self.usuario) + ": %s\n" % self.letra)

        ## Sempre quando acabar um comando devemos fechar o arquivo.

        self.arquivo.close()

        ## Aqui abre o arquivo para rodar o looping for.

        self.arquivo = open("Conversa.txt")

        ## sys.stdout é usado para a saida de instrucoes print
        ## Ira percorrer o arquivo e mostrar todas as palavras contidas.

        for i in self.arquivo:
            sys.stdout.write(i)
        print(self.arquivo.read())
        self.arquivo.close()

## Neste chama a Classe empresa e suas funçoes
x = Empresa()
x.pessoa()
x.escolha()
x.porta()
x.criacaoArquivo()
                
