"""
email_sender.py

Este módulo define la clase EmailSender, responsable de enviar mensajes por correo electrónico.
"""

class EmailSender:
    """
    Simula el envío de correos electrónicos.
    """

    def send_email(self, contact, message):
        """
        Simula el envío de un mensaje de cumpleaños a un contacto.

        :param contact: Objeto Contact al que se enviará el correo.
        :param message: Mensaje a enviar.
        """
        print(f"Enviando correo a {contact.email}: {message}")
