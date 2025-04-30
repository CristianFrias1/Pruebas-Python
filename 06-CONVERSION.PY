resultado = input("Ingresa Tu Edad:")
print(type(resultado))
# Print(resultado + 22) Esto no funciona porque no se puede sumar un string con un int
# Para convertir un string a un int se usa la funcion int()
numero = int(resultado)
print(numero + 2)
str(22) # Toma Cualquier Tipo De Dato Y Lo Convierte A String
float("22.13") # Toma Cualquier Tipo De Dato Y Lo Convierte A Float (Numero Decimal)
bool("Un String") # Lo Trasforma A Un False O Un True Y La Mayoria De Las Veces Es True
# Van A Existir 4 Valores Falsos En Python:
# 1. Bool(false)
# 2. Int(0)
# 3. String("") Vacío
# 4. None
# Para Evaluar En Falso Utilizare:
bool(False)
bool("")
bool(None)
bool(0)