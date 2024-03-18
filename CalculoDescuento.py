print("Abarrotes SUSANITA")

print("Liquidación de Productos")

print("LISTA DE PRODUCTOS A PAGAR")
print("Jabón -> $23")
print("Shampoo -> $41")
print("Espejo -> $21")
print("Perfume -> $42")
def calc_desc(total_mnt, porc_desc=10):
    descuento = (total_mnt * porc_desc) /100
    return descuento

valor_compra1 = calc_desc(127)
desc1 = calc_desc(valor_compra1)
total_final = valor_compra1 - desc1

print("\n **SUBTOTAL** ")

print(f"Valor de su compra es: $ {valor_compra1} \n ")
print(f"Descuento: {desc1} % \n ")
print(f"Pagar: $ {total_final: .2f} \n ")

valor_compra2 = calc_desc(250000)
porc_desc2 = 50
desc2 = calc_desc(valor_compra2, porc_desc2)
total_final2 = valor_compra2 - desc2

print("\n **TOTAL** ")
print(f"Subtotal de compra es: $ {valor_compra2} \n ")
print(f"Descuento del: {porc_desc2} % \n ")
print(f"Precio con descuento: $ {desc2} \n ")
print(f"TOTAL FINAL: $ {total_final2} \n")

print("GRACIAS POR SU COMPRA")