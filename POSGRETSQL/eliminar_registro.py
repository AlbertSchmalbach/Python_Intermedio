import psycopg2
from xlwt import Workbook

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
            sql = 'DELETE FROM persona WHERE id_persona=%s'
            entrada_id = input('Ingrese el numero de ID a eliminar: ')
            val = (entrada_id,)
            cursor.execute(sql, val)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: ', registros_eliminados)
except Exception as e:
    print("\n")
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close