import json
from tkinter import messagebox
import vagasfunc


def entrada(nome= None,placa=None,data="",hora= "" ,veiculo= None):
  with open("relatorio.json","r") as relatorio:
      Registro =  relatorio.read()
      Cadastro= json.loads(Registro)
  if veiculo == "" or nome == "" or placa== "" or data == "" or hora== "" :
  	return messagebox.showwarning(title="Erro", message= "informe todos os dados")
  elif vagasfunc.ocupavaga(veiculo)==0:
  	return 0

  Cadastro[nome]=  {}
  Cadastro[nome]['placa']= placa
  Cadastro[nome]['dataentrada']= data
  Cadastro[nome]['horaentrada']=hora
  Cadastro[nome]['veiculo']= veiculo
  Cadastro[nome]['datasaida']= '-'
  Cadastro[nome]['horasaida'] = '-'
  Cadastro[nome]['preço']= 0.0
  Cadastro[nome]['vaga']= vagasfunc.ocupavaga(veiculo)
  with open("relatorio.json","w") as outfile:
       json.dump(Cadastro,outfile)
  return messagebox.showinfo(title= "Confirmação",message= "Registrado com sucesso")


def saida(nome:str,placa:str,data:str,hora:str):
  with open("relatorio.json","r") as regs:
  	lista= regs.read()
  	registros= json.loads(lista)
  if not nome in registros or not placa in registros[nome]['placa'] or data=="" or hora=="":
  	return messagebox.showwarning(title="Erro",message= "Cliente inexistetente/Informe corretamente os dados")
  registros[nome]['datasaida']= data
  registros[nome]['horasaida']= hora
  registros[nome]['preço']= vagasfunc.calculapreco(registros[nome]['veiculo'],registros[nome]['dataentrada'],registros[nome]['horaentrada'],data,hora) 
  if registros[nome]['preço']== 0:
  	return 0
  vagasfunc.liberavaga(registros[nome]['vaga'],registros[nome]['veiculo'] )
  with open("relatorio.json","w") as outfile:
       json.dump(registros,outfile)
       return messagebox.showinfo(title= "Confirmação",message= "Registrado com sucesso") 


		