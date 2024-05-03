 #Funcionamento dos sockets: https://github.com/Victor-Santana-2/Sockets

import socket

try: 
    #                           IPV4           TCP 
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error:
        print("houve um erro durante a criação do socket")  
        exit()

host = '' #127.0.0.1   Entre as '' deve  ser adicionado um endereço IP Válido 
port = 9999 #Porta de comunicação

tcp_socket.bind((host, port)) #listando 
tcp_socket.listen(1)

while True:
      c, addr = tcp_socket.accept()
      print("connection from {}:{}".format(addr[0], addr[1])) #Ao estabelecer a conexão ele fecha o servidor
      c.close

tcp_socket.close() #fecha o server
