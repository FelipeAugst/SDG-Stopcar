import json
from tkinter import messagebox
import datetime as dt
def ocupavaga(porte= None):
	with open("Databases/vagas.json","r") as vagas:
		vagasdisponiveis= vagas.read()
	listavagas= json.loads(vagasdisponiveis)
	if not porte in listavagas:
		return 0
	if len(listavagas[porte])==0:
		messagebox.showwarning(title= "Erro",message="Vagas indisponíveis para esta categoria")
		return 0
	else:
		a= listavagas[porte][0]
		listavagas[porte].pop(0)
		with open("Databases/vagas.json","w") as vagasrestantes:
			json.dump(listavagas,vagasrestantes)
		return a
		
		
def liberavaga(vaga,porte):
	with open("Databases/vagas.json","r") as vagas:
		vagasdisponiveis= vagas.read()
	listavagas= json.loads(vagasdisponiveis)
	listavagas[porte].append(vaga)
	listavagas[porte].sort()
	with open("Databases/vagas.json","w") as vagas:
		json.dump(listavagas,vagas)
		
def resetvagas():		
	with open("Databases/vagas.json","w") as modelo:
		listavagas= {}
		listavagas["pequeno"]= [x for x in 				range(1,26)]
		listavagas["medio"]= [x for x in range(1,26)]
		listavagas["grande"]= [x for x in range(1,26)]
		listavagas["moto"]= [x for x in range(1,26)]
		json.dump(listavagas,modelo)
		
def resetdados():
		answer= messagebox.askyesno(title= "Confirmar",message= "Apagar todos os dados")
		if not answer:
			return 0
		resetvagas()
		with open("Databases/relatorio.json","w") as relatorio:
			reseta= {}
			json.dump(reseta,relatorio)
			messagebox.showinfo(title="Resetado com sucesso",message= "Dados Apagados")


def calculapreco(porte,data,hora,data2,hora2):
	with open("Databases/tabela.json","r") as tabela:
		temp= tabela.read()
		preco= json.loads(temp)
	formatdata= data.split("/")
	formathora= hora.split(":")
	formatdata2= data2.split("/")
	formathora2= hora2.split(":")
	entrada= dt.datetime(year= 		int(formatdata[2]),month= int(formatdata[1]),day=int(formatdata[0]),hour=int(formathora[0]),minute= int (formathora[1]),second= 0)
	saida= dt.datetime(year= int(formatdata2[2]),month= int(formatdata2[1]), day= int(formatdata2[0]),hour= int(formathora2[0]),minute=int(formathora2[1]),second=0)
	tdelta= saida-entrada
	if tdelta.total_seconds() <= 0:
		messagebox.showwarning(title= "Erro",message= "Intervalo de tempo invalido")
		return 0
	tempototal= (tdelta.total_seconds()/3600)
	if tempototal <= preco['horasemtaxa']:
		preco= tempototal* preco[porte]
		return round(preco,2)
	else:
		taxa= (tempototal- preco['horasemtaxa'])*(preco[porte]+preco['taxa'])
		preco= taxa+(preco[porte]*preco['horasemtaxa'])
		return round(preco,2)

