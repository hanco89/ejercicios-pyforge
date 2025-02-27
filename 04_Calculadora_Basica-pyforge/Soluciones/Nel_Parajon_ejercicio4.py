
#se usa float en vez de int ya que permite al usuario añadir tanto enteros como decimales
#si usasemos int el usuario no podría añadir decimales
def suma(num1: float, num2: float):
    """Función que realiza una suma
    Arguments:
        num1(float): número 1 introducido por el usuario
        num2(float): número 2 introducido por el usuario
    Return:
        float: resultado de la suma
    """
    return num1 + num2

def resta(num1: float, num2: float):
    """Función que realiza una resta
    Arguments:
        num1(float): número 1 introducido por el usuario
        num2(float): número 2 introducido por el usuario
    Return:
        float: resultado de la resta
    """
    return num1 - num2

def multiplicacion(num1: float, num2: float):
    """Función que realiza una multiplicación
    Arguments:
        num1(float): número 1 introducido por el usuario
        num2(float): número 2 introducido por el usuario
    Return:
        float: resultado de la multiplicación
    """
    return num1 * num2

def division(num1: float, num2: float):
    """Función que realiza una división
    Arguments:
        num1(float): número 1 introducido por el usuario
        num2(float): número 2 introducido por el usuario
    Returns:
        float: resultado de la división
    Raises:
        ZeroDivisionError: error al dividir entre cero
    """
    try:
        return num1 / num2
    except ZeroDivisionError as e: #usamos la excepción division entre cero para capturar el error
        return f"Error: {e} - No se puede dividir entre cero" #lanzamos el error de la excepción + un mensaje explicativo

def obtener_numero(mensaje: str) -> float:
    """Solicita un número al usuario manejando los errores de entrada."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Ingresa un número válido.")

def menu():
    """Muestra el menú y permite al usuario realizar cálculos."""
    while True:
        print("\nIntroduce dos números o escribe '0' para salir.")

        num1 = obtener_numero("Introduce el primer número: ")
        if num1 == 0:
            print("Gracias por usar la calculadora. Saliendo...")
            break

        num2 = obtener_numero("Introduce el segundo número: ")

        print("\nElige la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        try:
            match opcion:
                case '1':
                    print(f"Resultado: {suma(num1, num2)}")
                case '2':
                    print(f"Resultado: {resta(num1, num2)}")
                case '3':
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                case '4':
                    print(f"Resultado: {division(num1, num2)}")
                case '0':
                    print("Gracias por usar la calculadora. Saliendo...")
                    break
                case _:
                    print("Opción no válida, intenta de nuevo.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    menu()
        
