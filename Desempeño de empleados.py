#Desempeño de empleados 

def registrar_datos(num_empleados=3):
    equipo = []
    for i in range(num_empleados):
        nombre = input(f"Ingrese el nombre del empleado {i+1}: ")
        desempeno = []
        for semana in range(4):  # indicadores para 4 semanas
            valor = float(input(f"Ingrese desempeño semana {semana+1} (0-10): "))
            desempeno.append(valor)
        empleado = {"nombre": nombre, "desempeno": tuple(desempeno)}
        equipo.append(empleado)
    return equipo

def calcular_promedio(empleado):
    return sum(empleado["desempeno"]) / len(empleado["desempeno"])

def clasificar_desempeno(promedio):
    if promedio >= 8.5:
        return "Sobresaliente"
    elif promedio < 5:
        return "Bajo"
    else:
        return "Aceptable"

def mostrar_reporte(equipo):
    print("\nREPORTE FINAL DE DESEMPEÑO")
    print(f"{'Nombre':<20}{'Promedio':<10}{'Estado'}")
    for empleado in equipo:
        promedio = calcular_promedio(empleado)
        estado = clasificar_desempeno(promedio)
        print(f"{empleado['nombre']:<20}{promedio:<10.2f}{estado}")

# Ejecución del programa (mínimo 3 empleados)
equipo = registrar_datos(5)
mostrar_reporte(equipo)
