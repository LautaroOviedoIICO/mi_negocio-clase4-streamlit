from fpdf import FPDF
logo="logo.png"
nombre_negocio="Peter el del pan"

def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def armar_pdf(cliente, total, productos, fecha, iva, descuento, precio_individual, numero, formadepago, subtotal, cantidad, iva_cargado, subtotal_sin_descuento):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(logo, x=12, y=12, w=35)

    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, nombre_negocio, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Presupuesto N° {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)
 
    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    for i in range(len(productos)):
        renglon(pdf, f"{productos[i]} x {cantidad[i]}", f"${precio_individual[i]:.2f} c/u")
        renglon(pdf, "Subtotal", f"${precio_individual[i]*cantidad[i]:.2f}")
    pdf.ln(4)
 
    renglon(pdf, "Subtotal completo", f"${subtotal_sin_descuento:.2f}")
    renglon(pdf, "Forma de pago", formadepago)
    if formadepago == "Efectivo":
        renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, f"IVA {iva_cargado}%", f"${iva:.2f}")
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color("#9f139f")
    renglon(pdf, "TOTAL", f"${total:.2f}")
    pdf.set_text_color(0,0,0)


    pdf.ln(10)
    pdf.set_font("Arial", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.", new_x="LMARGIN", new_y="NEXT")

    pdf.output("factura.pdf")
    return bytes(pdf.output())