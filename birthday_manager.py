"""
birthday_manager.py

Este módulo contiene la clase BirthdayManager, responsable de gestionar contactos y verificar si cumplen años hoy.
"""

from datetime import datetime

class BirthdayManager:
    """
    Administra una lista de contactos y verifica si hoy es su cumpleaños.
    """

    def __init__(self, contacts):
        """
        Inicializa el gestor con una lista de contactos.

        :param contacts: Lista de objetos Contact.
        """
        self.contacts = contacts

    def get_birthdays_today(self):
        """
        Retorna una lista de contactos que cumplen años hoy.

        :return: Lista de objetos Contact que tienen cumpleaños hoy.
        """
        today = datetime.today().strftime('%m-%d')
        return [contact for contact in self.contacts if contact.birthday[5:] == today]
