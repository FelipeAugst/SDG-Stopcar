import tkinter as tk
import regfrontend
import menuadm
from tkinter import messagebox
# função que verifica login
def CheckaLogin(janela,usuario,senha):
   if usuario == "Pitagoras" and senha == "Betim":
   	menu(janela)
   elif usuario== "Admin" and senha== "102030":
   	menuadm.configuracoes(janela)
   else:
      return messagebox.showwarning(title= "Usuario nao existe", message= "Usuario ou Senha incorretos")



def menu(janela):
 janela.destroy()
 menuprincipal= tk.Tk()
 menuprincipal.title("SDG-Menu Principal")
 menuprincipal["bg"]= "white"
 menuprincipal.geometry("700x500")
 tk.Label(menuprincipal,text= "Seja bem-vindo(a)! Escolha uma opção: ",     foreground= "#7c0000",background= "white").pack()
 bg= tk.PhotoImage(file= "mainrd.png")
 carromain=tk.Label(menuprincipal,image= bg,background="white").pack()

 entrada= tk.Button(menuprincipal, text= "Registrar Entrada", background=  "#8c0000", foreground="white", command= lambda: regfrontend.regentrada(menuprincipal)).pack()
 saida= tk.Button(menuprincipal,text= "Registrar Saída",background=  "#8c0000",foreground="white",command= lambda: regfrontend.regsaida(menuprincipal)).pack()
 voltar= tk.Button(menuprincipal,text="Voltar", bg="white",foreground= "blue",command= lambda: teladelogin(menuprincipal)).pack()
 sair= tk.Button(menuprincipal,text="Sair", bg="white",foreground= "blue",command= menuprincipal.destroy).pack()
 menuprincipal.mainloop()



def teladelogin(janela):
	janela.destroy()
	login = tk.Tk()
	login.title("SDG-Tela De Login")
	login.geometry("700x500")
	tk.Label(login,text="Stopcar-SDG",			background= "white",foreground= "#8c0000",font= "Arial 10").pack()
	bg= tk.PhotoImage(file= "ferrari.png")
	tk.Label(login,image= bg,				background="white").pack()
	tk.Label(login,text="Digite seu nome de usuário:",background="white",foreground= "blue").pack()
	login["bg"]="white"
	user= tk.Entry(login)
	user.pack()
	tk.Label(login,text="Digite sua senha:",	background="white",foreground= "blue").	pack()
	password = tk.Entry(login,show= '*')
	password.pack()
	confirm= tk.Button(login,			text="Confirmar",background="#8c0000",foreground= "white",command= lambda:		CheckaLogin(login,user.get(),password.get()),width="15",height="1").	pack(pady="10")
	login.mainloop()

