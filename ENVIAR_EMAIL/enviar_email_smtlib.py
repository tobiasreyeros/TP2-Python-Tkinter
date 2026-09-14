"""
SMTP
¿Qué es y para qué sirve SMTP?
SMTP, Simple Mail Transfer Protocol por sus siglas en inglés, es un protocolo o conjunto de reglas 
de comunicación que utilizan los servidores de correo electrónico para enviar y recibir e-mails.
"""

from email.message import EmailMessage  # Construir la estructura del email
import os  # Para acceder a variables de entorno
import smtplib  # Conectar con el servidor y enviarlo
from tkinter import *
from tkinter import messagebox, simpledialog
from dotenv import load_dotenv  # Cargar variables desde archivo .env local
# Python Image Library
from PIL import ImageTk, Image

# Cargar variables del archivo .env local si existe
load_dotenv()

# ------------ INTERFAZ TKINTER ------------
ventana = Tk()
ventana.title("Enviar Gmail")
ventana.geometry("380x500")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(
    ventana,
    text="ENVIAR CORREO VIA GMAIL",
    fg="black",
    font=("Arial", 15, "bold"),
    padx=5,
    pady=5,
).grid(row=0, column=0, columnspan=2)

# Imagen GMAIL (Punto 4b)
try:
    imagen_gmail = Image.open(
        "C:/Users/NET USO ESCOLAR 115/Documents/Repositorios/TP2-Python-Tkinter/ENVIAR_EMAIL/xd.jpg"
    )
    nueva_imagen = imagen_gmail.resize((125, 84))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagen = Label(ventana, image=render)
    label_imagen.image = render
    label_imagen.grid(row=1, column=0, columnspan=2)
except Exception:
    Label(ventana, text="[Imagen no encontrada]").grid(
        row=1, column=0, columnspan=2
    )

# Variables
asunto = StringVar(ventana)
destinatario_seleccionado = StringVar(ventana)
remitente_input = StringVar(ventana, value="tobiastrabajo2@gmail.com")  # Valor por defecto

# Lista de destinatarios predefinidos (Punto 4c)
lista_correos = [
    "fjcoronati@gmail.com",  # Docente 1 (profe del TP)
    "docente2@gmail.com",  # Docente 2
    "mfedullo@gmail.com",  # Docente 3
    "elcrack35158@gmail.com",  # Compañero
    "tobiastrabajo2@gmail.com",  # Correo propio
]
destinatario_seleccionado.set(lista_correos[0])

# Campo de entrada de texto (Entry) para inputear el correo REMITENTE
Label(
    ventana, text="Remitente:", fg="black", font=("Arial", 10, "bold")
).grid(row=2, column=0, pady=5)
entry_remitente = Entry(ventana, textvariable=remitente_input, width=32)
entry_remitente.grid(row=2, column=1, pady=5)

# Menú desplegable para seleccionar DESTINATARIO
Label(
    ventana, text="Destinatario:", fg="black", font=("Arial", 10, "bold")
).grid(row=3, column=0, pady=5)
menu_destinatarios = OptionMenu(
    ventana, destinatario_seleccionado, *lista_correos
)
menu_destinatarios.config(width=26)
menu_destinatarios.grid(row=3, column=1, pady=5)

# Asunto
Label(ventana, text="Asunto:", fg="black", font=("Arial", 10, "bold")).grid(
    row=4, column=0, pady=5
)
Entry(ventana, textvariable=asunto, width=32).grid(row=4, column=1, pady=5)

# Mensaje
Label(ventana, text="Mensaje:", fg="black", font=("Arial", 10, "bold")).grid(
    row=5, column=0, pady=5
)
mensaje = Text(ventana, height=5, width=28, padx=5, pady=5)
mensaje.grid(row=5, column=1, pady=5)
mensaje.config(font=("Arial", 9))


# ------------ ENVIO DE CORREO ------------
def enviar_email():
    remitente_actual = remitente_input.get().strip()
    correo_destino = destinatario_seleccionado.get()

    if not remitente_actual:
        messagebox.showwarning(
            "Remitente requerido", "Por favor, ingrese el correo del remitente."
        )
        return

    # Intentar obtener la clave desde el archivo .env o variable de entorno
    app_password = os.getenv("GMAIL_APP_PASS")

    # Si no la encuentra, solicitarla interactivamente
    if not app_password:
        app_password = simpledialog.askstring(
            "Autenticación Requerida",
            f"Ingrese la Contraseña de Aplicación de Gmail para {remitente_actual}:",
            show="*",
        )
        if not app_password:
            messagebox.showwarning(
                "Envío cancelado",
                "Es necesaria la contraseña de aplicación para realizar el envío.",
            )
            return

    # Validar campos vacíos
    if not asunto.get().strip() or not mensaje.get(1.0, "end").strip():
        messagebox.showwarning(
            "Campos vacíos", "Por favor, completa el asunto y el mensaje."
        )
        return

    # Estructura del email
    email = EmailMessage()
    email["From"] = remitente_actual
    email["To"] = correo_destino
    email["Subject"] = asunto.get()
    email.set_content(str(mensaje.get(1.0, "end")))

    try:
        # Envío de email mediante protocolo SMTP
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(remitente_actual, app_password)
        smtp.send_message(email)
        smtp.quit()
        messagebox.showinfo("MENSAJERIA", "Mensaje enviado correctamente")
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo enviar el correo.\nDetalle: {e}"
        )


# ------------ BOTON ------------
Button(
    ventana,
    text="ENVIAR",
    command=enviar_email,
    height=2,
    width=10,
    bg="black",
    fg="white",
    font=("Arial", 10, "bold"),
).grid(row=6, column=0, columnspan=2, padx=5, pady=10)

ventana.mainloop()