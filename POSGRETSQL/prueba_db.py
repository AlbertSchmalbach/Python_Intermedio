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
            # sql = 'SELECT * FROM persona WHERE id_persona IN %s'
            sql = 'SELECT * FROM persona'
            # id_persona = input('Proporciona el valor id_persona: ')
            # entrada = input('Proporciona los id a buscar (separados por coma): ')
            # llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sql)
            # cursor.execute(sql, llaves_primarias)
            registros = cursor.fetchall()
            # registros = cursor.fetchone()
            for registro in registros:
                print(registro)
            
            wb = Workbook()
            sheet = wb.add_sheet('Sheet 1')
            sheet.write(0,0, 'ID')
            sheet.write(0,1, 'NAME')
            sheet.write(0,2, 'LASTNAME')
            sheet.write(0,3, 'EMAIL')
        
            contador = 1

            for i in registros:
                sheet.write(contador,0, i[0])
                sheet.write(contador,1, i[1])
                sheet.write(contador,2, i[2])
                sheet.write(contador,3, i[3])
                contador+=1

            wb.save('datos.xls')
except Exception as e:
    print(f'Ocurrio un error: {e}')

finally:
    conexion.close