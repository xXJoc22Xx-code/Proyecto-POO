"""
contact.py

Este módulo define la clase Contact, que representa un contacto con nombre, correo electrónico y fecha de cumpleaños.
"""

class Contact:
    """
    Representa un contacto con nombre, correo electrónico y cumpleaños.
    """
    def __init__(self, name, email, birthday):
        """
        Inicializa un nuevo contacto.

        :param name: Nombre del contacto.
        :param email: Correo electrónico del contacto.
        :param birthday: Fecha de cumpleaños del contacto en formato 'YYYY-MM-DD'.
        """
        self.name = name
        self.email = email
        self.birthday = birthday
