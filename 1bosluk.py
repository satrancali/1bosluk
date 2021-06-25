#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
import codecs
import time

os.system("apt install sublist3r")
os.system("clear")

gelenDomain = input("Enter domain example: example.com\n")

liste=[]
#komut = "rm -r Results/"+gelenDomain
#w = os.system(komut)
komut = "mkdir -p Results/"+gelenDomain
os.system(komut)
dosyaYolu = "Results/"+gelenDomain+"/"+gelenDomain
file = codecs.open(dosyaYolu+"_subdomains.txt", "a", "utf-8")
file2 = codecs.open(dosyaYolu+"_ip.txt", "a", "utf-8")
komut = "sublist3r -d "+gelenDomain
output = os.popen(komut).read()
print("DENEME")
a = output.split("\n")
for b in a:
	b = b.replace("\x1b[92ma","")
	b = b.replace("\x1b[0m","")
	b = b.replace("[92m","")
	if gelenDomain in b:
		if " " in b:
			continue
		file.write(b+"\n")
		print(b)
		IPBulmaKomutu = "host "+b
		outputIP = os.popen(IPBulmaKomutu).read()
		if "has address" in outputIP:
			ipVar = outputIP.split("has address ")
			#print(ipVar[1])
			liste.append(ipVar[1].replace("\n",""))
#print(liste)
liste =  set(liste)
#print(liste)
for c in liste:
	print(c)
	file2.write(c+"\n")
		#print(outputIP)

onlineSubdomains = codecs.open(dosyaYolu+"_onlineSubDomains.txt", "a", "utf-8")
f = open(dosyaYolu+"_subdomains.txt", "r")
hepsi = f.readlines()
for a in hepsi:
	siteAdresi = a.replace("\n","")
	#print(siteAdresi)
	komut = "host "+siteAdresi
	heyyo = os.popen(komut).read()
	if heyyo.find("has address") != -1:
		print(siteAdresi)
		onlineSubdomains.write(c + "\n")

#for c in liste:
#	komut = "nmap "+c+" --script=vulners.nse -sV"
#	print(komut)
#	nmapSonucu = os.popen(komut).read()
#	file3.write(nmapSonucu+"\n")
#komut = "nmap -n -iL "+dosyaYolu+"_ip.txt --script=vulners.nse -sV --append-output "+dosyaYolu+"_nmap.txt"
#print(komut)
#os.system(komut)