import csv
from contact import Contact

class BirthdayManager:
    """
    Clase para gestionar una lista de contactos con cumpleaños,
    cargándolos desde un archivo CSV, guardándolos y realizando operaciones sobre ellos.

    Atributos:
        filename (str): Nombre del archivo CSV donde se almacenan los contactos.
        contacts (list of Contact): Lista de objetos Contact cargados desde el archivo.
    """

    def __init__(self, filename="contacts.csv"):
        """
        Inicializa el gestor de cumpleaños y carga los contactos desde el archivo CSV.

        Args:
            filename (str, opcional): Nombre del archivo CSV. Por defecto "contacts.csv".
        """
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """
        Carga los contactos desde el archivo CSV.

        Returns:
            list of Contact: Lista de contactos cargados. Si el archivo no existe, devuelve lista vacía.
        """
        contacts = []
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    contact = Contact(
                        row['name'],
                        row['birth_date'],
                        row['email'],
                        row.get('message_index', None)
                    )
                    contacts.append(contact)
        except FileNotFoundError:
            pass
        return contacts

    def save_contacts(self):
        """
        Guarda la lista actual de contactos en el archivo CSV, sobrescribiendo su contenido.
        """
        with open(self.filename, mode="w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "birth_date", "email", "message_index"])
            for contact in self.contacts:
                writer.writerow([
                    contact.name,
                    contact.birth_date.isoformat(),
                    contact.email,
                    contact.message_index if contact.message_index is not None else ""
                ])

    def add_contact(self, name, birth_date, email, message_index=None):
        """
        Agrega un nuevo contacto a la lista y guarda los cambios.

        Args:
            name (str): Nombre del contacto.
            birth_date (str): Fecha de nacimiento en formato 'YYYY-MM-DD'.
            email (str): Correo electrónico del contacto.
            message_index (int|None, opcional): Índice de mensaje personalizado. Por defecto None.
        """
        contact = Contact(name, birth_date, email, message_index)
        self.contacts.append(contact)
        self.save_contacts()

    def assign_message_to_contact(self, contact_name, message_index):
        """
        Asigna un índice de mensaje personalizado a un contacto dado por su nombre.

        Args:
            contact_name (str): Nombre del contacto al que se asigna el mensaje.
            message_index (int): Índice del mensaje a asignar.
        """
        for contact in self.contacts:
            if contact.name == contact_name:
                contact.message_index = message_index
        self.save_contacts()

    def get_contacts_with_birthday_today(self):
        """
        Obtiene la lista de contactos cuyo cumpleaños es hoy.

        Returns:
            list of Contact: Lista de contactos con cumpleaños hoy.
        """
        return [c for c in self.contacts if c.is_birthday_today()]

    def remove_contact(self, contact_name):
        """
        Elimina un contacto de la lista por nombre y guarda los cambios.

        Args:
            contact_name (str): Nombre del contacto a eliminar.
        """
        self.contacts = [c for c in self.contacts if c.name != contact_name]
        self.save_contacts()
