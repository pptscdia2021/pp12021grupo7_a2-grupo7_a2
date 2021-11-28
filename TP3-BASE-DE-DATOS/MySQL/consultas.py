import pymysql

DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'felipe' 
DB_NAME = 'employees' 

def run_query(query=''): 
    try:
        conn = pymysql.connect(host=DB_HOST,
                             user=DB_USER,
                             password=DB_PASS,
                             db=DB_NAME)
                                # Conectar a la base de datos 
        print ("Conexion exitosa!")
        cursor = conn.cursor()         # Crear un cursor 
        cursor.execute(query)          # Ejecutar una consulta 

        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()   # Traer los resultados de un select 
        else: 
            conn.commit()              # Hacer efectiva la escritura de datos 
            data = None 
        
        cursor.close()                 # Cerrar el cursor 
        conn.close()                   # Cerrar la conexión 

        return data
    
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	    print("Ocurrió un error al conectar: ", e)
     

''' query = "SELECT * FROM employees;" 
result = run_query(query) 
print (result) '''

query = "SELECT emp_no, last_name FROM employees WHERE gender ='F';"
result = run_query(query) 
print (result)

query = "INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (1000, '1985-01-01','Pepe', 'Pe','M','1985-01-01');"
run_query(query)

query = "SELECT * FROM employees where first_name = 'Pepe';"
result = run_query(query) 
print (result)

query = "DELETE FROM employees WHERE first_name = 'Pepe';"
run_query(query)