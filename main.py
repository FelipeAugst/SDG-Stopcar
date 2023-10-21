import teladelogin
import menuadm
import tkinter as tk
class Inicializador:
	def __init__(self):
		pass
	def destroy(self):
		del self
		
start= Inicializador()
teladelogin.teladelogin(start)