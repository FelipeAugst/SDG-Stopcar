
import datetime as dt
print()
data= input("Digite a data")
hora= input("Digite a hora")
formatdata= data.split("/")
formathora= hora.split(":")

data2= input("Digite a data")

hora2= input("Digite a hora")
formatdata2= data2.split("/")
formathora2= hora2.split(":")

entrada= dt.datetime(year= int(formatdata[0]),month= int(formatdata[1]),day=int(formatdata[2]),hour=int(formathora[0]),minute= int (formathora[1]),second= int(formathora[2]))

saida= dt.datetime(year= int(formatdata2[0]),month= int(formatdata2[1]), day= int(formatdata2[2]),hour= int(formathora2[0]),minute=int(formathora2[1]),second=int(formathora2[2]))

tdelta= saida-entrada
tempototal= float( tdelta.total_seconds()/3600 )
taxa= 0,5

if tempototal <= 1:
	print(tempototal*25.0)
else:
		taxa= float(tempototal-1)*25.5
		print(round(taxa,2)+25)
		
