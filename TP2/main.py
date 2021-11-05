import obtenerDatos
import pandas as pd
import yahoofinance 
import Datos_Investpy

if __name__ == "__main__":
    
    #Obtener la tabla en tiempo real de la bolsa de españa    
    obtenerDatos.obtener_datos()
   
    #Mostrar tabla en pantalla usando BeautiFoul Soup
    print('')
    print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON WEB SCRAPING')
    print('')
    df_bolsaMadrid = pd.read_csv('bolsa_ibex35.csv')
    print(df_bolsaMadrid)

    #Método Yahoo Finance

    acciones = ["MELI", "DIS", "ADS.SG", "TSLA", "NFLX"]
    yahoofinance.ObtenerDatos(acciones)
    df_yahoofinance = pd.read_csv('Yahoo_finance.csv')
    print(df_yahoofinance)

    #Método Investpy

    acciones = ["MELI", "DIS", "TSLA", "NFLX"]
    Datos_Investpy.obtenerDatos(acciones)
    df_investpy = pd.read_csv('investpy.csv')
    print(df_investpy)