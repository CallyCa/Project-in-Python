# coding:utf-8[
class cripto(object):
    @staticmethod
    def cripto(entr):
        def xor(x, y):
            if x == "0" and y == "0":
                return "1"
            elif x == "0" and y == "1":
                return "0"
            elif x == "1" and y == "0":
                return "0"
            elif x == "1" and y == "1":
                return "1"

        entr = entr.split("|")
        codigo = entr[0]
        entrada = entr[1]
        entradaascii = []
        codigoascii = []
        cont = 0
        acentos = ["á", "é", "í", "ó", "ú", "ã", "õ", "â", "ê", "î", "ô", "û", "Á", "É", "Í", "Ó", "Ú", "Ã", "Õ", "Â",
                   "Ê", "Î", "Ô", "Û"]
        acentnum = [225, 233, 237, 243, 250, 227, 245, 226, 234, 238, 244, 251, 193, 201, 205, 211, 218, 195, 213, 194,
                    202, 206, 212, 219]
        while cont < len(entrada):
            verf = False
            caractere = entrada[cont]
            if cont + 1 < len(entrada):
                if caractere + entrada[cont + 1] in acentos:
                    caracteref = caractere + entrada[cont + 1]
                    decimal = acentnum[acentos.index(caracteref)]
                    binario = "a" + bin(decimal)[2:]
                    entradaascii.append(binario)
                    cont += 1
                else:
                    binario = bin(ord(caractere))[2:]
                    if len(binario) != 8:
                        dif = 8 - len(binario)
                        binario = dif * "0" + binario
                    entradaascii.append(binario)
            else:
                binario = bin(ord(caractere))[2:]
                if len(binario) != 8:
                    dif = 8 - len(binario)
                    binario = dif * "0" + binario
                entradaascii.append(binario)
            cont += 1
        for codcarac in codigo:
            codbin = bin(ord(codcarac))[2:]
            if len(codbin) != 8:
                dif = 8 - len(codbin)
                codbin = dif * "0" + codbin
            codigoascii.append(codbin)
        final = ""
        cont = 0
        for msgatual in entradaascii:
            verf = False
            novobin = ""
            cont2 = 0
            if cont == len(codigoascii):
                cont -= len(codigoascii)
            codatual = codigoascii[cont]
            cont += 1
            if msgatual[0] == "a":
                verf = True
                msgatual = msgatual[1:]
            for m in msgatual:
                c = codatual[cont2]
                n = xor(m, c)
                novobin += n
                cont2 += 1
            octal = oct(int(novobin, 2))
            if verf:
                octal = "a" + octal
            final = final + octal + " "
        final = final[:len(final) - 1]
        return final

    @staticmethod
    def decripto(entrada):
        def xorinverso(z, y):
            if z == "0" and y == "0":
                return "1"
            elif z == "0" and y == "1":
                return "0"
            elif z == "1" and y == "0":
                return "0"
            elif z == "1" and y == "1":
                return "1"

        frase = ""
        acentos = ["á", "é", "í", "ó", "ú", "ã", "õ", "â", "ê", "î", "ô", "û", "Á", "É", "Í", "Ó", "Ú", "Ã", "Õ", "Â",
                   "Ê",
                   "Î", "Ô", "Û"]
        acentnum = [225, 233, 237, 243, 250, 227, 245, 226, 234, 238, 244, 251, 193, 201, 205, 211, 218, 195, 213, 194,
                    202,
                    206, 212, 219]
        entrada = entrada.split("|")
        codigo = entrada[0]
        entrada = entrada[1].split(" ")
        novobin = ""
        cont2 = 0
        for octal in entrada:
            if cont2 == len(codigo):
                cont2 -= len(codigo)
            cod = codigo[cont2]
            cod = bin(ord(cod))[2:]
            vefacento = False
            if octal[0] == "a":
                vefacento = True
                octal = octal[1:]
                binario = bin(int(octal, 8))[2:]
                dif = 8 - len(binario)
                binario = dif * "0" + binario
                dif = 8 - len(cod)
                cod = dif * "0" + cod
            else:
                binario = bin(int(octal, 8))[3:]
            novobin = ""
            cont = 0
            for m in binario:
                c = cod[cont]
                n = xorinverso(m, c)
                novobin += str(n)
                cont += 1
            dec = int(str(novobin), 2)
            letraf = chr(dec)
            if vefacento:
                pos = acentnum.index(dec)
                letraf = acentos[pos]
            frase = frase + letraf
            cont2 += 1
        return frase
