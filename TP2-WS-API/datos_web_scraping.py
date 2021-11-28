#import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os


def obtener_datos():
    # indica la ruta
    url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
    id_table = 'ctl00_Contenido_tblAcciones'
    path = '~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/web_scraping.csv'
    page = requests.get(url_page).text 
    soup = BeautifulSoup(page, "lxml")

    # Obtenemos la tabla por un ID específico
    tabla = soup.find('table', attrs={'id': id_table})

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
    if os.path.exists(path):
        #print("che ya existo")
        os.remove(path)
        

    df["Max"] = df["Max"].str.replace(",", ".").astype(float)
    df["Min"] = df["Min"].str.replace(",", ".").astype(float)

    #Guardamos los datos en el archivo csv
    df.to_csv(path)
    