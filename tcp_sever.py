import socket
from threading import Thread
from multiprocessing import Process
import time

def task(conn1, conn2):
    data = conn1.recv(1024)
    print(data)
    conn2.sendall(data)


host1 = '192.168.1.103'
port1 = 8080
host2 = '192.168.1.103'
port2 = 8081

sever1 = socket.socket()
sever1.bind((host1, port1))
sever1.listen(2)
sever2 = socket.socket()
sever2.bind((host2, port2))
sever2.listen(2)

conn1, addr1 = sever1.accept()
print('服务器已连接', conn1, addr1)
conn2, addr2 = sever2.accept()
print('服务器已连接', conn2, addr2)

while True:
    time.sleep(1)
    # Process(target=task, args=(conn1, conn2)).start()
    print('----')
    Thread(target=task, args=(conn1, conn2)).start()
    Thread(target=task, args=(conn2, conn1)).start()
    # Thread(target=task, args=(conn2, conn1))


conn1.close()
sever1.close()
conn2.close()
sever2.close()
print('链接已关闭')
