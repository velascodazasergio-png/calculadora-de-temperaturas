def celsius_a_fahrenheit(c):
    return (c * 9/5) +32

def fahrenheit_a_celsius(f):
    return (f-32)*(5/9)

def celsius_a_kelvin(c):
    return c+273.15

def kelvin_a_celsius(k):
    return k-273.15

def fahrenheit_a_kelvin(f):
    return (f-32)*(5/9)+273.15

def kelvin_a_fahrenheit(k):
    return (k-273.15)*(9/5)+32

def menu():
    while True:
        print("-----------CALCULADORA DE TEMPERATURAS-------------")
        print("1. °C - °F")
        print("2. °F - °C")
        print("3. °C - °K")
        print("4. °K - °C")
        print("5. °F - °K")
        print("6. °K - °F")
        print("0. Salir")
        print("---------------------------------------------------")

        opcion = int(input("Digite una opcion: "))

        if opcion == 1:
            c = float(input("Cantidad de °C a convertir: "))
            print (f"Resultado: {celsius_a_fahrenheit(c)}°F")

        elif opcion == 2:
            f = float(input("Cantidad de °F a convertir: "))
            print(f"Resultado: {fahrenheit_a_celsius(f)}")
        elif opcion == 3:
            c = float(input("Cantidad de °C a convertir: "))
            print(f"Resultado: {celsius_a_kelvin(c)}")
        elif opcion == 4:
            k = float(input("Cantidad de °K a convertir: "))
            print(f"Resultado: {kelvin_a_celsius(k)}")
        elif opcion == 5:
            f = float(input("Cantidad de °F a convertir: "))
            print(f"Resultado: {fahrenheit_a_kelvin(f)}")
        elif opcion == 6:
            k = float(input("Cantidad de °K a convertir: "))
            print(f"Resultado: {kelvin_a_fahrenheit(k)}")
        elif opcion == 0:
            print("saliendo de la calculadora...")
            break
        else:
            print("Opcion no valida")

menu()