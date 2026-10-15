def buscar_posicion(lista,nombre):
    for i in range(len(lista)):
        if lista[i]==nombre:
            return i
    return -1
def subtotalxproducto(precio,cantidad):
    subtotalxproducto=[]
    for i in range(len(precio)):
        subtotalxproducto.append(precio[i]*cantidad[i])
    return subtotalxproducto
def descuento(subtotal_sin_descuento):
    descuento = subtotal_sin_descuento*10/100
    return descuento
def iva(forma_de_pago, subtotal, subtotal_sin_descuento, iva):
    if forma_de_pago == "Efectivo":
        return round(subtotal*iva/100,2)
    else:
        return round(subtotal_sin_descuento*iva/100,2)
def subtotal(subtotal_sin_descuento,descuento):
    subtotal = subtotal_sin_descuento-descuento
    return subtotal
def total(subtotal, forma_de_pago, subtotal_sin_descuento, iva_cargado):
    if forma_de_pago == "Efectivo":
        return round(subtotal+subtotal*iva_cargado/100,2)
    else:
        return round(subtotal_sin_descuento+subtotal_sin_descuento*iva_cargado/100,2)