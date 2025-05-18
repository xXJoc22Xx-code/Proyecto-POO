from datetime import datetime, date

class Contact:
    """
    Clase que representa un contacto con nombre, fecha de nacimiento, correo electrónico y un índice de mensaje opcional.

    Atributos:
        name (str): Nombre del contacto.
        birth_date (date): Fecha de nacimiento del contacto.
        email (str): Correo electrónico del contacto.
        message_index (int|None): Índice del mensaje personalizado para el contacto (opcional).
    """

    def __init__(self, name, birth_date, email, message_index=None):
        """
        Inicializa un objeto Contact.

        Args:
            name (str): Nombre del contacto.
            birth_date (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
            email (str): Correo electrónico del contacto.
            message_index (str|int|None): Índice del mensaje personalizado (opcional).
        """
        self.name = name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        self.email = email
        self.message_index = int(message_index) if message_index not in (None, '', 'None') else None

    def days_until_birthday(self):
        """
        Calcula los días que faltan para el próximo cumpleaños del contacto.

        Returns:
            int: Número de días hasta el próximo cumpleaños.
        """
        today = date.today()
        this_year_birthday = self.birth_date.replace(year=today.year)
        if this_year_birthday < today:
            this_year_birthday = this_year_birthday.replace(year=today.year + 1)
        return (this_year_birthday - today).days

    def is_birthday_today(self):
        """
        Verifica si hoy es el cumpleaños del contacto.

        Returns:
            bool: True si hoy es el cumpleaños, False en caso contrario.
        """
        today = date.today()
        return (self.birth_date.month == today.month) and (self.birth_date.day == today.day)

