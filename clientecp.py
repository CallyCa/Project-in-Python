import socket
import threading
import sys
import pickle
import cripto
from tkinter import *

class Cliente():
    """docstring for Cliente"""

    def __init__(self, host="10.50.22.132", port=8080):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        msg_recv = threading.Thread(target=self.msg_recv)

        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = raw_input()
            msg = cp.cripto(chave + "|" + msg)
            self.send_msg(msg)

    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    msgrec = pickle.loads(data)
                    msgrec = cp.decripto(chave + "|" + msgrec)
                    print(msgrec)
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))


janela = Tk()
janela.title('')
janela.geometry('800x600')

janela.mainloop()

c = Cliente()
