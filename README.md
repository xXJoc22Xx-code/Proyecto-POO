# 🎉 Gestor de Cumpleaños en Python

Una aplicación desarrollada en Python que permite gestionar cumpleaños, mostrar próximos eventos y enviar felicitaciones automáticas por correo electrónico usando una interfaz amigable en Streamlit.

##  Características Principales

- Registro y visualización de cumpleaños.
- Cuenta regresiva para próximos cumpleaños.
- Envío automático de correos de felicitación.
- Personalización de mensajes para cada contacto.
- Código organizado con clases y módulos, siguiendo los principios SOLID.
- Interfaz web con [Streamlit](https://streamlit.io/).
- Persistencia de datos en archivos `.csv`.

## Estructura del Proyecto

```
birthday_app/
├── app.py                  # Interfaz web con Streamlit
├── contact.py              # Clase Contact
├── birthday_manager.py     # Gestión de contactos y fechas
├── message_manager.py      # Gestión de mensajes
├── email_sender.py         # Envío de correos SMTP
├── birthday_service.py     # Servicio de envío automático
├── contacts.csv            # Archivo de contactos (se genera)
├── messages.csv            # Archivo de mensajes (se genera)
├── sent_log.csv            # Registro de correos enviados (se genera)
└── README.md               # Documentación del proyecto
```
## Cómo ejecutar la aplicación

El archivo principal para iniciar la aplicación es `app.py`.

Para ejecutar la aplicación, usa el siguiente comando en la terminal:

```bash
python app.py
```

## Diagrama UML
![Diagrama-UML](https://github.com/user-attachments/assets/5b763067-e16a-4bc0-808a-03d5731d95fc)



