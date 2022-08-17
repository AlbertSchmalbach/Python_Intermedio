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
            sql = 'SELECT * FROM persona ORDER BY id_persona ASC'
            cursor.execute(sql)
            registros = cursor.fetchall()

            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close