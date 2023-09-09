#Casteo de Variables

num1 = 4.5
#Casting de variables de float a int
num2 = int(4.5)
print (num2)

number = "3"

number1=int("3")
print (number1)
print (type(number1))

#Crear Formulario
name = input("Ingrese su nombre ")
apellido = input ("Ingrese su apellido ")
edad = input ("Cual es su edad ")
estudio = input ("Que esta estudiando en el momento ")
universidad = input ("Donde esta estudiando ")
semestre = input ("En que semestre se encuentra actualmente ")
residencia = input ("Donde Vive ")
transporte = input ("Que medio de transporte utiliza ")

print ("---------------------------------------------------------------")
print ("Su nombre es: " , name)
print ("Su apellido es: " , apellido)
print ("Su edad es: " , edad)
print ("Usted se encuentra estudiando: " , estudio)
print ("En la universidad: " , universidad)
print ("Actualmente esta cursando el: " , semestre)
print ("Se encuentra viviendo en: " , residencia)
print ("Utiliza el siguiente medio de transporte: " , transporte)
print ("---------------------------------------------------------------")