def show_welcome_message():
    print("Proyecto del curso Programación I")
    print("Desarrollado por: [Tu Nombre] [Tu Identificación]")

def count_vowels(sentence):
    vowels = 'aeiouáéíóúü'
    sentence = sentence.lower()
    vowel_count = {v: 0 for v in vowels}
    for char in sentence:
        if char in vowel_count:
            vowel_count[char] += 1
    return vowel_count

def is_narcissistic(number):
    digits = [int(d) for d in str(number)]
    n = len(digits)
    return sum(d**n for d in digits) == number

def decimal_to_binary(number):
    return bin(number)[2:]

def is_divisible_by_11(number):
    digits = [int(d) for d in str(number)]
    odd_sum = sum(digits[i] for i in range(0, len(digits), 2))
    even_sum = sum(digits[i] for i in range(1, len(digits), 2))
    return (odd_sum - even_sum) % 11 == 0

# Inicio del flujo del programa
show_welcome_message()

while True:
    print("\nMenú:")
    print("a) Vocales")
    print("b) Número Narcisista")
    print("c) Binario")
    print("d) Divisible por 11")
    print("e) Salir")
    
    option = input("Seleccione una opción: ").strip().lower()
    
    if option == 'a':
        sentence = input("Ingrese una oración: ")
        vowel_count = count_vowels(sentence)
        print("Conteo de vocales:", vowel_count)
    
    elif option == 'b':
        number = int(input("Ingrese un número entero: "))
        if is_narcissistic(number):
            print(f"{number} es un número narcisista.")
        else:
            print(f"{number} no es un número narcisista.")
    
    elif option == 'c':
        number = int(input("Ingrese un número entero: "))
        print(f"El número {number} en binario es {decimal_to_binary(number)}.")
    
    elif option == 'd':
        number = int(input("Ingrese un número entero: "))
        if is_divisible_by_11(number):
            print(f"{number} es divisible por 11.")
        else:
            print(f"{number} no es divisible por 11.")
    
    elif option == 'e':
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")
