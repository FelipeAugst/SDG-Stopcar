import json
from tkinter import messagebox
from Controles import vagas as vagas


def entrada(nome= None,placa=None,data="",hora= "" ,veiculo= None):
  with open("Databases/relatorio.json","r") as relatorio:
      Registro =  relatorio.read()
      Cadastro= json.loads(Registro)
  if veiculo == "" or nome == "" or placa== "" or data == "" or hora== "" :
  	return messagebox.showwarning(title="Erro", message= "informe todos os dados")
  elif vagas.ocupavaga(veiculo)==0:
  	return 0

  Cadastro[nome]=  {}
  Cadastro[nome]['placa']= placa
  Cadastro[nome]['dataentrada']= data
  Cadastro[nome]['horaentrada']=hora
  Cadastro[nome]['veiculo']= veiculo
  Cadastro[nome]['datasaida']= '-'
  Cadastro[nome]['horasaida'] = '-'
  Cadastro[nome]['preço']= 0.0
  Cadastro[nome]['vaga']= vagas.ocupavaga(veiculo)
  with open("Databases/relatorio.json","w") as outfile:
       json.dump(Cadastro,outfile)
  return messagebox.showinfo(title= "Confirmação",message= "Registrado com sucesso")


def saida(nome:str,placa:str,data:str,hora:str):
  with open("Databases/relatorio.json","r") as regs:
    lista= regs.read()
    registros= json.loads(lista)
  if not nome in registros or not placa in registros[nome]['placa'] or data=="" or hora=="":
  	return messagebox.showwarning(title="Erro",message= "Cliente inexistetente/Informe corretamente os dados")
  registros[nome]['datasaida']= data
  registros[nome]['horasaida']= hora
  registros[nome]['preço']= vagas.calculapreco(registros[nome]['veiculo'],registros[nome]['dataentrada'],registros[nome]['horaentrada'],data,hora) 
  if registros[nome]['preço']== 0:
  	return 0
  vagas.liberavaga(registros[nome]['vaga'],registros[nome]['veiculo'] )
  with open("Databases/relatorio.json","w") as outfile:
       json.dump(registros,outfile)
       return messagebox.showinfo(title= "Confirmação",message= "Registrado com sucesso") 


def precojson(tipo:str,valor:str):
  if tipo== "" or valor == "":
    messagebox.showwarning(title= "Erro",message= "Valor invalido")
    return 0
  with open("Databases/tabela.json","r") as precos:
    tab_preco= precos.read()
    tabela= json.loads(tab_preco)
    tabela[tipo]= float(valor)
  with open("Databases/tabela.json","w") as precos:
    json.dump(tabela,precos)
  messagebox.showinfo(title= "Realizado com sucesso",message="Preco Alterado")