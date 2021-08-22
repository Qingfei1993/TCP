import socket
from threading import Thread


def recive_task(client):
    recive_data = client.recv(1024).decode()
    print('虎跑调：%s' % recive_data)


# 兔任性
host = '192.168.1.103'
port = 8081

client = socket.socket()
client.connect((host, port))
print('服务器已连接')

while True:
    # Thread(target=send_task, args=(client, )).start()
    Thread(target=recive_task, args=(client, )).start()
    send_data = input('我:')
    client.send(send_data.encode())

client.close()
print('连接已关闭')
