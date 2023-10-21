from tkinter import messagebox
import tkinter as tk
from GUI import menuprincipal,menuadm

def CheckaLogin(janela,usuario,senha):
   if usuario == "User"and senha == "1,2,3":
   	menuprincipal.menu(janela)
   elif usuario== "Admin" and senha== "102030":
   	menuadm.configuracoes(janela)
   else:
      return messagebox.showwarning(title= "Usuario nao existe", message= "Usuario ou Senha incorretos")


def teladelogin(janela):
	janela.destroy()
	login = tk.Tk()
	login.title("SDG-Tela De Login")
	login.geometry("700x500")
	tk.Label(login,text="Stopcar-SDG",background= "white",foreground= "#8c0000",font= "Arial 10").pack()
	bg= tk.PhotoImage(file= "Asset/ferrari.png")
	tk.Label(login,image= bg,background="white").pack()
	tk.Label(login,text="Digite seu nome de usuário:",background="white",foreground= "blue").pack()
	login["bg"]="white"
	user= tk.Entry(login)
	user.pack()
	tk.Label(login,text="Digite sua senha:",background="white",foreground= "blue").	pack()
	password = tk.Entry(login,show= '*')
	password.pack()
	confirm= tk.Button(login,text="Confirmar",background="#8c0000",foreground= "white",command= lambda:CheckaLogin(login,user.get(),password.get()),width="15",height="1").	pack(pady="10")
	login.mainloop()