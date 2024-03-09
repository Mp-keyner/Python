### Ejercicio 1: Menú Simple

_Objetivo:_ Crear un menú simple que pregunte al usuario si desea una pizza vegetariana o no vegetariana.

### Ejercicio 2: Elección de Ingredientes

_Objetivo:_ Permitir al usuario elegir un ingrediente adicional, además de la mozzarella y el tomate, basándose en su elección de tipo de pizza.

### Ejercicio 3: Validación de Ingredientes

_Objetivo:_ Añadir validación para asegurar que el usuario elija un ingrediente válido.

### Ejercicio 4: Menú con Opciones Múltiples

_Objetivo:_ Crear un menú que permita al usuario elegir entre diferentes tipos de pizzas, incluyendo opciones vegetarianas y no vegetarianas, y validar la elección.

### Ejercicio 5: Personalización de Pizzas

_Objetivo:_ Permitir al usuario personalizar su pizza con múltiples ingredientes, incluyendo la opción de elegir entre vegetariana y no vegetariana.

# lo que te ayudara

El método .split() en Python es una función incorporada que opera en cadenas de texto, dividiéndolas en una lista de cadenas. Este método rompe la cadena en base a un separador dado. Si no se especifica ningún separador, el espacio en blanco es el separador predeterminado. La sintaxis básica del método .split() es str.split(separator, maxsplit), donde separator es el carácter o cadena que se utilizará para dividir la cadena original, y maxsplit es un parámetro opcional que indica el número máximo de divisiones a realizar [3].

### Ejemplo de uso de .split():

python

```
texto = "Hola mundo, bienvenido a Python"
palabras = texto.split()
print(palabras)
# Salida: ['Hola', 'mundo,', 'bienvenido', 'a', 'Python']
```

En este ejemplo, la cadena texto se divide en palabras, utilizando el espacio en blanco como separador, y el resultado es una lista de palabras.

### Método .lower()

El método .lower() en Python convierte todos los caracteres de la cadena a minúsculas. Este método es útil para normalizar texto, especialmente en operaciones de comparación de cadenas donde la diferencia entre mayúsculas y minúsculas puede ser significativa.

### Ejemplo de uso de .lower():

```
python
texto = "Hola Mundo"
texto_minusculas = texto.lower()
print(texto_minusculas)

# Salida: "hola mundo"
```

En este ejemplo, la cadena texto se convierte a minúsculas, resultando en "hola mundo".

Ambos métodos, .split() y .lower(), son herramientas fundamentales en el manejo de cadenas de texto en Python, permitiendo realizar tareas comunes como la división de texto en partes más pequeñas y la normalización de texto para facilitar comparaciones y análisis de texto.

---

# Operador In

El operador in en Python se utiliza para verificar si un valor específico está presente en una secuencia, como listas, cadenas de texto (strings), tuplas, entre otros. Este operador devuelve True si el valor se encuentra en la secuencia y False si no se encuentra. Es una forma eficiente de realizar búsquedas o verificaciones de pertenencia en colecciones de datos [3].

### Ejemplos de uso del operador in:

#### Con listas:

```
python
numeros = [1, 2, 3, 4, 5]
print(3 in numeros) # Muestra True
print(12 not in numeros) # Muestra True
```

En este ejemplo, 3 in numeros verifica si el número 3 está en la lista numeros, lo cual es cierto, por lo que devuelve True. Por otro lado, 12 not in numeros verifica si el número 12 no está en la lista, lo cual es cierto, por lo que devuelve True.

#### Con cadenas de texto:

```
python
saludo = "Hola Mundo"
print("Mundo" in saludo) # Muestra True
print("mundo" in saludo) # Muestra False
```

Aquí, "Mundo" in saludo verifica si la subcadena "Mundo" está en la cadena saludo, lo cual es cierto, por lo que devuelve True. Sin embargo, "mundo" in saludo verifica si la subcadena "mundo" (en minúsculas) está en saludo, lo cual es falso debido a que las cadenas en Python son sensibles a mayúsculas y minúsculas, por lo que devuelve False.

### Uso del operador not in:

El operador not in es simplemente la negación del operador in. Se utiliza para verificar si un valor no está presente en una secuencia.

```
python
print("Python" not in saludo) # Muestra True
```

En este caso, "Python" not in saludo verifica si la subcadena "Python" no está en la cadena saludo, lo cual es cierto, por lo que devuelve True.

El operador in es muy útil para realizar búsquedas rápidas y verificaciones de pertenencia en colecciones de datos en Python, facilitando la escritura de código más limpio y legible.
