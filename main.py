import streamlit as st
import pandas as pd
from PIL import Image

st.title("Clippy AI Solutions")
st.markdown("A partir de los correos recibidos nuestra solución Summary entregará un resumen ordenado de los correos prioritarios con un detalle de la urgencia y categoría de estos.")
# st.markdown("Esta app mostrará el resumen diario")

df_priority = pd.read_csv("data.csv")

response ="""
Respuesta Automática: Estimado José Gómez,
Gracias por su interés en nuestro producto de crédito hipotecario. Para poder procesar su solicitud, necesitamos algunos detalles adicionales. Por favor,
proporcione su número de teléfono y RUT. Además, hemos notado que usted no es cliente de banca con nosotros. Para solicitar un crédito hipotecario, es necesario abrir una con nosotros. ¿Le gustaría que le ayudemos con el proceso de apertura de cuenta?
Por último, hemos recibido sus documentos adjuntos. Los revisaremos y nos pondremos en contacto con usted necesitamos información adicional.

Quedamos atentos a su respuesta.
Saludos cordiales,Agente AI Scotiabank
"""

body={'nombre_cliente': 'José Gómez',
                     'email_cliente': 'josebas.gmz@gmail.com',
                     'telefono_cliente': '',
                     'rut': '',
                     'cliente_banca': False,
                     'correo_interno': False,
                     'urgencia': 2,
                     'categoria': 'Ventas',
                     'producto': 'Credito Hipotecario',
                     'resumen': 'Solicitud crédito hipotecario - Busco financiar 2000UF de 3700 que cuesta la propiedad a 25 años con tasa fija.',
                     'adjuntos': ['identificación.pdf', 'liquidación_marzo.pdf', 'cartola_afp.pdf']}

mail= {'from': 'josebas.gmz@gmail.com',
       'body': 'Buen día Paola,\
                Busco financiar 2000UF de 3700 que cuesta la propiedad a 25 años con tasa fija.\
                    La propiedad está para listo para escriturar, es un departamento nuevo ubicado\
                        en ciudad empresarial (Proyecto Parque los Almendros de la inmobiliaria Fortaleza).\
                            Adjunto las últimas liquidaciones de sueldo y el certificado de la AFP.\
                            Si necesita algo adicional quedo atento.\
                              José Gómez'}

st.text("Email enviado por el cliente:")
st.json(mail, expanded=True)

st.text("Resumen realizado por IA:")
st.json(body, expanded=True)

st.text("Respuesta automática al correo enviado por el cliente:")
st.markdown(response)

image = Image.open('requerimientos.png')

st.image(image, caption='Revisión de requerimientos')

st.text("Tabla resumen de los correos ordenados por prioridad:")
st.table(data=df_priority)
