print("*"*30)
print("Bienvenido a su fruver de confianza")
print("*"*30)
print()
producto=input("Qué producto compró?\n")
while True:
    try:
        precio=float(input("Cuál es el precio de la unidad?\n"))
        if precio<0:
            print("debe ser un numero mayor a cero\n")
        else:
            break
    except ValueError:
        print("debe ingresar un número y mayor a cero\n")
while True:
    try:
        cantidad=int(input("Qué cantidad compró?\n"))
        if cantidad<0:
            print("Debe ser una cantidad mayor a cero\n")
        else:
            break
    except ValueError:
        print("debe ser un número entero y mayor a cero\n")
while True:
    try:
        descuento=float(input("Qué porcentaje de descuento quiere aplicar?\n"))
        if descuento<0 or descuento>100:
            print("Debe ser una cantidad entre 0 y 100\n")
        else:
            break
    except ValueError:
        print("Debe ser un número entre 0 y 100\n")
total1=precio*cantidad
porcentaje=(total1*descuento)/100
total2=total1-porcentaje
print("*"*30)
print(f"El precio total por la compra de {producto} es: {total1}\nEL precio después de aplicar el descuento es: {total2:.2f}")
print("*"*30)