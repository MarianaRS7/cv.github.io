import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Currículum Vitae", layout="wide")

col1, col2 = st.columns([1, 2.2]) # The ratio [1, 2] means col2 is twice as wide as col1.

with col1:
    st.image("/Users/anapa/Downloads/CV.jpeg", caption="", width=140)

    # Título
    st.markdown("## Mariana Ramírez Sánchez")

    # Información personal
    st.header("Información de Contacto")
    st.write("""
    *Celular:* +52 3310148845   
    *Email:* 0242526@up.edu.mx  
    *LinkedIn:* [Mariana Ramírez Sánchez](www.linkedin.com/in/mariana-ramírez-sánchez-b34635253)
    """)
    
    # Idiomas
    st.header("Idiomas")
    st.write("- Español (Nativo)")
    st.write("- Inglés (Avanzado)")
    st.write("- Chino mandarín (Básico)")

     # Habilidades
    st.header("Habilidades")
    st.write("- Trabajo en equipo")
    st.write("- Liderazgo")
    st.write("- Responsabilidad")
    st.write("- Adaptabilidad")
    st.write("- Comunicación efectiva")

    # Herramientas
    st.header("Herramientas")
    st.write("- Manejo avanzado de programas de Office")
    st.write("- Análisis de estados de situación financiera")
    st.write("- Manejo de herramientas contables")


with col2:
    # Educación
    st.header("Educación")
    st.subheader("Licenciatura en Administración y Finanzas")
    st.write("Universidad Panamericana | 2021 - Presente")

    # Experiencia profesional
    st.header("Experiencia Profesional")
    st.subheader("Merchandise - Disney Summer Cultural Exchange Program")
    st.write("Walt Disney World | Junio 2024 - Agosto 2024")
    st.write("Estrategias de ventas y marketing, manejo de inventarios, servicio al cliente.")

    st.subheader("Asesorías extracurriculares")
    st.write("CEDI A.C. | Octubre 2021 - Presente")
    st.write("Clases adicionales de matemáticas y química para alumnos de bachillerato.")

    # Experiencia internacional
    st.header("Experiencia Internacional")
    st.subheader("Purdue University 2022 HR Case Competition")
    st.write("GE Aerospace Human Resources Case - First Place")
   
    #Actividades académicas
    st.header("Actividades académicas")
    st.subheader("IMEF Universitario")
    st.write("Directora de Promoción y Desarrollo | Enero - Junio 2022")
    st.subheader("ENACTUS")
    st.write("Incubadora de proyectos: From the heart to Uganda | Enero - Julio 2022")
    st.subheader("Seminario de Mujeres Líderes")
    st.write("Participante | Enero - Mayo 2022")
    st.subheader("Equipo representativo de voleibol")
    st.write("Enero 2023 - Presente")

    #  Labor social
    st.header("Labor Social")
    st.write("- 80 horas de servicio en 'Estancia para la Senectud A.C.'")
    st.write("- Voluntariado y donación de artículos de limpieza para  'Ministerios de Amor A.C.'")
    st.write("- Miembro Ciudadanitos A.C. para Decembrinas 2022")

   

   