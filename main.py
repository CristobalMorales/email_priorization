import streamlit as st
import pandas as pd

st.title("Procesamiento de correos recibidos")
st.text("A partir de los correos recibidos nuestra solución Summary entregará un resumen ordenado de los correos prioritarios con un detalle de la urgencia y categoría de estos.")
# st.markdown("Esta app mostrará el resumen diario")

df_priority = pd.read_csv("data.csv")

st.table(data=df_priority)


body={'nombre_cliente': 'José Gómez',
                     'email_cliente': 'josebas.gmz@gmail.com',
                     'telefono_cliente': '',
                     'rut': '',
                     'cliente_banca': False,
                     'correo_interno': False,
                     'urgencia': 2,
                     'categoria': 'Ventas',
                     'producto': 'Apertura de cuenta',
                     'resumen': 'Solicitud crédito hipotecario - Busco financiar 2000UF de 3700 que cuesta la propiedad a 25 años con tasa fija.',
                     'adjuntos': ['identificación.pdf', 'liquidación_marzo.pdf', 'cartola_afp.pdf'],
                     'body': 'Buen día Paola,\
                              Busco financiar 2000UF de 3700 que cuesta la propiedad a 25 años con tasa fija.\
                              La propiedad está para listo para escriturar, es un departamento nuevo ubicado\
                              en ciudad empresarial (Proyecto Parque los Almendros de la inmobiliaria Fortaleza).\
                              Adjunto las últimas liquidaciones de sueldo y el certificado de la AFP.\
                              Si necesita algo adicional quedo atento.\
                              José Gómez'}

st.json(body, expanded=True)
from PIL import Image

image = Image.open('requerimientos.png')

st.image(image, caption='Sunrise by the mountains')