tasacomision = 0.13

#Pedir los datos del vendedor
nombre = input("Por favor, dime tu nombre: ")
ventas = int(input("Diga sus ventas totales del mes: "))

#Calcular la comision
comision = round(ventas * tasacomision,2)

#Presentar en pantalla
print(f"Hola {nombre}, tus comisiones de este mes son de ${comision}")
