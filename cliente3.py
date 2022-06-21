from time import sleep
import socket
#import threading

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
print(p)
print(type(p))
n = int(n)
print(n)
print(type(n))
c = int(c)
print(c)
print(type(c))

#print(dir(cli.send(dir)))
        

if p == 1:
    soma_calculo = 0
    for i in range(n+1):
        calculo = ((-1)**i)/(2*i + 1)
        print(calculo)
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
            cli.sendall(str.encode(str(round(soma_calculo,4))))
            print(round(soma_calculo,4))
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
            print(round(soma_calculo,4))
            print(total-1)
            print('\n')
            cli.sendall(str.encode(str(round(soma_calculo,4))))
            break
        if supervisor == (a)//c:
            
            maximo += 1
            if maximo >= c:
                pass
            else:
                print('\n')
                print('enviando...')
                print(round(soma_calculo,4))
                print(total-1)
                print('\n')
                cli.sendall(str.encode(str(round(soma_calculo,4))))
                soma_calculo = 0
                supervisor = 0
                sleep(0.5)
        calculo = round(((-1)**total)/(2*total + 1), 4)
        soma_calculo += calculo
        print(round(soma_calculo,4))
        print(total)
        supervisor += 1
        total += 1
        
#while True:
#    msg = cli.recv(1024)
#    if not msg:
#        break
#    print(msg.decode())
#    msg = input('digite: ')
#    cli.sendall(str.encode(msg))