import usocket as socket

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
counter=0

while True:
    res = s.accept()
    client_s = res[0]
    client_addr = res[1]
    print("Client address:", client_addr)
    print("Client socket:", client_s)
    print("Request:")
    req = client_s.recv(4096)
    print(req)
    client_s.send(bytes(CONTENT.format(counter), "utf-8"))
    client_s.close()
    #parts = req.decode('ascii').split(' ')
    #if parts[1] == '/exit':
    #  break
    counter += 1
