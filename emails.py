import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()


user = str(input("Informe seu email: "))
senha = str(input("Informe sua senha: "))
to = str(input("Informe o email que deseja enviar a mensagem: "))
num = int(input("Informe a quantidade de email: "))
msg = str(input("Informe a mensagem que deseja enviar: "))

try:
    server.login(user,senha)
    print("Logado com sucesso")
except:
    print("Email ou senha invalidos. Tente novamente.")

x = 0
while(x < num):
    server.sendmail(user,to,msg)
    x+=1
    print("Contador email\nFoi enviado %d emails" % x)