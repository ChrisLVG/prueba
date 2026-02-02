curso_dalto_optimizado= 1.5
curso_dalto_crudo= 3.5
curso_minimo= 2.5
curso_promedio_optimizado= 4
curso_promedio_crudo= 5
curso_maximo= 7
total_tiempo_optimizado= curso_dalto_optimizado + curso_minimo + curso_promedio_optimizado + curso_maximo
total_tiempo_crudo= curso_dalto_crudo + curso_minimo + curso_promedio_crudo + curso_maximo
def calcular_porcentaje(tiempo_curso, tiempo_total):
    porcentaje = (tiempo_curso / tiempo_total) * 100
    return int(porcentaje)

print("Curso Dalto Optimizado: ", curso_dalto_optimizado)
print("Curso Dalto Crudo: ", curso_dalto_crudo)
print("Curso Minimo: ", curso_minimo)
print("Curso Promedio Optimizado: ", curso_promedio_optimizado)
print("Curso Promedio Crudo: ", curso_promedio_crudo)
print("Curso Maximo: ", curso_maximo)
print("Total Tiempo Optimizado: ", total_tiempo_optimizado)
print("Total Tiempo Crudo: ", total_tiempo_crudo)
print("El curso de dalto optimizado representa el ", calcular_porcentaje(curso_dalto_optimizado, total_tiempo_optimizado), "% del total de tiempo optimizado")
print("El curso minimo representa el ", calcular_porcentaje(curso_minimo, total_tiempo_optimizado), "% del total de tiempo optimizado")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso minimo es de: ", abs(calcular_porcentaje(curso_dalto_optimizado, total_tiempo_optimizado) - calcular_porcentaje(curso_minimo, total_tiempo_optimizado)), "%")
print("El curso promedio representa el ", calcular_porcentaje(curso_promedio_optimizado, total_tiempo_optimizado), "% del total de tiempo optimizado")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso promedio es de: ", abs(calcular_porcentaje(curso_dalto_optimizado, total_tiempo_optimizado) - calcular_porcentaje(curso_promedio_optimizado, total_tiempo_optimizado)), "%")
print("El curso maximo representa el ",calcular_porcentaje(curso_maximo, total_tiempo_optimizado), "% del total de tiempo optimizado")
print("La diferencia en porcentaje entre el curso de dalto optimizado y el curso maximo es de: ",abs(calcular_porcentaje(curso_dalto_optimizado, total_tiempo_optimizado) - calcular_porcentaje(curso_maximo, total_tiempo_optimizado)), "%")



