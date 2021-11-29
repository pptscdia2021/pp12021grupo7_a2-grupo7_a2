import menu
import datos_web_scraping
import datos_investpy
import datos_yahoofinance
import maximo_minimo
from PIL import Image
import pandas as pd

if __name__ == "__main__":
    
    #Inicializacion de variables:    
    url = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'
    id_table = 'ctl00_Contenido_tblAcciones'
    path = '~/Escritorio/pp12021grupo7_a2-grupo7_a2/TP4-POO/archivos_csv'

    #datos investpy 
    acciones = ["MELI", "DIS", "TSLA", "NFLX"] 
    country='United States'
    from_date='01/11/2021'
    to_date='05/11/2021'
    
    # datos yahoo finance
    start= "2021-11-01"
    end = "2021-11-05"
            
    opcion = menu.Menu.show_menu()
    while opcion != 12:            
        if opcion == 1:
            datos = datos_web_scraping.Webscraping(url, id_table, path)
            datos_web_scraping.Webscraping.obtener_datos(datos)
        elif opcion == 2:
            datos1 = datos_yahoofinance.Yahoofinance(path, start, end, acciones)
            datos_yahoofinance.Yahoofinance.obtener_datos(datos1)
        elif opcion == 3:
            datos2 = datos_investpy.Investpy(path,country, from_date, to_date, acciones)
            datos_investpy.Investpy.obtener_datos(datos2)
        elif opcion == 4:
            print('')
            print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON WEB SCRAPING')
            print('')
            df_bolsaMadrid = pd.read_csv(path + '/web_scraping.csv')
            print(df_bolsaMadrid)
        elif opcion == 5:
            print('')
            print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON YAHOO FINANCE')
            print('')
            df_yahoofinance = pd.read_csv(path + '/yahoo_finance.csv')
            print(df_yahoofinance)
        elif opcion == 6:
            print('')
            print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON INVESTPY')
            print('')
            df_investpy = pd.read_csv(path + '/investpy.csv')
            print(df_investpy)
        elif opcion == 7:
            #Obtener maximo y minimo de las cotizaciones de WEB SCRAPING
            df_bolsaMadrid = pd.read_csv(path + '/web_scraping.csv')
            print('')
            maximo_minimo.Maximo_minimo.obtenerMaxMin(df_bolsaMadrid, by="web_scraping")
        elif opcion == 8:
            #Obtener maximo y minimo de las cotizaciones de YAHOO FINANCE
            df_yahoofinance = pd.read_csv(path + '/yahoo_finance.csv')
            print('')
            maximo_minimo.Maximo_minimo.obtenerMaxMin(df_yahoofinance, by="yahoo finance")
        elif opcion == 9:
            #Obtener maximo y minimo de las cotizaciones de INVESTPY
            df_investpy = pd.read_csv(path + '/investpy.csv')
            print('')
            maximo_minimo.Maximo_minimo.obtenerMaxMin(df_investpy, by="investpy")
        elif opcion == 10:
            ''' i = Image.open('/graficos/maximo_minimo_investpy','r')
            i.show() '''
            print ("Generar Graficos cotizaciones maximas y minimas")
        elif opcion == 11:
            print ("Graficar accion")
        elif opcion == 12:
            print ("salir")           
            
        opcion = menu.Menu.show_menu()