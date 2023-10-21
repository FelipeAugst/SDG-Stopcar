import tkinter as tk
from GUI import menuregistrar, menuadm,login
from tkinter import messagebox,Text
import json

def menu(janela):
 janela.destroy()
 menuprincipal= tk.Tk()
 menuprincipal.title("SDG-Menu Principal")
 menuprincipal["bg"]= "white"
 menuprincipal.geometry("900x700")
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
	line= 1.0
	janela.destroy()
	mostrar= tk.Tk()
	mostrar.geometry("900x700")
	mostrar.title("Clientes Cadastrados")
	with open("Databases/relatorio.json","r") as relatorios:
		variaveljson= relatorios.read()
		registros= json.loads(variaveljson)
		t=Text(mostrar,height=350,width= 350,bg= "white",fg= "blue")
		for key,value in registros.items():
			t.insert(tk.END,
			"Nome:"+key+"\n",
			"Placa:"+value['placa']+"\n",
			"Data/Hora de Entrada:"+value['dataentrada']+'-'+value['horaentrada']+"\n",
			"Data/Hora de Saida:"+value['datasaida']+'-'+value['horasaida']+"\n",
			"Tipo de Veiculo:"+value['veiculo']+
			"| Preco:"+str(value['preco'])+"\n")
			print(type(value['dataentrada']),type(key))
	voltar= tk.Button(mostrar,text="Voltar", bg="white",foreground= "blue",command= lambda: menu(mostrar)).pack()
	t.pack()
	mostrar.mainloop()