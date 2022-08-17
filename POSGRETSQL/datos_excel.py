import psycopg2
import pandas as pd

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
            df = pd.read_sql(sql, con = conexion)
            print(df)
            df.to_excel('datos_bs.xlsx', index=False)
            
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close