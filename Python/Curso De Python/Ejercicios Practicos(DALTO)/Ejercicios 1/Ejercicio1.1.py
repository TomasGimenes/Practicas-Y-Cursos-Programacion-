#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
dalto_curso_crudo = 3.5
otros_cursos_promedio_crudo = 5

#material reducido
material_reducido_curso_dalto = 100 - dalto_curso * 1000 // dalto_curso_crudo / 10
material_reducido_cursos_promedios = 100 - otros_cursos_promedio / otros_cursos_promedio_crudo * 100

#Diferencias con los cursos
diferencias_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencias_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencias_con_promedios = 100 - dalto_curso / otros_cursos_promedio * 100

#mostrando la diferencia de duracion(Ejercicio A)
print("El curso de dalto dura:")
print(f" - un {diferencias_con_min}% menos que el mas rapido")
print(f" - un {diferencias_con_max}% menos que el mas Lento")
print(f" - un {diferencias_con_promedios}% menos que el promedio")
print("............................................")

#mostrando el procentaje de material inservible borrado(Ejercicio B)
print(f"El material inservible que se reduce en el curso de dalto es de {material_reducido_curso_dalto}%")
print(f"El material inservible que se reduce en los cursos promedios es de {material_reducido_cursos_promedios}%")
print("............................................")

#Mostrando diferencias si los cursos duraran 10 horas(Ejecicio C)
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
print("............................................")

