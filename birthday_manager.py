import csv
import os
import random

class MessageManager:
    """
    Clase para gestionar mensajes de felicitación almacenados en un archivo CSV.
    
    Atributos:
        filename (str): Nombre del archivo CSV donde se guardan los mensajes.
        messages (list of str): Lista de mensajes cargados desde el archivo.
    """

    def __init__(self, filename="messages.csv"):
        """
        Inicializa el gestor de mensajes y carga los mensajes existentes desde el archivo.
        
        Args:
            filename (str, opcional): Ruta del archivo CSV con mensajes. Por defecto "messages.csv".
        """
        self.filename = filename
        self.messages = []
        self.load_messages()

    def load_messages(self):
        """
        Carga los mensajes desde el archivo CSV si existe.
        """
        if os.path.exists(self.filename):
            with open(self.filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                self.messages = [row[0] for row in reader]

    def save_messages(self):
        """
        Guarda la lista actual de mensajes en el archivo CSV, sobrescribiendo el contenido.
        """
        with open(self.filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for message in self.messages:
                writer.writerow([message])

    def add_message(self, message):
        """
        Añade un nuevo mensaje a la lista y guarda los cambios.

        Args:
            message (str): Texto del mensaje a añadir.
        """
        self.messages.append(message)
        self.save_messages()

    def get_random_message(self):
        """
        Devuelve un mensaje aleatorio de la lista.
        
        Returns:
            str: Un mensaje aleatorio o un mensaje por defecto si la lista está vacía.
        """
        return random.choice(self.messages) if self.messages else "¡Feliz cumpleaños!"

    def remove_message(self, index):
        """
        Elimina un mensaje de la lista dado su índice y guarda los cambios.

        Args:
            index (int): Índice del mensaje a eliminar.
        """
        if 0 <= index < len(self.messages):
            del self.messages[index]
            self.save_messages()
