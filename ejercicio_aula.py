asistencia=int(input("ingresa el numero de asistencias: "))
aula={}
for i in range (asistencia):
    nombre=input("ingresa el nombre del estudiante: ")
    edad=int(input("ingresa la edad del estudiante: "))
    aula[f"alumno{i+1}"]=nombre, edad

def ordenar_por_edad(aula):
    return dict(sorted(aula.items(), key=lambda item: item[1][1]))#Obtener un diccionario ordenado por edad

aula_ordenada=ordenar_por_edad(aula)
menor_edad=min(aula_ordenada.items(), key=lambda item: item[1][1])#Obtener el estudiante con menor edad
mayor_edad=max(aula_ordenada.items(), key=lambda item: item[1][1])#Obtener el estudiante con mayor edad
clave_menor_edad=menor_edad[0]#Extraer la clave del estudiante con menor edad
clave_mayor_edad=mayor_edad[0]#Extraer la clave del estudiante con mayor edad
aula_ordenada["Asistente"]=aula_ordenada.pop(clave_menor_edad)#cambiar la clave del estudiante con menor edad a "Asistente"
aula_ordenada["Profesor"]=aula_ordenada.pop(clave_mayor_edad)#cambiar la clave del estudiante con mayor edad a "Profesor"
contador=1
for key in list(aula_ordenada.keys()):
    if key=="Asistente":
        continue
    elif key=="Profesor":
        break
    else:
        aula_ordenada[f"alumno{contador}"]=aula_ordenada.pop(key)#Renombrar las claves de los estudiantes restantes  
        contador+=1

print("----- Datos del aula -----")
for clave, valor in aula_ordenada.items():
    if clave=="Asistente":
        print(f" El asistente es {valor[0]} y tiene {valor[1]} años")
    elif clave=="Profesor":
        print(f" El profesor es {valor[0]} y tiene {valor[1]} años")

print("----- Lista del aula -----")
for clave, valor in aula_ordenada.items():
    print(f"{clave}: {valor[0]}, {valor[1]} años")