from colorama import Fore , Style , init

init(autoreset=True)

# [✓]
# [✗]
#  [i]

class Inventario:
	
	# Clase inventario para manejar el stock del usuario 
	
	def __init__(self):
		self.productos = {} # Diccionario de los productos
		
	def agregar_producto(self, producto , cantidad):
		"""
		Metodo para añadir un producto o aumentar su camtidad
		
		Se verifica si producto esta dentro del diccionario de la clase, si esta dentro del diccionario se añadira la cantidad dada por el usuario 
		Si no esta dentro del diccionario, se añade el producto con la cantidad dada por el usuario
		"""
		if producto in self.productos:
			self.productos[producto] += cantidad
		else:
			self.productos[producto] = cantidad
		
	def eliminar_producto(self, producto , cantidad):
		
		"""
		Metodo para reducir la cantidad dada por el usuario al producto que se elija
		
		Primero se verifica si la cantidad es mayor que la cantidad existente del producto, si es mayor se elimina el producto del diccionario de la clase, si no entonces se resta la cantidad dada por el usario 
		"""
		
		if self.productos[producto] < cantidad:
			del self.productos[producto]
		else:
			self.productos[producto] -= cantidad
	
	def mostrar_inventario(self):
		# Retorna el diccionario de la clase
		return dict(self.productos)
					
def mensaje_error(mensaje):
	# Para mensajes de error
	print(Fore.RED + Style.BRIGHT + "[✗] " + mensaje)
	
def mensaje_valido(mensaje):
	# Para mensajes que ejecuten una accion correcta
	print(Fore.GREEN + Style.BRIGHT + "[✓] " + mensaje)
	
def mensaje_info(mensaje):
	# Para mensajes informativos
	print(Fore.BLUE + Style.BRIGHT + "[i] " + mensaje)
	
def validar_cantidad():
	"""
	Funcion que verifica que se ingrese un numero tipo entero y que no sea negativo
	"""
	status = True
	while status:
		try:
			numero = int(input("Ingresa la cantidad del producto: "))
			if numero < 0: # Si es menor que 0 se repite el bucle
				mensaje_info("No se admiten numeros negativos")
				continue
			return numero # Si no es menor que 0 se finaliza el bucle y retorna la variable numero que contiene el dato deseado
		except ValueError: # Si hay un error por el valor, se imprime un mensaje de error y se repite el bucle
			mensaje_error("Ingresa una cantidad valida ")
	
def pedir_productos(inventario):
	"""
	Funcion para solicitar los productos a añadir o productos a modificar 
	
	"""
	status = True
	while status:
		print("Ingresa el nombre del producto o (salir) para terminar de seleccionar productos")
		
		producto = input(">...  ").lower()
		
		if producto == "salir":   # Si se ingresa la palabra "salir" entonces se imprimira los productos existentes y su cantidad
			
			if inventario.mostrar_inventario(): # Se verifica si el inventario tiene productos, si los tiene va a ordenar las claves del diccionario en orden alfabetico y una vez se tenga el diccionario ordenado se usa el bucle for para recorrerlo, obteniendo el valor de las claves previamente ordenadas e imprimiendo ambas cosas
				diccionario = inventario.mostrar_inventario()
				productos_ordenados = dict(sorted(diccionario.items()))
				for producto , cantidad in productos_ordenados.items():
					print(f"\nNombre: {producto} Cantidad: {cantidad}")
				mensaje_info("Saliendo.... ")
				status = False
						
			else: # Si el inventario esta vacio se informa y finaliza el bucle
				mensaje_info("Lista vacia, Saliendo... ")
				status = False
				
		elif  all(caracter.isalpha() or caracter.isspace() for caracter in producto): # Se recorre la entrads dada por el usuario verificando si es una letra o si es un espacio, si ambas se cumplen se retorna True
			
			if producto in inventario.mostrar_inventario(): # Una vez verificado que la entrada sea una palabra, entonces se verifica si ya pertenece al diccionario, si pertenece se solicita la cantidad a modificar del producto y se envia un mensaje para confirmarlo
				cantidad = validar_cantidad()
				mensaje_valido("Producto Modificado exitosamente ")
				inventario.agregar_producto(producto , cantidad)
			else: # Si el producto no pertenece al diccionario aun, se solicita la cantidad a agregar y se envia el mensaje de confirmacion
			    cantidad = validar_cantidad()
			    mensaje_valido("Producto Agregado exitosamente ")
			    inventario.agregar_producto(producto , cantidad)
		else: # Si la entrada no es ni "salir" ni es una palabra valida para un producto, se imprime el mensaje informativo y se vuleve a repetir el bucle
			mensaje_info("Nombre de producto no valido ")			    

