const nodemailer = require("nodemailer");

let transporter = nodemailer.createTransport({
    host: "192.168.31.134",
    port: 1025,
    secure: false, 
});

transporter.sendMail({
    from: "node@test.com",
    to: "usuarioqa@test.com",
    subject: "Correo de prueba desde Node.js",
    text: "¡Hola! Este es un correo de prueba enviado desde Node.js usando MailTip.",
}, (error, info) => {
    if (error) {
        return console.log("Error al enviar correo:", error);
    }
    console.log("Correo enviado correctamente:", info.response);
});