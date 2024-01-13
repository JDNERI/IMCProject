def input_number(answer):
    while True:
        try:
            num = float(input(answer))
            if num:
                return num
            else:
                print("No has contestado correctamente. Intentalo de nuevo.")
        except ValueError:
            print("No has contestado correctamente. Intentalo de nuevo.")

print("***********************************************************")
print("*                     CALCULADORA IMC                     *")
print("***********************************************************")
print("\n")

print("VAMOS A CALCULAR TU IMC, RESPONDE LAS SIGUIENTES PREGUNTAS")
print("\n")


name = ""
while not name.strip():
    name = input("Introduce tu nombre: ")

last_name_1 = ""
while not last_name_1.strip():
    last_name_1 = input("Introduce tu apellido paterno: ")

last_name_2 = ""
while not last_name_2.strip():
    last_name_2 = input("Introduce tu apellido materno: ")

age = input_number("Introduce tu edad: ")
peso = input_number("Introduce tu peso en kg: ")
height = input_number("Introduce tu estatura en metros: ")

print("\n")

imc = peso / (height * height)

print(f"Hola {name} {last_name_1} {last_name_2}")
print(f"Edad: {age:.0f} años")

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.9:
    print("Estas bajo de peso")
elif imc >= 19 and imc <= 24.9:
    print("Estas en tu peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Tienes sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Tienes obesidad leve")
elif imc >= 35 and imc <= 39.9:
    print("Tienes obesidad media")
elif imc >= 40:
    print("Tienes obesidad morbida")