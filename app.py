import streamlit as st
from birthday_manager import BirthdayManager
from message_manager import MessageManager
from email_sender import EmailSender
from birthday_service import BirthdayService

st.set_page_config(page_title="Gestor de Cumpleaños", page_icon="🎂")
st.title("🎉 Gestor de Cumpleaños")

# Inicializar componentes
bm = BirthdayManager()
mm = MessageManager()
email_sender = EmailSender("smtp.gmail.com", 587, "tu_email@gmail.com", "tu_contraseña")
service = BirthdayService(bm, mm, email_sender)

# --- Envío automático de correos al abrir ---
st.header("📨 Felicitaciones enviadas hoy")
sent = service.send_greetings_for_today()
if sent:
    for name, email in sent:
        st.success(f"Correo enviado a {name} ({email})")
else:
    st.info("No hay cumpleaños hoy o ya se enviaron los correos.")

# --- Lista de cumpleaños hoy ---
st.header("🎁 Cumpleaños hoy")
cumples_hoy = bm.get_contacts_with_birthday_today()
if cumples_hoy:
    for c in cumples_hoy:
        st.write(f"🎈 {c.name} - {c.email}")
else:
    st.write("Nadie cumple años hoy.")

# --- Lista de próximos cumpleaños ---
st.header("📅 Próximos cumpleaños")
for contact in sorted(bm.contacts, key=lambda c: c.days_until_birthday()):
    st.write(f"{contact.name} ({contact.birth_date.strftime('%d/%m/%Y')}) - en {contact.days_until_birthday()} días")
