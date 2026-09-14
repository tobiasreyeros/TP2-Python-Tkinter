Trabajo Práctico N°2: Interfaz Gráfica de Usuario (GUI) y GitHub Fork

Alumno: Tobías Reyeros Raul Aguero
Repositorio Original: [LuisOchoa1495/Python-Tkinter](https://github.com/LuisOchoa1495/Python-Tkinter)  
Materia: Laboratorio de Programación  


Descripción del Proyecto
Este proyecto es una bifurcación (Fork) de una aplicación desarrollada en Python con Tkinter para el envío de correos electrónicos a través del protocolo SMTP de Gmail.

¿Qué es SMTP?
SMTP (*Simple Mail Transfer Protocol*) es el protocolo estándar de red utilizado para el intercambio y envío de correos electrónicos entre servidores o desde un cliente hacia un servidor de correo.


Modificaciones Realizadas

1. Selección de Remitente: Se añadió un campo de entrada (`Entry`) que permite al usuario ingresar de forma dinámica el correo desde el cual desea enviar el mensaje.
2. Menú de Destinatarios (`OptionMenu`): Se reemplazó el campo de texto simple por un menú desplegable que incluye direcciones de correo predefinidas de docentes, compañeros y correo propio.
3. Seguridad y Credenciales: Se integró el módulo `python-dotenv` para manejar la Contraseña de Aplicación de Gmail a través de variables de entorno y evitar la exposición de datos sensibles en el repositorio.
4. Personalización Visual: Se incorporó una imagen personalizada en la interfaz gráfica mediante la librería `Pillow` (`PIL`).
5. Compilación: Se generó el ejecutable distribuible para Windows utilizando la herramienta `pyinstaller`, ubicado en la carpeta `/output`.


Capturas de Pantalla

Interfaz Principal de la Aplicación
<img width="377" height="528" alt="image" src="https://github.com/user-attachments/assets/d6b6f4c6-2c3d-4a6d-9efb-523140f217d0" />


Confirmación de Recepción en Bandeja de Entrada
<img width="459" height="532" alt="image" src="https://github.com/user-attachments/assets/74ea37b9-9020-48f7-9b11-f7bc6d6bb415" />

<img width="1038" height="239" alt="image" src="https://github.com/user-attachments/assets/62695e40-9223-464a-8769-eadc09f43bf1" />
