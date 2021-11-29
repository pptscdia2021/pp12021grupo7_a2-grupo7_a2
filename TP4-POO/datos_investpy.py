import investpy
import pandas as pd

class Investpy():
    
    def __init__(self,path_csv, country, from_date, to_date, acciones ):
        self.path_csv = path_csv + "/investpy.csv"
        self.country = country
        self.from_date = from_date
        self.to_date = to_date
        self.acciones = acciones
    
    def obtener_datos(self):
        acclist = list()
        for ticker in self.acciones:
            df = investpy.get_stock_historical_data(stock=ticker,
                                            country='United States',
                                            from_date='01/11/2021',
                                            to_date='05/11/2021')
            df['Nombre'] = ticker
        # print(df.head())
            acclist.append(df)
            
        df = pd.concat(acclist)    
        df.to_csv(self.path_csv)   