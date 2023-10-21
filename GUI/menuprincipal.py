import tkinter as tk
from GUI import menuregistrar, menuadm,login
from tkinter import messagebox

def menu(janela):
 janela.destroy()
 menuprincipal= tk.Tk()
 menuprincipal.title("SDG-Menu Principal")
 menuprincipal["bg"]= "white"
 menuprincipal.geometry("700x500")
 tk.Label(menuprincipal,text= "Seja bem-vindo(a)! Escolha uma opção: ",foreground= "#7c0000",background= "white").pack()
 bg= tk.PhotoImage(file= "Asset/mainrd.png")
 carromain=tk.Label(menuprincipal,image= bg,background="white").pack()

 entrada= tk.Button(menuprincipal, text= "Registrar Entrada", background=  "#8c0000", foreground="white", command= lambda: menuregistrar.regentrada(menuprincipal)).pack()
 saida= tk.Button(menuprincipal,text= "Registrar Saída",background=  "#8c0000",foreground="white",command= lambda: menuregistrar.regsaida(menuprincipal)).pack()
 clientes= tk.Button(menuprincipal,text= "Mostrar Clientes",background=  "#8c0000",foreground="white",command= lambda: mostrarclientes(menuprincipal)).pack()
 voltar= tk.Button(menuprincipal,text="Voltar", bg="white",foreground= "blue",command= lambda: login.teladelogin(menuprincipal)).pack()
 sair= tk.Button(menuprincipal,text="Sair", bg="white",foreground= "blue",command= menuprincipal.destroy).pack()
 menuprincipal.mainloop()


def mostrarclientes(janela):
	janela.destroy()
	mostrar= tk.Tk()
	mostrar.geometry("700x500")
	mostrar.title("Clientes Cadastrados")
	with open("relatorio.json","r") as relatorios:
		variaveljson= relatorios.read()
		registros= json.loads(variaveljson)
		texto= tk.Label(mostrar,text= registros,background= "white",     foreground= "blue")
		t=tk.Text(mostrar,height=300,width= 300,bg= "white",fg= "blue")
		t.pack()
		texto.pack
		t.insert(tk.END,registros)
		voltar= tk.Button(mostrarclientes,text="Voltar", bg="white",foreground= "blue",command= lambda: menu(mostrar)).pack()
		mostrar.mainloop()