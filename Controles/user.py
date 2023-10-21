import tkinter as tk
from tkinter import messagebox
import json


with open("databaseusers.json","w") as users:
	listauser= {}
	listauser['adm']= {}
	listauser['colaboradorew']={}
	listauser['adm']['user']= "Albano"
	listauser['adm']['password']= "102030"
	json.dump(listauser,users)
	