import requests
respuesta = requests.get('http://192.168.31.134:8025/api/v1/messages')
data = respuesta.json()
correos = data["messages"]
print("Cantidad de correos capturados:", len(correos))
if len(correos) > 0:
    primer_correo = correos[0]
    print("Asunto del primer correo:", primer_correo["Subject"])
    print("Remitente del primer correo:", primer_correo["From"])
    print("Destinatario del primer correo:", primer_correo["To"])

else:
    print("No se han capturado correos.")