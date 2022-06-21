from time import sleep
import socket

host = socket.gethostname()
port = 55551
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli.connect((host, port))
soma = 0

p = cli.recv(8)
print('p é: ', p.decode())
cli.sendall(str.encode('Recebido o valor de p!'))

n = cli.recv(8)
print('n é: ', n.decode())
cli.sendall(str.encode('Recebido o valor de n!'))

c = cli.recv(8)
print('c é: ', c.decode())
cli.sendall(str.encode('Recebido o valor de c!'))


p = int(p)

n = int(n)

c = int(c)
        

if p == 1:
    soma_calculo = 0
    for i in range(n+1):
        calculo = ((-1)**i)/(2*i + 1)
        print('\n')
        print('enviando...')
        cli.sendall(str.encode(str(round(calculo, 4))))
        sleep(0.5)
        

a = n + 1
supervisor = 0
total = 0
soma_calculo = 0

if p == 2 and ((a)%c) == 0:
   while True:
        if supervisor == int((a)/c):
            supervisor = 0
            print('\n')
            print('enviando...')
            cli.sendall(str.encode(str(round(soma_calculo,4))))
            soma_calculo = 0
            sleep(0.5)
        if total == a:
            break
        calculo = ((-1)**total)/(2*total + 1)
        soma_calculo += calculo
        supervisor += 1
        total += 1

supervisor = 0
total = 0
soma_calculo = 0
maximo = 0

if p == 2 and ((a)%c) != 0:
    while True:
        if total == a:
            print('\n')
            print('enviando...')
            cli.sendall(str.encode(str(round(soma_calculo,4))))
            break
        if supervisor == (a)//c:
            
            maximo += 1
            if maximo >= c:
                pass
            else:
                print('\n')
                print('enviando...')
                cli.sendall(str.encode(str(round(soma_calculo,4))))
                soma_calculo = 0
                supervisor = 0
                sleep(0.5)
        calculo = round(((-1)**total)/(2*total + 1), 4)
        soma_calculo += calculo
        supervisor += 1
        total += 1
