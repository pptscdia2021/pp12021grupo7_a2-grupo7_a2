import yfinance as yf
import pandas as pd


def obtener_datos(acciones):
    path = '~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/Yahoo_finance.csv'
    acclist = list()
    for ticker in acciones:
        datos = yf.download(ticker, start="2021-11-01", end="2021-11-05",group_by="ticker")
        datos['Nombre'] = ticker
        acclist.append(datos)
    
    df = pd.concat(acclist)



    df.to_csv(path)