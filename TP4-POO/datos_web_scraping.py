from bs4.element import SoupStrainer
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import os

class Webscraping():

    def __init__(self, url, table, path_csv):
        self.url = url
        self.table_id = table
        self.path_csv = path_csv + "/web_scraping.csv"
        
    
    def obtener_datos(self):
        
        page = requests.get(self.url).text 
        soup = BeautifulSoup(page, "lxml")
        # Obtenemos la tabla por un ID específico
        tabla = soup.find('table', attrs={'id': self.table_id})

        name=""
        ult=""
        dif=""
        nroFila=0
        df = pd.DataFrame(columns=["Nombre" , "Ult", "Max", "Min", "Dif", "Fecha"])

        for fila in tabla.find_all("tr"):
            nroCelda=0
            for celda in fila.find_all('td'):
                if nroCelda==0:
                    name=celda.text
                    #print("Nombre:", name)
                if nroCelda==1:
                    ult=celda.text
                    #print("Ult:", ult)
                if nroCelda==2:
                    dif=celda.text
                    #print("Dif:", dif)
                if nroCelda==3:
                    max=celda.text
                    #print("Max:", max)
                if nroCelda==4:
                    min=celda.text
                    #print("Min:", min)
                nroCelda=nroCelda+1        
            nroFila=nroFila+1
            if nroFila>1:   
                df = df.append({'Nombre':name, 'Ult':ult, 'Dif':dif,'Max':max,'Min':min, 'Fecha': datetime.now()}, ignore_index=True)

        #chequeamos si el archivo csv existe. Si es asi se borra.
        if os.path.exists(self.path_csv):
            #print("che ya existo")
            os.remove(self.path_csv)
            

        df["Max"] = df["Max"].str.replace(",", ".").astype(float)
        df["Min"] = df["Min"].str.replace(",", ".").astype(float)

        #Guardamos los datos en el archivo csv
        df.to_csv(self.path_csv)
