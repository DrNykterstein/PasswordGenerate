#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importo el paquete random, para poder usar su modulo choice para no tener que usar random.choice
from random import choice
#Importo el paquete string, para poder usar los modulos ascii_letters y digits normalmente.No tener que estar haciendo string.ascii_letters
from string import ascii_letters, digits
import os
import hashlib
import os

def limpiar():
	try:
		os.system('clear')
	except:
		os.system('cls')

def mensaje():
	print" "
	print " ############################################################################## "
	print " ####### 00000   0     0000  0000  00 00 00  000000  000000  00000000   #######"
	print " ####### 00000  0 0    00    00    00 00 00  00  00  00  00  000     00  ######"
	print " ####### 00000 00000   0000  0000  00 00 00  00  00  000000  000     00 #######"
	print " ####### 00   0     0    00    00  00 00 00  00  00  00  00  000    00 ########"
	print " ####### 00  0       0 0000  0000  00000000  000000  00  00  0000000 ##########"
	print " ##############################################################################"

def menu():
	print "1- cifrar" 
	print "2- Generar contraseña (aleaotoria)"

def generarhash(mensaje):
	mensaje = hashlib.sha256(mensaje).hexdigest()
	return mensaje
	
def comparar(password,mensaje):
	return password == hashlib.sha256(mensaje).hexdigest()
	
def funcionhash():
	while True:
		limpiar()
		palabra = raw_input("Introduce el mensaje a cifrar: ")
		hashpassword=generarhash(palabra)
		print hashpassword
		password = raw_input("\nIntroduzca de nuevo el mensaje a cifrar: ")
		if comparar(hashpassword,password):
			print "\nEs correcto, debe recordar el mensaje"
		else:
			print "\nLo sentimos , clave incorrecto"
		
		print "\nDesea volver a cifrar un mensaje (s/n) "
		x = raw_input("? ")
		if (x == 'n' or x =='N'):
			break
			
def claved():
	while True:
		longitud = raw_input("Longitud de la clave que se desea creear: ")
		longitud = int(longitud)
		numero = raw_input("Cuantas password desea crear: ")
		numero = int(numero)
			
		caracteres = ascii_letters + digits
		def clave(x):
			for i in range(x):
				final = ''.join([choice(caracteres) for i in range(longitud)])
				print final
					
		clave(numero)
		op=raw_input("Desea generar otros password (s/n): ")
		if (op == 'n' or op == 'N'):
			break
	
def main():
	while True:
		limpiar()
		mensaje()
		menu()
		op = raw_input("? ")
		op = int(op)
		if (op == 1):
			funcionhash()
		if (op == 2):
			claved()
		limpiar()
		d = raw_input("Desea realiza otra operacion (s/n): ")
		if(d == 'n' or d == 'N'):
			break
			
	limpiar()
	
main()
