import yfinance as yf
import pandas as pd


def ObtenerDatos(acciones):
    acclist = list()
    for ticker in acciones:
        datos = yf.download(ticker, start="2021-10-20", end="2021-10-21",group_by="ticker")
        datos['Nombre'] = ticker
        acclist.append(datos)
    
    df = pd.concat(acclist)



    df.to_csv('Yahoo_finance.csv')