# Estado de aprobación
while True:
    try:
        nota=int(input("Ingrese la nota:\n"))
        if nota<0 or nota>100:
            print("Debe ser un numero entero entre 0 y 100")
        else:
            break
    except ValueError:
        print("Ingresa un numero entero entre 0 y 100")
if nota>=60:
    print("Has aprobado\n")
else:
    print("Has reprobado\n")

# Calculo promedio
while True:
    lista=input("Ingrese las notas, separadas por comas:\n").split(',')
    calificaciones=[]
    suma=0
    try:
        for nota in lista:
            nota=int(nota)
            if 0<=nota<=100:
                calificaciones.append(nota)
                suma+=nota
            else:
                print("Deben ser números enteros entre 0 y 100")
                break
        else: 
            break
    except ValueError:
        print("Deben ser números enteros entre 0 y 100")
promedio=suma/len(calificaciones)
print(f"El promedio de las notas: {calificaciones} es: {promedio:.2f}\n")

#Conteo calificaciones mayores
while True:
    try:
        nota_comparar=int(input("Ingrese la nota a comparar en la lista\n"))
        if 0<=nota_comparar<=100:
            break
        else:
            print("Debe ser un numero entero entre 0 y 100.")
    except ValueError:
        print("debes ingresar un numero entero entre 0 y 100")
contador=0
i=0
while i<len(calificaciones):
    if calificaciones[i]>nota_comparar:
        contador+=1
    i+=1
print(f"la cantidad de notas mayores a {nota_comparar} es {contador}")

# verificacion y conteo de calificacion especifica
while True:
    try:
        nota_especifica=int(input("Ingrese la nota que desea evaluar\n"))
        iguales=0
        if 0<=nota_especifica<=100:
            for nota in calificaciones:
                if nota!=nota_especifica:
                    continue
                else:
                    iguales+=1
            break
        else:
            print("Debe ser un numero entre 0 y 100\n")
    except ValueError:
        print("Deben ser un numero entero entre 0 y 100")
print(f"La cantidad de notas iguales a {nota_especifica} es {iguales}")