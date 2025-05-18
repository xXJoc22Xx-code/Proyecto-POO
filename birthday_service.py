import csv
from datetime import date

class BirthdayService:
    def __init__(self, birthday_manager, message_manager, email_sender, log_file="sent_log.csv"):
        self.birthday_manager = birthday_manager
        self.message_manager = message_manager
        self.email_sender = email_sender
        self.log_file = log_file
        self.sent_today = self.load_sent_today()

    def load_sent_today(self):
        try:
            with open(self.log_file, newline='', encoding='utf-8') as f:
                return {(row['email'], row['date']) for row in csv.DictReader(f)}
        except FileNotFoundError:
            return set()

    def save_sent_today(self, contact):
        with open(self.log_file, mode="a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            today_str = date.today().isoformat()
            writer.writerow([contact.name, contact.email, today_str])

    def send_greetings_for_today(self):
        sent = []
        today_str = date.today().isoformat()
        contacts_today = self.birthday_manager.get_contacts_with_birthday_today()

        try:
            with open(self.log_file, 'r', encoding='utf-8') as f:
                pass
        except FileNotFoundError:
            with open(self.log_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["name", "email", "date"])

        for contact in contacts_today:
            if (contact.email, today_str) in self.sent_today:
                continue

            if contact.message_index is not None and 0 <= contact.message_index < len(self.message_manager.messages):
                msg = self.message_manager.messages[contact.message_index]
            else:
                msg = self.message_manager.get_random_message()

            self.email_sender.send_email(contact.email, "🎉 ¡Feliz cumpleaños!", msg)
            self.save_sent_today(contact)
            sent.append((contact.name, contact.email))
        return sent
