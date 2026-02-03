curso_dalto_optimizado= 1.5
curso_dalto_crudo= 3.5
curso_minimo= 2.5
curso_promedio_optimizado= 4
curso_promedio_crudo= 5
curso_maximo= 7
def calcular_porcentaje(tiempo_curso, tiempo_total):
    porcentaje = (tiempo_curso / tiempo_total) * 100
    return round(porcentaje,2)

print("Curso Dalto Optimizado: ", curso_dalto_optimizado)
print("Curso Dalto Crudo: ", curso_dalto_crudo)
print("Curso Minimo: ", curso_minimo)
print("Curso Promedio Optimizado: ", curso_promedio_optimizado)
print("Curso Promedio Crudo: ", curso_promedio_crudo)
print("Curso Maximo: ", curso_maximo)
print("----- Porcentajes -----")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso minimo es de: ", 100-calcular_porcentaje(curso_dalto_optimizado,curso_minimo) , "%")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso promedio es de: ", 100-calcular_porcentaje(curso_dalto_optimizado,curso_promedio_optimizado), "%")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso maximo es de: ", 100-calcular_porcentaje(curso_dalto_optimizado,curso_maximo), "%")
print("----- Comparacion Crudo vs Optimizado -----")
print("El curso de dalto optimizado representa una diferencia de ",round(100-calcular_porcentaje(curso_dalto_optimizado,curso_dalto_crudo), 2), "% con el curso de dalto crudo")
print("El curso promedio optimizado representa una diferencia de ", round(100-calcular_porcentaje(curso_promedio_optimizado, curso_promedio_crudo), 2), "% con el curso promedio crudo")
print("----- Equivalencias -----")
print("Ver 10 horas del curso optimizado de dalto seria el equivalente a ver ", round((10 / curso_dalto_optimizado) * curso_minimo,1), " horas del curso minimo")
print("Ver 10 horas del curso optimizado de dalto seria el equivalente a ver ", round((10 / curso_dalto_optimizado) * curso_promedio_optimizado,1), " horas del curso promedio optimizado")
print("Ver 10 horas del curso optimizado de dalto seria el equivalente a ver ", round((10 / curso_dalto_optimizado) * curso_maximo,1), " horas del curso maximo")