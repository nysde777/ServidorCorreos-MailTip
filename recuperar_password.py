import smtplib
from email.mime.text import MIMEText

email_usuario = "usuario@test.com"
link_recuperacion = "http://localhost:8000/recuperar?token=abc123"
mensaje = MIMEText(f"Hola, haz clic en el siguiente enlace para recuperar tu contraseña: {link_recuperacion}")

mensaje["Subject"] = "Recuperación de contraseña"
mensaje["From"] = "app@test.com"
mensaje["To"] = email_usuario
smtp = smtplib.SMTP("192.168.31.134", 1025)
smtp.send_message(mensaje)
print("Correo de recuperación enviado a:", email_usuario)
smtp.quit()