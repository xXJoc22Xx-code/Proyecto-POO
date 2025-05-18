%%writefile app.py
from birthday_manager import BirthdayManager
from message_manager import MessageManager
from email_sender import EmailSender
from birthday_service import BirthdayService
import streamlit as st
from datetime import date

# Configuración inicial
st.set_page_config(page_title="Gestor de Cumpleaños", page_icon="🎂")

# Inicializar gestores
bm = BirthdayManager()
mm = MessageManager()

# Inicializar el control de correos enviados por día
hoy = str(date.today())
if "correos_enviados_hoy" not in st.session_state or st.session_state.get("correos_fecha") != hoy:
    st.session_state.correos_enviados_hoy = set()
    st.session_state.correos_fecha = hoy

# Menú lateral
with st.sidebar:
    st.header("Menú de Navegación")
    pagina = st.radio(
        "Selecciona una sección:",
        ["🏠 Inicio", "➕ Agregar", "🗑️ Eliminar"],
        index=0
    )

# Página Principal
if pagina == "🏠 Inicio":
    st.title("🎉 Gestor de Cumpleaños - Inicio")

    # Inicializar servicio solo una vez
    if "email_service" not in st.session_state:
        st.session_state.email_service = BirthdayService(
            bm,
            mm,
            EmailSender("smtp.gmail.com", 587, "tu correo", "tu contraseña")
        )

    # --- Cumpleaños hoy ---
    st.header("🎁 Cumpleaños hoy")
    contacts_today = bm.get_contacts_with_birthday_today()

    if contacts_today:
        for contact in contacts_today:
            st.write(f"**{contact.name}** - {contact.email}")

        # --- Envío automático al cargar la página (una vez por persona por día) ---
        st.header("📨 Felicitaciones enviadas hoy")
        nuevos_a_felicitar = [
            c for c in contacts_today if c.email not in st.session_state.correos_enviados_hoy
        ]

        if nuevos_a_felicitar:
            sent = []
            for contact in nuevos_a_felicitar:
                st.session_state.email_service.email_sender.send_email(
                    contact.email, "🎉 ¡Feliz cumpleaños!", mm.get_random_message()
                )
                st.session_state.correos_enviados_hoy.add(contact.email)
                sent.append((contact.name, contact.email))

            for name, email in sent:
                st.success(f"Correo enviado a {name} ({email})")
        else:
            st.info("Todos los contactos de hoy ya fueron felicitados.")

        # --- Botón manual para reenviar a nuevos ---
        if st.button("🎈 Enviar felicitaciones ahora", key="enviar_hoy"):
            nuevos_a_felicitar = [
                c for c in contacts_today if c.email not in st.session_state.correos_enviados_hoy
            ]
            if nuevos_a_felicitar:
                sent = []
                for contact in nuevos_a_felicitar:
                    st.session_state.email_service.send_email(
                        contact.email, "🎉 ¡Feliz cumpleaños!", mm.get_random_message()
                    )
                    st.session_state.correos_enviados_hoy.add(contact.email)
                    sent.append((contact.name, contact.email))
                st.success("✅ Nuevas felicitaciones enviadas:")
                for name, email in sent:
                    st.write(f"- {name} ({email})")
            else:
                st.info("Todos los contactos de hoy ya fueron felicitados.")
    else:
        st.info("No hay cumpleaños hoy.")

    # --- Próximos cumpleaños ---
    st.header("📅 Próximos cumpleaños")
    for contact in sorted(bm.contacts, key=lambda c: c.days_until_birthday()):
        st.write(f"**{contact.name}** ({contact.birth_date.strftime('%d/%m/%Y')}) - en {contact.days_until_birthday()} días")

# Página de Agregar
elif pagina == "➕ Agregar":
    st.title("🎉 Gestor de Cumpleaños - Agregar")

    # --- Agregar contacto ---
    with st.expander("➕ Nuevo Contacto", expanded=True):
        with st.form("Agregar contacto"):
            name = st.text_input("Nombre")
            birth_date = st.date_input("Fecha de nacimiento")
            email = st.text_input("Correo electrónico")
            msg_options = ["Aleatorio"] + mm.messages
            selected_msg = st.selectbox("Mensaje personalizado", msg_options)
            submitted = st.form_submit_button("Agregar")
            if submitted:
                index = None if selected_msg == "Aleatorio" else msg_options.index(selected_msg) - 1
                bm.add_contact(name, birth_date.strftime("%Y-%m-%d"), email, index)
                st.success(f"Contacto {name} agregado.")

    # --- Agregar mensaje ---
    with st.expander("💌 Nuevo Mensaje", expanded=True):
        with st.form("Agregar mensaje"):
            new_message = st.text_area("Contenido del mensaje")
            add_msg = st.form_submit_button("Guardar mensaje")
            if add_msg:
                mm.add_message(new_message)
                st.success("Mensaje guardado")

    # --- Asignar mensaje ---
    with st.expander("🎯 Asignar Mensaje", expanded=True):
        with st.form("Asignar mensaje"):
            contact_names = [c.name for c in bm.contacts]
            selected_contact = st.selectbox("Selecciona un contacto", contact_names)
            msg_choices = [f"{i+1}. {m}" for i, m in enumerate(mm.messages)]
            selected_index = st.selectbox("Selecciona mensaje", msg_choices)
            asignar = st.form_submit_button("Asignar mensaje")
            if asignar:
                index = int(selected_index.split('.')[0]) - 1
                bm.assign_message_to_contact(selected_contact, index)
                st.success(f"Mensaje asignado a {selected_contact}.")

# Página de Eliminar
elif pagina == "🗑️ Eliminar":
    st.title("🎉 Gestor de Cumpleaños - Eliminar")

    with st.expander("🗑️ Eliminar Contactos", expanded=True):
        if bm.contacts:
            contactos_a_eliminar = [c.name for c in bm.contacts]
            selected_contact = st.selectbox("Selecciona un contacto:", contactos_a_eliminar)

            if st.button("❌ Confirmar eliminación de contacto", key="eliminar_contacto"):
                bm.remove_contact(selected_contact)
                st.success(f"Contacto '{selected_contact}' eliminado!")
        else:
            st.warning("No hay contactos registrados")

    # --- Eliminar Mensajes ---
    with st.expander("🗑️ Eliminar Mensajes", expanded=True):
        if mm.messages:
            selected_msg_index = st.selectbox(
                "Selecciona un mensaje:",
                options=[f"{i+1}. {msg}" for i, msg in enumerate(mm.messages)]
            )

            if st.button("❌ Confirmar eliminación de mensaje", key="eliminar_mensaje"):
                index = int(selected_msg_index.split(".")[0]) - 1
                mm.remove_message(index)
                st.success("Mensaje eliminado!")
        else:
            st.warning("No hay mensajes guardados")
