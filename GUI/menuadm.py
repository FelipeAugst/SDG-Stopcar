import tkinter as tk
from tkinter import messagebox
import Controles.registrador as registrador
from GUI import menuprincipal,menuregistrar,login
import json
import Controles.vagas as vagas



def alterapreco(janela):
	janela.destroy()
	altera= tk.Tk()
	altera["bg"]= "white"
	bg= tk.PhotoImage(file= "Asset/polo2.png")
	carromain=tk.Label(altera,image= bg,background="white").pack()
	veiculo = tk.StringVar(altera)
	altera.title("Alterar preço")
	altera.geometry("900x700")
	#im= tk.PhotoImage(file= "reg.png", master= altera)
	titulo= tk.Label(altera,text= "Escolha o tipo de veiculo:",background="white",foreground= "blue").pack()
	veiculos= tk.OptionMenu(altera,veiculo,"pequeno","medio","grande","moto","taxa","horasemtaxa").pack()
	preco = tk.Label(altera, text="Digite  o preco:", foreground="red",background="white").pack()
	entradapreco= tk.Entry(altera)
	entradapreco.pack()
	confirm = tk.Button(altera,  text="Confirmar", background="#0000ff",  foreground="white",command= lambda: registrador.precojson(veiculo.get(),entradapreco. get() ) ).pack()
	voltar= tk.Button(altera,text="Voltar", bg="white",foreground= "blue",command= lambda: configuracoes(altera)).pack()
	altera.mainloop()
  

	
	
def teladecadastro(janela):
	janela.destroy()
	cadastro= tk.Tk()
	cadastro.geometry("900x700")
	cadastro.title("Cadastrar Usuário")
	cadastro["bg"]= "white"
	titulo= tk.Label(cadastro,text= "Cadastro De Usuarios",foreground="blue",	background= "white").pack()
	im= tk.PhotoImage(file="Asset/polo.png",master= cadastro)
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
	     
	

def configuracoes(janela):
	janela.destroy()
	config = tk.Tk()
	config.title("Configuracoes")
	config["bg"]= "white"
	config.geometry("900x700")  
	inicio=tk.Label(config,text= "Configurações",     foreground= "#0000ff", 	background= "white").pack()
	bg= tk.PhotoImage(master=config,file= "Asset/polo.png")
	carromain=tk.Label(config,image= bg,    	background="white").pack()
	registrarusuario= tk.Button(config, text= "Registrar Usuário", background=  "#0000ff", foreground="white",command= lambda: teladecadastro(config)).pack()
	alterarpreco= tk.Button(config,text= "Alterar Preços",background=  "#0000ff",		foreground="white",command= lambda: 	alterapreco(config)).pack()
	resetdados= tk.Button(config,text= "Limpar Dados",background= "#0000ff",foreground= "white",command=vagas.resetdados).pack()
	voltar= tk.Button(config,text="Voltar", bg="white",foreground= "blue",command= lambda: login.teladelogin(config)).pack()
	sair= tk.Button(config,text="Sair", bg="white",foreground= "blue",command= 	config.destroy).pack()
	config.mainloop()
  
  
  