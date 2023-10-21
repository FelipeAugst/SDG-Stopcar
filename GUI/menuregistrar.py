import tkinter as tk

import Controles.registrador as registrador
from GUI import menuprincipal





def regentrada(janela):
  janela.destroy()
  janelain= tk.Tk()
  veiculo = tk.StringVar(janelain)
  janelain.title("Registrar Entrada")
  janelain.geometry("700x500")
  im= tk.PhotoImage(file= "reg.png",master= janelain)
  foto= tk.Label(janelain,image=im).pack()
  texto1= tk.Label(janelain,text="Digite  o nome do cliente",foreground="blue").pack()
  entradacliente= tk.Entry(janelain)
  entradacliente.pack()
  texto2 = tk.Label(janelain, text="Digite  a placa do veículo:", foreground="blue").pack()
  entradaplaca= tk.Entry(janelain)
  entradaplaca.pack()
  texto3 = tk.Label(janelain, text="Digite  a data:", foreground="blue").pack()
  entradadata = tk.Entry(janelain)
  entradadata.pack()
  texto4 = tk.Label(janelain, text="Digite  o horário:", foreground="blue").pack()
  entradahorario = tk.Entry(janelain)
  entradahorario.pack()
  veiculos= tk.OptionMenu(janelain,veiculo,"pequeno","medio","grande","moto").pack()

  confirm = tk.Button(janelain, text="Confirmar", background="#8c0000", foreground="white",command= lambda: registrador.entrada(  entradacliente.get(),
  entradaplaca.get(),entradadata.get(),
 entradahorario.get(),veiculo.get()) )
  confirm.pack()
  voltar= tk.Button(janelain,text="Voltar", bg="white",foreground= "blue",command= lambda: menuprincipal.menu(janelain)).pack()
  janelain.mainloop()


def regsaida(janela):
  janela.destroy()
  janelain= tk.Tk()
  veiculo = tk.StringVar(janelain)
  janelain.title("Registrar Saida")
  janelain.geometry("700x500")
  im= tk.PhotoImage(file= "reg.png",master= janelain)
  foto= tk.Label(janelain,image=im).pack()
  texto1= tk.Label(janelain,text="Digite  o nome do cliente",foreground="blue").pack()
  saidacliente= tk.Entry(janelain)
  saidacliente.pack()
  texto2 = tk.Label(janelain, text="Digite  a placa do veículo:", foreground="blue").pack()
  saidaplaca= tk.Entry(janelain)
  saidaplaca.pack()
  texto3 = tk.Label(janelain, text="Digite  a data:", foreground="blue").pack()
  saidadata = tk.Entry(janelain)
  saidadata.pack()
  saidadata.insert(0,"")
  texto4 = tk.Label(janelain, text="Digite  o horário:", foreground="blue").pack()
  saidahorario = tk.Entry(janelain)
  saidahorario.pack()
  saidahorario.insert(0,"")
  confirm = tk.Button(janelain, text="Confirmar", background="#8c0000", foreground="white",command= lambda: registrador.saida(saidacliente.get(),
  saidaplaca.get(),saidadata.get(),
 saidahorario.get()) )
  confirm.pack()
  voltar= tk.Button(janelain,text="Voltar", bg="white",foreground= "blue",command= lambda: menuprincipal.menu(janelain)).pack()
  janelain.mainloop()



