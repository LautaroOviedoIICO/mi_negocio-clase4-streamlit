import streamlit as st
from calculos import *
import pdf_presupuesto
from mi_negocio import *

st.title("Peter el del pan")
st.write("Buen día")

st.title("Peter el del pan")
st.write("Buen día")

nombre = st.text_input("Escribe tú nombre:")
numero = st.number_input("Pon tu número:", min_value=0, step=1)

RENGLONES = 3
nombres = []
cantidades = []
precios_unitarios = []
for i in range(RENGLONES):
    producto = st.selectbox(f"Producto {i + 1}", PRODUCTOS)
    cantidad = st.number_input(f"Cantidad {i + 1}", min_value=0, step=1)
    if cantidad > 0:
        pos = buscar_posicion(PRODUCTOS, producto)
        nombres.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(PRECIOS[pos])


forma_de_pago = st.radio("Forma de pago: ", ["Transferencia","Efectivo"])

fecha=st.date_input("Fecha:")

iva_elegir=st.selectbox("IVA: ", ["Excento","10,5%","21%"])
if iva_elegir == "Excento":
    iva_cargado = 0
elif iva_elegir == "10,5%":
    iva_cargado = 10.5
else:
    iva_cargado = 21

subtotalxproductousado=subtotalxproducto(precios_unitarios, cantidades)
subtotal_sin_descuento = sum(subtotalxproductousado)
descuento = descuento(subtotal_sin_descuento)
subtotal = subtotal(subtotal_sin_descuento,descuento)
total = total(subtotal, forma_de_pago, subtotal_sin_descuento, iva_cargado)
iva = iva(forma_de_pago, subtotal, subtotal_sin_descuento, iva_cargado)

archivo = pdf_presupuesto.armar_pdf(nombre, total, nombres, fecha, iva, descuento, precios_unitarios, numero, forma_de_pago, subtotal, cantidades, iva_cargado, subtotal_sin_descuento)

st.write(f"Pedido de: {nombre}.")
for i in range(len(nombres)):
    st.write(f"Producto {i + 1}: {nombres[i]} x {cantidades[i]}")
    st.write(f"Subtotal: ${subtotalxproductousado[i]}")
    st.write(f"Precio unitario: ${precios_unitarios[i]}")
if forma_de_pago == "Efectivo":
    st.write(f"Su descuento es: ${descuento}")
else:
    st.write(f"Su descuento es: 0%")
st.metric(f"El IVA aplicado es:", f"${iva}")
st.metric(f"El subtotal es:", f"${subtotal_sin_descuento}")
st.metric(f"El total es:", f"${total}")

if nombre=="" or numero==0 or len(cantidades)==0:
    st.warning("Por favor, ingrese su nombre, número o al menos un producto antes de descargar el PDF.")
else:
    st.download_button("Descargar PDF", archivo, file_name="factura.pdf", mime="application/pdf")
