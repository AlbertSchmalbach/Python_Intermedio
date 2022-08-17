# En primer lugar, se importan las librerías que se utilizarán para preparar y enviar el mensaje.

import smtplib, ssl    # Librerías para conectarse al servidor y enviar el mensaje
from email.mime.text import MIMEText   # Librerías para la creación del mensaje
from email.mime.multipart import MIMEMultipart
from getpass import getpass   # Librería para capturar la contraseña
import pandas as pd      # Libería para leer el archivo con los datos de los destinatarios.

# Luego, se crean las versiones en texto plano y HTML del mensaje prototipo.  
# Note los rótulos que se utilizan para identificar los campos personalizables dentro del mensaje.

# Mensaje en texto plano
texto = """\
Cordial saludo, {name}.

Soy Gerardo Becerra, docente de la ECBTI en la UNAD y presentador del taller Automatiza las tareas aburridas usando Python.

Usted ha registrado su asistencia al evento con los siguientes datos:

- Nombres: {name}.
- Apellidos: {lname}.
- Correo electrónico: {email}.
- Estamento: {estam}.

Espero que este taller sea de gran utilidad para usted.

Atentamente,

Gerardo Becerra.

"""
# Mensaje en HTML
html = """\
<html>
    <body>
        <p>Cordial saludo, {name}.</p>
        <p>Soy Gerardo Becerra, docente de la ECBTI en la UNAD y presentador del taller <b>Automatiza las tareas aburridas usando Python</b>.</p>
        <p>Usted ha registrado su asistencia al evento con los siguientes datos:</p>
        <ul>
            <li>Nombres: {name}.</li>
            <li>Apellidos: {lname}.</li>
            <li>Correo electrónico: {email}.</li>
            <li>Estamento: {estam}.</li>
        </ul>
        <p>Espero que este taller sea de gran utilidad para usted.</p>
        <p>Atentamente,</p>
        <p>Gerardo Becerra.</p>    
    </body>
</html>
"""

# Se utiliza la librería `Pandas` para leer el archivo xlsx donde se encuentran los datos de los destinatarios del mensaje

asistentes = pd.read_excel("Talleres ETR 2021-2 - Automatiza las tareas aburridas usando Python - Registro de Asistencia (Responses).xlsx",\
             sheet_name="Form Responses 1",\
             header=0,index_col=0,usecols="B:F")

# Se definen los datos básicos de la cuenta de correo del remitente: dirección y contraseña.

email_envia = "taller.python.unad@gmail.com"
password = getpass()

# Para cada destinatario se leen los datos registrados en el archivo xlsx, se insertan dentro de la plantilla del mensaje preparado previamente y se envía el mensaje.

# Para cada destinatario lee los datos (nombres, apellidos, correo, estamento)
for nombres, apellidos, correo, estamento in zip(asistentes['Nombres'],\
    asistentes['Apellidos'],asistentes['Correo electrónico'],asistentes['Estamento']):    
    email_recibe = correo

    # Prepara el mensaje
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = "Mensaje de correo personalizado"
    mensaje["From"] = email_envia
    mensaje["To"] = email_recibe

    # Se insertan los datos en la plantilla y se convierte el HTML/texto plano a objetos MIMEText
    part1 = MIMEText(texto.format(name=nombres,lname=apellidos,email=correo,estam=estamento), "plain")
    part2 = MIMEText(html.format(name=nombres,lname=apellidos,email=correo,estam=estamento), "html")    

    # Agrega las partes HTML/texto plano al mensaje MIMEMultipart
    mensaje.attach(part1)
    mensaje.attach(part2)

    # Crea una conexión segura con el servidor usando SSL y se conecta al servidor
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # Envía el mensaje de correo
        print(f"Enviando correo a {nombres} {apellidos}")
        server.login(email_envia, password)
        server.sendmail(
            email_envia, email_recibe, mensaje.as_string()
        )
print('Proceso finalizado exitosamente.')