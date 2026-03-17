import smtplib
from email.mime.text import MIMEText

mensaje = MIMEText("Hola, este es un correo de prueba enviado desde MailTip.")
mensaje['Subject'] = "Correo de Prueba"
mensaje['From'] = "qaremitente@yopmail.com"
mensaje['To'] = "usuarioqa@test.com"
smtp = smtplib.SMTP('localhost', 1025)
smtp.send_message(mensaje)
smtp.quit()
print("Correo enviado a MailTip")
