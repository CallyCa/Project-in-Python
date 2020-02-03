# -*- coding: utf-8 -*-

import Tkinter
import socket
import threading, time
import interface

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

chatters = {}
mainWidgets = {}
newChatWidgets = {}
recMessage = True
socketTimeout = 0.5


ip = ""
port = 8080

def enviar(data):
    global mainWidgets, soc, chatters
    if "ListaChat" not in mainWidgets:
        print "Lista não encontrada."
        return
    else:
        selection = mainWidgets["ListaChat"].get(Tkinter.ACTIVE)
        if selection not in chatters:
            print "Erro: Usuário não encontrado."
        else:
            soc.sendto(str(data), chatters[selection])

def vhat():
    global mainWidgets, soc
    if "ListaChat" not in mainWidgets:
        print "Lista nao encontrada."
        return
    else:
        outrochat()


def outrochat():
    LoginFor = Tkinter.Tk()

    IPLabel = Tkinter.Label(LoginFor, text = "IP")
    IPLabel.grid(row = 0, column = 0)

    PortLabel = Tkinter.Label(LoginFor, text = "Porta")
    PortLabel.grid(row = 1, column = 0)

    IPEntry = Tkinter.Entry(LoginFor, text = "IP")
    IPEntry.grid(row = 0, column = 1)

    PortEntry = Tkinter.Entry(LoginFor, text = "Porta")
    PortEntry.grid(row = 1, column = 1)

    ConnectButton = Tkinter.Button(LoginFor, text = "Conectar", command = lambda: addchat(IPEntry.get(), PortEntry.get(), LoginFor))
    ConnectButton.grid(row = 2, column = 0, columnspan = 2, sticky=Tkinter.E+Tkinter.W)

    LoginFor.mainloop()

def addchat(ip, port, form):
    global mainWidgets, chatters
    mainWidgets["ListaChat"].insert(0, ip)
    chatters[ip] = (ip, int(port))
    form.destroy()

def recevpo():
    global soc, widgets
    while recMessage:
        try:
            (data, sender) = soc.recvfrom(1024)
            print "Reecebendo %s de %s" % (str(data), str(sender))
        except socket.timeout:
            pass




def kill(toalinha, sock):
    global recMessage
    toalinha.destroy()
    recMessage = False
    time.sleep(socketTimeout)
    sock.close()

def main():
    global mainWidgets, soc
    vidrodragrao = Tkinter.Tk()
    vidrodragrao.title("CH4T MU1T0 L0C0")

    mainWidgets["ListaChat"] = Tkinter.Listbox(vidrodragrao)

    mainWidgets["ListaChat"].grid(row = 0, column = 0,sticky=Tkinter.N+Tkinter.S)

    mainWidgets["chatBox"] = Tkinter.Text(vidrodragrao)
    mainWidgets["chatBox"].grid(row = 0, column = 1)

    mainWidgets["chatInput"] = Tkinter.Entry(vidrodragrao)
    mainWidgets["chatInput"].grid(row = 1, rowspan = 2,column = 1, sticky = Tkinter.W+Tkinter.E+Tkinter.S+Tkinter.N)

    mainWidgets["enviarInput"] = Tkinter.Button(vidrodragrao, text = "Enviar", command = lambda: enviar(mainWidgets["chatInput"].get()))
    mainWidgets["enviarInput"].grid(row = 1, column = 0, sticky = Tkinter.W+Tkinter.E)

    mainWidgets["ChatBtn"] = Tkinter.Button(vidrodragrao, text = "Novo Chat", command = vhat)
    mainWidgets["ChatBtn"].grid(row = 2, column = 0, sticky = Tkinter.W+Tkinter.E)

    soc.bind((ip, port))
    soc.settimeout(1)

    vidrodragrao.protocol("WM_DELETE_WINDOW", lambda: kill(vidrodragrao, soc))
    receiveThread = threading.Thread(target = recevpo, args = ())
    receiveThread.start()

    vidrodragrao.mainloop()

if __name__ == "__main__":
    main()

