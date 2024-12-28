from socket import socket

with open("request.txt", "rb") as fp:
    data = fp.read()

print("here 1")
sock = socket()
print("here 2")
sock.connect(("httpbin.org", 80))
sock.sendall(data)
print("here 3")

chunks = []
for chunk in iter(lambda: sock.recv(1024), b""):
    chunks.append(chunk)
    print("here 4")
reply = b"".join(chunks)
print("here 5")
print(reply.decode())
print("here 6")
