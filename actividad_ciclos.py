#Solicitar información
nombre=input ("nombre completo: ")
materias=5
#Hacer un ciclo, pedir datos y sumar la calificación
contador=1
sumatoria=0
while contador<= materias:
    nombre_materia=input("Ingresa el nombre de la ("+str(contador)+") materia: ")
    calificacion=float(input("calificacion obtenidas en "+str(nombre_materia)+": "))
    # Aquí sumamos la calificación a la sumatoria
    sumatoria=sumatoria+calificacion
    #Aumentar el contador para no hacer un ciclo infinito
    contador=contador+1
#Hacer cálculos e imprimir resultados
promedio=sumatoria/materias
print("***RESULTADOS***")
print(f'Hola, {nombre} tienes un promedio de {promedio} en el 5to semestre.')