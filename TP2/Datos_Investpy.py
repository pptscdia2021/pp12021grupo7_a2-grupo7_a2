import investpy
import pandas as pd

def obtenerDatos(acciones):

    acclist = list()
    for ticker in acciones:
        df = investpy.get_stock_historical_data(stock=ticker,
                                        country='United States',
                                        from_date='01/01/2020',
                                        to_date='10/01/2020')
        df['Nombre'] = ticker
       # print(df.head())
        acclist.append(df)
        
    df = pd.concat(acclist)    
    df.to_csv('investpy.csv')    