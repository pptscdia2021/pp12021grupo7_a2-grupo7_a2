import pandas as pd


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

