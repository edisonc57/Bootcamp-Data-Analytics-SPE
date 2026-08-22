import streamlit as st 

st.title ("Bootcamp-Data-Analytics-SPE")
st.sidebar.title('Parámetros')

modulos= st.sidebar.selectbox('Selecciona un módulo', ['Introducción a variables', 'Funciones'])

if modulos == 'Introducción a variables':

    pozo =  "SPE-001"
    Petroleo_bpd= 1250
    agua_bpd = 350.50
    status = True
    
    st.write(pozo)
    st.write(Petroleo_bpd)
    st.write(agua_bpd)
    st.write(status)
elif modulos == 'Funciones':

    def calcular_caudal_vogel(caudal_maximo= 1000, presion_yacimiento= 3000, presion_fondo=0, decimales=2):

        relacion_presion = presion_fondo / presion_yacimiento
        caudal = caudal_maximo * (1 - 0.2 * relacion_presion - 0.8 * relacion_presion**2 )

        return round(caudal, decimales)

caudal_maximo= st.number_input ('Ingrese el caudal máximo')
presion_yacimiento = st.number_input('Ingrese la presión del yacimiento')
presión_fondo = st.number_input('Ingese la presion de fondo fluyente')
decimales = st.slider('Seleccione la cantidad de decimales para su resultado')

  caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)

  st.write("El caudal es:", caudal)

elif  modulos == "POO": 

  class Pozo:
  
    def __init__(self,nombre, campo, petroleo, agua):
      self.nombre = nombre
      self.campo = campo
      self.petroleo = petroleo
      self.agua = agua
  
    def mostrar_informacion(self):
      st.write("Pozo:", self.nombre)
      st.write("Campo:", self.campo)
      st.write("Petroleo:", self.petroleo, "BPD")
      st.write("Agua:", self.agua, "BPD")
  
    def produccion_total(self):
      total_produccion = self.petroleo + self.agua
      return total_produccion
  
    def proyectar_produccion(self, dias=30):
      produccion_proyectada = (self.petroleo + self.agua)*dias
      return produccion_proyectada

  nombre_pozo = st.text_input("Ingrese el nombre del pozo")
  campo_pozo = st.text_input("Ingrese el campo al que pertenece el pozo")
  petroleo = st.number_input("Ingrese producción de petróleo", min_value = 0, max_value = 5000, value =1000)
  agua = st.number_input("Ingrese producción de agua", min_value = 0, max_value = 5000, value =200)

  pozo = Pozo(nombre_pozo,campo_pozo,petroleo,agua)

  st.write(pozo.mostrar_informacion())

  st.write(pozo.produccion_total())

  dias = st.number_input("Ingrese los días a proyectar", min_value = 0, max_value = 365, value =30)
  st.write(pozo.proyectar_produccion(dias))
