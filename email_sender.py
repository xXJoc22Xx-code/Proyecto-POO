import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    """
    Clase para enviar correos electrónicos usando un servidor SMTP.

    Atributos:
        smtp_server (str): Dirección del servidor SMTP.
        port (int): Puerto del servidor SMTP.
        sender_email (str): Dirección de correo electrónico del remitente.
        password (str): Contraseña para autenticarse en el servidor SMTP.
    """

    def __init__(self, smtp_server, port, sender_email, password):
        """
        Inicializa el objeto EmailSender con los datos del servidor y credenciales.

        Args:
            smtp_server (str): Dirección del servidor SMTP.
            port (int): Puerto del servidor SMTP.
            sender_email (str): Correo electrónico del remitente.
            password (str): Contraseña del remitente para autenticación.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, to_email, subject, message):
        """
        Envía un correo electrónico simple con asunto y mensaje de texto plano.

        Args:
            to_email (str): Dirección de correo electrónico del destinatario.
            subject (str): Asunto del correo.
            message (str): Contenido del mensaje de correo.

        Imprime en consola si el envío fue exitoso o si ocurrió un error.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = to_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, to_email, msg.as_string())
            server.quit()
            print(f"✅ Correo enviado a {to_email}")
        except Exception as e:
            print(f"❌ Error al enviar correo a {to_email}: {e}")
