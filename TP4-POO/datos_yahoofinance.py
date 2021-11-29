import yfinance as yf
import pandas as pd

class Yahoofinance():
    
    def __init__(self,path_csv, from_date, to_date, acciones ):
        self.path_csv = path_csv + "/yahoo_finance.csv"
        self.from_date = from_date
        self.to_date = to_date
        self.acciones = acciones
        
    def obtener_datos(self):
        acclist = list()
        for ticker in self.acciones:
            datos = yf.download(ticker, start=self.from_date, end=self.to_date,group_by="ticker")
            datos['Nombre'] = ticker
            acclist.append(datos)
        
        df = pd.concat(acclist)

        df.to_csv(self.path_csv)