def mostrar_inventario(inventario):
	"""
	Funcion para mostrar los productos del inventario, imprimiendo su nombre y la cantidad que hay
	"""
	if inventario.mostrar_inventario(): # Se verifica si el inventario tiene productos
		for producto , cantidad in inventario.mostrar_inventario().items(): # Se recorren los productos del inventario para luego imprimir su nombre y la cantidad disponible
			print(f"\nNombre: {producto} Cantidad: {cantidad}")
	else: # Si no hay productos en el inventario se imprime el mensaje informativo
		mensaje_info("Inventario Vacio ")
		
def eliminar_producto(inventario , producto):
	"""
	Funcion para eliminar cierta cantidad de un producto, pero si se excede a la cantidad disponible, se elimina el producto del inventario
	"""
	if not inventario.mostrar_inventario(): # Si no hay nada en el inventario se imprime el mensaje informativo
		mensaje_info("Inventario Vacio ")
	else: # Si hay productos en el inventario se evalua si el producto dado por el usario existe dentro del inventario
		if producto in inventario.mostrar_inventario(): # Si existe el producto en el inventario se solicita la cantidad a eliminar, se elimina la cantidad proporcionada o si la cantidad proporcionada es mayor entonces se elimina el producto del inventario
			cantidad = validar_cantidad()
			inventario.eliminar_producto(producto , cantidad)
			mensaje_valido("Modificado Exitosamente ")
		else: # Si no existe el producto se informa
			mensaje_info("El producto no esta en el inventario ")
		
def menu():
	# Funcion del menu 
	
	print("""
	Lista de Compras
	
	1. Agregar Productos
	2. Eliminar Producto
	3. Mostrar Inventario
	4. Salir
	""")
	
def main(inventario):
   # Funcion principal 
   status = True
   while status:
   	menu()
   	eleccion = input("Elige una opcion... : ") # Se solicita una opcion
   	if eleccion == "1": # Si es "1" se llama la funcion pedir_productos y se le pasa como argumento la instancia de la clase inventaril
   		pedir_productos(inventario)
   	elif eleccion == "2": # Si es "2" se solicita el nombre del producto y luego se llama la funcion eliminar_producto donde se le pasa como argumento la instancia de la clase inventario y el nombre del producto
   		producto = input("Ingresa el nombre del producto: ")
   		eliminar_producto(inventario , producto)
   	elif eleccion == "3": # Si es "3" se llama la funcion mostrar_inventario y se le pasa como argumento la instancia de la clase Inventario
   		mostrar_inventario(inventario)
   	elif eleccion == "4": # Si es "4" se manda un mensaje de despedida y se detiene el bucle cambiando a False la variable que controla el flujo
   		mensaje_info("Saliendo del programa... :) ")
   		status = False
   	else: # Si no es ninguna de las anteriores se informa que lo ingresado es invalido
   		mensaje_info("Opcion invalida ")
	
inventario = Inventario() # Se inicia una instancia de la clase Inventario

if __name__ == "__main__": # Condicional para verificar que el codigo se este ejecutando desde el mismo archivo
	main(inventario) # Se llama la funcion main donde se le pasa como argumento la instancia de la clasd Inventario definida anteriormente
#.
