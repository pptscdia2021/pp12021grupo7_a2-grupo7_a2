class Menu:
        
    def show_menu():
        print('*** Menu ***')
        print('1) Obtener datos a travez de WEB-SCRAPING')
        print('2) Obtener datos a travez de YAHOO FINANCE')
        print('3) Obtener datos a travez de INVESTPY')
        print('4) Mostrar datos WEB-SCRAPING')
        print('5) Mostrar datos YAHOO FINANCE')
        print('6) Mostrar datos INVESTPY')
        print('7) Obtener cotizacion maxima y minima de WEB-SCRAPING')
        print('8) Obtener cotizacion maxima y minima de YAHOO FINANCE')
        print('9) Obtener cotizacion maxima y minima de INVESTPY')
        print('10) Graficar cotizaciones maximas y minimas')
        print('11) Graficar accion ')
        print('12) Salir')

        opcion = int(input('Elije una opcion: \n'))
        while opcion < 1 or opcion > 12:
            opcion = int(input('Elije una opcion (entre 1 y 12): '))
        return opcion