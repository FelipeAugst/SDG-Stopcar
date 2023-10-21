from GUI import menuprincipal,login
import tkinter as tk
class Inicializador:
	def __init__(self):
		pass
	def destroy(self):
		del self
		
start= Inicializador()
login.teladelogin(start)