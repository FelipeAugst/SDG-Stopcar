import tkinter as tk
from tkinter import messagebox
import backend
import teladelogin
import regfrontend
import json
import vagasfunc


def alterapreco(janela):
	janela.destroy()
	altera= tk.Tk()
	altera["bg"]= "white"
	bg= tk.PhotoImage(file= "cooper2.png")
	carromain=tk.Label(altera,image= bg,background="white").pack()
	veiculo = tk.StringVar(altera)
	altera.title("Alterar preço")
	altera.geometry("700x500")
	im= tk.PhotoImage(file= "reg.png", master= altera)
	titulo= tk.Label(altera,text= "Escolha o tipo de veiculo:",background="white",foreground= "blue").pack()
	veiculos= tk.OptionMenu(altera,veiculo,"pequeno","medio","grande","moto","taxa","horasemtaxa").pack()
	preco = tk.Label(altera, text="Digite  o preco:", foreground="red",background="white").pack()
	entradapreco= tk.Entry(altera)
	entradapreco.pack()
	confirm = tk.Button(altera,  text="Confirmar", background="#0000ff",  foreground="white",command= lambda: precojson(veiculo.get(),entradapreco. get() ) ).pack()
	voltar= tk.Button(altera,text="Voltar", bg="white",foreground= "blue",command= lambda: configuracoes(altera)).pack()
	altera.mainloop()
  
def precojson(tipo,valor):
	if tipo== "" or valor == "":
		messagebox.showwarning(title= "Erro",message= "Valor invalido")
		return 0
	with open("tabela.json","r") as precos:
		importa= precos.read()
		tabela= json.loads(importa)
		tabela[tipo]= float(valor)
	with open("tabela.json","w") as precos:
		json.dump(tabela,precos)
		messagebox.showinfo(title= "Realizado com sucesso",message="Preco Alterado")
	
	
def teladecadastro(janela):
	janela.destroy()
	cadastro= tk.Tk()
	cadastro.geometry("700x500")
	cadastro.title("Cadastrar Usuário")
	cadastro["bg"]= "white"
	titulo= tk.Label(cadastro,text= "Cadastro De Usuarios",foreground="blue",	background= "white").pack()
	im= tk.PhotoImage(file="polo.png",			master= cadastro)
	image= tk.Label(cadastro,image=im,background= "white").pack()
	text1= tk.Label(cadastro,text= "Digite o nome de usuario",background="white",foreground= "red").pack()
	usuario= tk.Entry(cadastro).pack()
	text2= tk.Label(cadastro,text= "Digite a senha",background="white",foreground= "red").pack()
	senha1= tk.Entry(cadastro).pack()
	text3= tk.Label(cadastro,text= "Confirme a senha",background="white",foreground= "red").pack()
	senha2= tk.Entry(cadastro).pack()
	confirm = tk.Button(cadastro,  				text="Confirmar", background="#0000ff",  foreground="white" ).pack()
	voltar= tk.Button(cadastro,text="Voltar", bg="white",foreground= "blue",command= lambda: configuracoes(cadastro)).pack()
	cadastro.mainloop()
	     
	

def mostrarclientes(janela):
	janela.destroy()
	mostrar= tk.Tk()
	mostrar.geometry("700x500")
	mostrar.title("Clientes Cadastrados")
	with open("relatorio.json","r") as relatorios:
 		variaveljson= relatorios.read()
 		registros= json.loads(variaveljson)
 		texto= tk.Label(mostrar,text= registros,background= "white",					foreground= "blue")
 		t=tk.Text(mostrar,height=300,width= 300,bg= "white",fg= "blue")
 		t.pack()
 		texto.pack
 		t.insert(tk.END,registros)
 		mostrar.mainloop()
	
	
def configuracoes(janela):
	janela.destroy()
	config = tk.Tk()
	config.title("Configuracoes")
	config["bg"]= "white"
	config.geometry("700x500")  
	inicio=tk.Label(config,text= "Configurações",     foreground= "#0000ff", 	background= "white").pack()
	bg= tk.PhotoImage(master=config,file= "polo.png")
	carromain=tk.Label(config,image= bg,    	background="white").pack()
	registrarusuario= tk.Button(config, text= "Registrar Usuário", background=  "#0000ff", foreground="white",command= lambda: teladecadastro(config)).pack()
	alterarpreco= tk.Button(config,text= "Alterar Preços",background=  "#0000ff",		foreground="white",command= lambda: 	alterapreco(config)).pack()
	gerarrelatorio= tk.Button(config,text= "Mostrar Clientes",bg="blue",foreground= "white",command= lambda:  		mostrarclientes(config)).pack()
	resetdados= tk.Button(config,text= "Limpar Dados",background= "#0000ff",foreground= "white",command=vagasfunc.resetdados).pack()
	voltar= tk.Button(config,text="Voltar", bg="white",foreground= "blue",command= lambda: teladelogin.teladelogin(config)).pack()
	sair= tk.Button(config,text="Sair", bg="white",foreground= "blue",command= 	config.destroy).pack()
	config.mainloop()
  
  
  