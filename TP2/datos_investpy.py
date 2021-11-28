import investpy
import pandas as pd

def obtener_datos(acciones):
    path = '~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/investpy.csv'
    acclist = list()
    for ticker in acciones:
        df = investpy.get_stock_historical_data(stock=ticker,
                                        country='United States',
                                        from_date='01/11/2021',
                                        to_date='05/11/2021')
        df['Nombre'] = ticker
       # print(df.head())
        acclist.append(df)
        
    df = pd.concat(acclist)    
    df.to_csv(path)    