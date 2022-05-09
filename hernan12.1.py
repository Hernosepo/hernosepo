import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('es.wikipedia.org', 80))
cmd = 'GET https://es.wikipedia.org/wiki/Anexo:Estad%C3%ADsticas_de_la_selecci%C3%B3n_de_f%C3%BAtbol_de_Argentina#Jugadores HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
