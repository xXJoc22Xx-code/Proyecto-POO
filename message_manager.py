"""
message_manager.py

Este módulo contiene la clase MessageManager, que genera mensajes de felicitación personalizados para los contactos.
"""

class MessageManager:
    """
    Generador de mensajes de cumpleaños personalizados.
    """

    def create_message(self, contact):
        """
        Crea un mensaje de cumpleaños personalizado para un contacto.

        :param contact: Objeto Contact para el cual se generará el mensaje.
        :return: Cadena con el mensaje personalizado.
        """
        return f"¡Feliz cumpleaños, {contact.name}! Espero que tengas un día maravilloso."
