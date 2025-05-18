from datetime import date

class BirthdayService:
    """
    Servicio que gestiona el envío de felicitaciones de cumpleaños
    utilizando un gestor de contactos, un gestor de mensajes y un sistema de envío de emails.
    """

    def __init__(self, birthday_manager, message_manager, email_sender):
        """
        Inicializa el servicio con los gestores necesarios.

        Args:
            birthday_manager: Instancia encargada de gestionar los contactos y sus cumpleaños.
            message_manager: Instancia que proporciona los mensajes de felicitación.
            email_sender: Instancia que envía los correos electrónicos.
        """
        self.birthday_manager = birthday_manager
        self.message_manager = message_manager
        self.email_sender = email_sender

    def send_greetings_for_today(self):
        """
        Envía correos electrónicos de felicitación a todos los contactos que cumplen años hoy.

        Para cada contacto con cumpleaños hoy, selecciona un mensaje personalizado si tiene un índice válido,
        o un mensaje aleatorio en caso contrario.

        Returns:
            list of tuple: Lista de tuplas (nombre, email) de los contactos a los que se les envió el correo.
        """
        sent = []
        contacts_today = self.birthday_manager.get_contacts_with_birthday_today()

        for contact in contacts_today:
            if contact.message_index is not None and 0 <= contact.message_index < len(self.message_manager.messages):
                msg = self.message_manager.messages[contact.message_index]
            else:
                msg = self.message_manager.get_random_message()

            self.email_sender.send_email(contact.email, "🎉 ¡Feliz cumpleaños!", msg)
            sent.append((contact.name, contact.email))

        return sent
