import obtenerDatos
import pandas as pd

if __name__ == "__main__":
    
    #Obtener la tabla en tiempo real de la bolsa de españa    
    obtenerDatos.obtener_datos()
   
    #Mostrar tabla en pantalla usando BeautiFoul Soup
    print('')
    print('IMPRIMIENDO TABLA DE DATOS BOLSA DE MADRID CON WEB SCRAPING')
    print('')
    df_bolsaMadrid = pd.read_csv('bolsa_ibex35.csv')
    print(df_bolsaMadrid)