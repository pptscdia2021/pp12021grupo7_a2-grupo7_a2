import pandas as pd
import matplotlib.pyplot as plt
class Maximo_minimo():

    def obtenerMaxMin(df,by):
        print("OBTENIENDO COTIZACION MAXIMA Y MINIMA DE: ",by)
        if by != "web_scraping":
            maxi = df["High"].max()
            mini = df["Low"].min()
            idmax = df["High"].idxmax()
            idmin = df["Low"].idxmin()
        else:
            maxi = df["Max"].max()
            mini = df["Min"].min()
            idmax = df["Max"].idxmax()
            idmin = df["Min"].idxmin()
        max = round(maxi, 2)
        max_accion = (df.iloc[idmax]['Nombre'])
        min = round(mini, 2)
        min_accion = (df.iloc[idmin]['Nombre'])
        print("Cotizacion Máxima: ", max, "corresponde a: ",max_accion)
        print("Cotizacion mínima: ", min, "corresponde a :", min_accion)

        
        plt.style.use('Solarize_Light2')
        fig, ax = plt.subplots()
        #fig.set_size_inches(7,12)
        ax.bar(max_accion, max, label ='Valor máximo', color="#04D8B2")
        ax.bar(min_accion, min, label ='Valor mínimo', linestyle = 'dashed', color="#FA8072")
        ax.set_title('Grafico', loc = "left", fontdict = {'fontsize':12, 'fontweight':'bold', 'color':'tab:blue'})
        plt.legend() 
        plt.savefig('nombre', bbox_inches='tight')
        plt.tight_layout();plt.show()
        return
