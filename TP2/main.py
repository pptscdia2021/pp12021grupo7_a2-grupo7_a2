import datos_web_scraping
import datos_yahoofinance
import datos_investpy
import maximo_minimo
import pandas as pd

if __name__ == "__main__":
    
    #Metodo Web Scraping   
    datos_web_scraping.obtener_datos()
    print('')
    print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON WEB SCRAPING')
    print('')
    df_bolsaMadrid = pd.read_csv('~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/web_scraping.csv')
    print(df_bolsaMadrid)

    #Método Yahoo Finance
    acciones = ["MELI", "DIS", "TSLA", "NFLX"]
    datos_yahoofinance.obtener_datos(acciones)
    df_yahoofinance = pd.read_csv('~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/Yahoo_finance.csv')
    print('')
    print('IMPRIMIENDO TABLA DE DATOS CON YAHOO FINANCE')
    print('')
    print(df_yahoofinance)

    #Método Investpy
    acciones = ["MELI", "DIS", "TSLA", "NFLX"]
    datos_investpy.obtener_datos(acciones)
    df_investpy = pd.read_csv('~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP2/archivos_csv/investpy.csv')
    print('')
    print('IMPRIMIENDO TABLA DE DATOS CON INVESTPY')
    print('')
    print(df_investpy)

    #Obtener maximo y minimo de las cotizaciones de YAHOO FINANCE
    print('')
    maximo_minimo.obtenerMaxMin(df_yahoofinance, by="yahoo finance")
    #Obtener maximo y minimo de las cotizaciones de INVESTPY
    print('')
    maximo_minimo.obtenerMaxMin(df_investpy, by="investpy")
    #Obtener maximo y minimo de las cotizaciones de WEB SCRAPING
    print('')
    maximo_minimo.obtenerMaxMin(df_bolsaMadrid, by="web_scraping")


    