from socket import * 

s = socket(AF_INET,SOCK_STREAM)

s.bind(("192.168.1.110",3456))

s.listen(1)
print("Sunucu Aktif.")
con,addr = s.accept()

print("Bağlantı Aktif.")

while True:
	data = con.recv(2048).decode("utf-8")
	print(data)
