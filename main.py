import random

alumnos = []

def agregarAlumno (nombre, edad, telefono=None, asistencia=0):
    alumnos.append({
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
        "asistencia": asistencia
    })

nombre = ["José", "María", "Ramiro", "Tomas"]

for alum in range(1,10):
    alumno = nombre[random.randint(0,3)]
    edad = random.randint(17, 19)
    #agregarAlumno(alumno,edad)
    agregarAlumno(edad=edad, nombre=alumno)

#Muestra todos los elementos de la lista
#print(alumnos)

# Muestra solo los nombres y su asistencia
for alum in alumnos:
    print("Nombre: {}     Asistencia: {}".format(alum["nombre"], alum["asistencia"]))
