contas = []
saldos = []

def main():
    i = True
    while(i):
        oper = int(input("Informe uma opcao: 1 - Criar conta, 2 - Depositar, 3 - Saque, 4 - Ver conta, 5 - Sair: "))
        while(oper not in range(1,6)):
            print("Operacao invalida. Tente novamente\n")
            oper = int(input("Informe uma opcao: 1 - Criar conta, 2 - Depositar, 3 - Saque, 4 - Ver conta, 5 - Sair: "))
        if(oper == 1):
            criaContas()
        elif(oper == 2):
            deposito()
        elif(oper == 3):
            saque()
        elif(oper == 4):
            ver_saldo()
        else:
            i = False
            print("Voce saiu.\n")

def criaContas():
    global contas,saldos
    conta = int(input("Digite o numero da conta: "))
    while(conta in contas or len(str(conta)) != 6):
        print("Numero ja utilizado ou numero de caracteres faltando.\n")
        conta = int(input("Digite o numero da conta: "))
    contas.append(conta)
    pdep = float(input("Informe o valor para deposito: "))
    while(pdep <= 0):
        print("Deposito invalido. Tente novamente\n")
        pdep = float(input("Informe o valor para deposito: "))
    saldos.append(pdep)
    print("\n")

def deposito():
    global contas,saldos,ver
    verificacao()
    depo = float(input("Informe o valor do deposito: "))
    saldos[contas.index(ver)] += depo
    print("Voce realizou um deposito de R$ %0.2f\n Dinheiro restante: R$ %0.2f\n" % depo,saldos[contas.index(ver)])
    print("\n")

def saque():
    global contas,saldos,ver
    verificacao()
    saq = float(input("Digite o valor do saque: "))
    while(saldos[contas.index(ver)] < saq):
        print("Voce nao tem dinheiro suficiente para sacar. Tente novamente\n")
        saq = float(input("Digite o valor do saque: "))
    saldos[contas.index(ver)] -= saq
    print("Voce sacou R$ %0.2f\nDinheiro restante: R$ %.2f " % (saq,saldos[contas.index(ver)]))
    print("\n")

def ver_saldo():
    global contas,saldos,ver
    ver = int(input("Digite o numero da conta: "))
    verificacao()
    print("O saldo da sua conta eh: R$ %.2f" % (saldos[contas.index(ver)]))
    print("\n")

def verificacao():
    global ver
    ver = int(input("Informe o numero da sua conta: "))
    while(ver not in contas):
        print("Conta invalida. Tente novamente\n")
        ver = int(input("Informe o numero da sua conta: "))

main()