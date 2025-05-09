# Estado de aprobación
while True:
    try:
        nota1=int(input("Ingrese una nota\n"))
        if nota1<0 or nota1>100:
            print("ingrese una nota entre 0 y 100")
        else:
            break
    except ValueError:
        print("Debe ser una cantidad numérica y entera")
if nota1>=60:
    print("Has aprobado")
else:
    print("Has reprobado")

# Calcular promedio
while True:
    entrada=input("ingrese las notas separadas por coma, recuerde enteros entre 0 y 100\n")
    notas_str=entrada.split(",")
    notas=[]
    notas_validas=True
    for nota in notas_str:
        nota=nota.strip()
        if nota.isdigit():
            nota_int=int(nota)
            if 0<=nota_int<=100:
                notas.append(nota_int)
            else:
                print(f"{nota_int} está fuera del rango 0-100.")
                notas_validas=False
        else:
            print(f"{nota} no es un número entero")
            notas_validas=False
    if notas_validas and len(notas)>0:
        break
    else:
        print("por favor ingresa una lista valida y con almenos una nota")
suma=0
for nota in notas:
    suma +=nota
promedio=suma/len(notas)
print(f"el promedio de {notas} es {promedio:.2f}")

# Contar calificaciones mayores
while True:
    try:
        nota_evaluar=int(input("Ingrese número para evaluar\n"))
        if 0<nota_evaluar<100:
            break
        else:
            print("debe estar entre 0 y 100 ")
    except ValueError:
        print("Debe ser un número entero")
contador=0
indice=0
while indice<len(notas):
    if notas[indice]>nota_evaluar:
        contador+=1
    indice+=1
print(f"la cantidad de notas mayores a {nota_evaluar} es {contador}")

# Verificar y contar calificaciones especificas
while True:
    try:
        nota_evaluar=int(input("Ingrese la nota a comparar\n"))
        if 0<nota_evaluar<100:
            break
        else:
            print("Debe estar entre 0 y 100")
    except ValueError:
        print("Debe ser un número entero")
contador=0
indicador=False
for nota in notas:
    if nota!=nota_evaluar:
        continue
    contador+=1
    indicador=True
if indicador:
    print(f"en la lista {notas} la nota {nota_evaluar} se encuentra {contador} veces")
else:
    print(f"la nota {nota_evaluar} no se encuentra en la lista {notas}")