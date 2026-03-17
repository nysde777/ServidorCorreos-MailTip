import smtplib

from email.mime.text import MIMEText

email_usuario = "usuarioqa@test.com"
mensaje = MIMEText("Bienvenido a nuestro sitio web, gracias por registrarte!")
mensaje["Subject"] = "Registro exitoso"
mensaje["From"] = "app@test.com"
mensaje["To"] = email_usuario

smtp = smtplib.SMTP("192.168.31.134", 1025)

smtp.send_message(mensaje)
print("Correo de registro enviado a:", email_usuario)
smtp.quit()