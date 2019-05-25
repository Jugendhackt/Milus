import usocket as socket
import control

CONTENT = """\
HTTP/1.0 200 OK

"""
file = open("index.html","r")
CONTENT += file.read()

ai = socket.getaddrinfo("192.168.4.1",8080)
addr = ai[0][4]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)

while True:
    res = s.accept()
    client_s = res[0]
    client_addr = res[1]
    print("Client address:", client_addr)
    print("Client socket:", client_s)
    print("Request:")
    req = client_s.recv(4096)
    print(req)
    parts = req.decode('ascii').split(' ')
    if parts[1] == '/control':
        client_s.close()
        values = req.decode('ascii').split('dataforcontrol')[1].split(',')
        control.move(int(values[0]),int(values[1]),int(values[2]))
        continue
    client_s.send(bytes(CONTENT, "utf-8"))
    client_s.close()
  