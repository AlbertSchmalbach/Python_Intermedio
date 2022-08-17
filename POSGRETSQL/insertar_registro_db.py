import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'admin',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sql ='INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            num_regist = int(input('Cuantos registros vas a insertar: '))
            valores = []
            for r in range(num_regist):
                nombre = input('Nombre: ')
                ape = input('Apellido: ')
                mail = input('Correo: ')
                print("\n")

                val = (nombre, ape, mail)

                valores.append(val)
            valores = tuple(valores)
            
            cursor.executemany(sql, valores)
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: ', registros_insertados)

except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close