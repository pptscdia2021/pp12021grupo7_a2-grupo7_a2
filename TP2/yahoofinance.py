import yfinance as yf
import pandas as pd


def ObtenerDatos(acciones):
    acclist = list()
    for ticker in acciones:
        datos = yf.download(ticker, start="2021-11-01", end="2021-11-05",group_by="ticker")
        datos['Nombre'] = ticker
        acclist.append(datos)
    
    df = pd.concat(acclist)



    df.to_csv('Yahoo_finance.csv')