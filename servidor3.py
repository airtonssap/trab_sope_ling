import socket
import struct

lista = []
n = input("Número 'n' de parcelas da série a ser calculadas: ")
c = input("Número 'c' de clientes que farão parte do processamento: ")
print('1 - Processamento interativo.')
print('2 - Processamento em lote.')
p = input('1 ou 2: ')

host = socket.gethostname()
porta = 55551

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, porta))
serv.listen()
print('Aguardando conexão de um cliente')
con, adr = serv.accept()

print('Conectado em: ', adr)

con.sendall(str.encode(p))
msg = con.recv(1024)
print(msg.decode())

con.sendall(str.encode(n))
msg = con.recv(1024)
print(msg.decode())

con.sendall(str.encode(c))
msg = con.recv(1024)
print(msg.decode())

if p == '1':
    for i in range(int(n)+1):
        parcela = con.recv(7)
        print('parcela: ', parcela.decode())
        print(parcela,'\n')
        #valor = parcela.decode()
        valor = float(parcela.decode())
#        valor = parcela.decode('utf-8')
        lista.append(valor)
        print(lista, '\n')   
    print(f'O valor do cálculo de cada cliente é: {round(sum(lista), 4)}')
    print('Fechando a conexão')
    con.close()
    
if p == '2':
    for i in range(int(c)):
        parcela = con.recv(7)
        print('parcela: ', parcela.decode())
        valor = float(parcela.decode())
#        valor = parcela.decode('utf-8')
        lista.append(valor)
        print(lista, '\n')   
    print(f'O valor da soma de cada cliente é: {round(sum(lista), 4)}')
    print('Fechando a conexão')
    con.close()
    
#while True:
#    msg = input('digite: ')
#    if msg == 'fim'.upper():
#        con.close()
#        break
#    con.sendall(str.encode(msg))
#    msg = con.recv(1024)
#    print(msg.decode())