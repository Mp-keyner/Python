En Python, los objetos de tipo str (cadenas de texto) tienen una serie de métodos incorporados que permiten realizar diversas operaciones sobre ellas. A continuación, te proporciono una descripción de algunos de los métodos más comunes y útiles que puedes utilizar con cadenas de texto en Python:

### 1. capitalize()

- _Función_: Convierte la primera letra de la cadena a mayúscula y el resto a minúsculas.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.capitalize()) # Salida: "Hola mundo"

### 2. casefold()

- _Función_: Convierte la cadena a minúsculas, aplicando una normalización de Unicode para comparaciones de texto.
- _Ejemplo_:
  python
  s = "Hola Mundo"
  print(s.casefold()) # Salida: "hola mundo"

### 3. center(width[, fillchar])

- _Función_: Centra la cadena dentro de un campo de ancho width, rellenando con fillchar (por defecto es un espacio).
- _Ejemplo_:
  python
  s = "hola"
  print(s.center(10)) # Salida: " hola "

### 4. count(sub[, start[, end]])

- _Función_: Cuenta el número de ocurrencias de sub en la cadena, desde start hasta end.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.count("o")) # Salida: 2

### 5. encode(encoding="utf-8", errors="strict")

- _Función_: Codifica la cadena en bytes usando el encoding especificado.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.encode("utf-8")) # Salida: b'hola mundo'

### 6. endswith(suffix[, start[, end]])

- _Función_: Verifica si la cadena termina con suffix, desde start hasta end.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.endswith("mundo")) # Salida: True

### 7. expandtabs(tabsize=8)

- _Función_: Reemplaza las tabulaciones en la cadena con espacios, usando tabsize como el número de espacios por tabulación.
- _Ejemplo_:
  python
  s = "hola\tmundo"
  print(s.expandtabs(4)) # Salida: "hola mundo"

### 8. find(sub[, start[, end]])

- _Función_: Devuelve el índice más bajo donde sub se encuentra en la cadena, desde start hasta end. Retorna -1 si no se encuentra.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.find("mundo")) # Salida: 5

### 9. format(\*args, \*\*kwargs)

- _Función_: Formatea la cadena usando args y kwargs como valores de reemplazo.
- _Ejemplo_:
  python
  s = "hola {nombre}"
  print(s.format(nombre="mundo")) # Salida: "hola mundo"

### 10. index(sub[, start[, end]])

- _Función_: Similar a find(), pero lanza una excepción ValueError si sub no se encuentra.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.index("mundo")) # Salida: 5

### 11. isalnum()

- _Función_: Verifica si todos los caracteres de la cadena son alfanuméricos.
- _Ejemplo_:
  python
  s = "hola123"
  print(s.isalnum()) # Salida: True

### 12. isalpha()

- _Función_: Verifica si todos los caracteres de la cadena son letras.
- _Ejemplo_:
  python
  s = "hola"
  print(s.isalpha()) # Salida: True

### 13. isdigit()

- _Función_: Verifica si todos los caracteres de la cadena son dígitos.
- _Ejemplo_:
  python
  s = "123"
  print(s.isdigit()) # Salida: True

### 14. islower()

- _Función_: Verifica si todos los caracteres de la cadena son minúsculas.
- _Ejemplo_:
  python
  s = "hola"
  print(s.islower()) # Salida: True

### 15. isspace()

- _Función_: Verifica si todos los caracteres de la cadena son espacios en blanco.
- _Ejemplo_:
  python
  s = " "
  print(s.isspace()) # Salida: True

### 16. istitle()

- _Función_: Verifica si la cadena tiene un formato de título, es decir, cada palabra comienza con una letra mayúscula y el resto son minúsculas.
- _Ejemplo_:
  python
  s = "Hola Mundo"
  print(s.istitle()) # Salida: True

### 17. isupper()

- _Función_: Verifica si todos los caracteres de la cadena son mayúsculas.
- _Ejemplo_:
  python
  s = "HOLA"
  print(s.isupper()) # Salida: True

### 18. join(iterable)

- _Función_: Une todos los elementos de iterable en una cadena, separados por la cadena original.
- _Ejemplo_:
  python
  s = "-"
  print(s.join(["hola", "mundo"])) # Salida: "hola-mundo"

### 19. ljust(width[, fillchar])

- _Función_: Alinea la cadena a la izquierda dentro de un campo de ancho width, rellenando con fillchar (por defecto es un espacio).
- _Ejemplo_:
  python
  s = "hola"
  print(s.ljust(10)) # Salida: "hola "

### 20. lower()

- _Función_: Convierte todos los caracteres de la cadena a minúsculas.
- _Ejemplo_:
  python
  s = "HOLA MUNDO"
  print(s.lower()) # Salida: "hola mundo"

### 21. lstrip([chars])

- _Función_: Elimina los caracteres especificados en chars del inicio de la cadena.
- _Ejemplo_:
  python
  s = " hola"
  print(s.lstrip()) # Salida: "hola"

### 22. partition(sep)

- _Función_: Divide la cadena en una tupla de tres elementos: la parte antes de sep, sep mismo, y la parte después de sep.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.partition(" ")) # Salida: ('hola', ' ', 'mundo')

### 23. replace(old, new[, count])

- _Función_: Reemplaza todas las ocurrencias de old por new en la cadena, hasta count veces.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.replace("mundo", "Python")) # Salida: "hola Python"

### 24. rfind(sub[, start[, end]])

- _Función_: Similar a find(), pero busca desde el final de la cadena.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.rfind("o")) # Salida: 8

### 25. rindex(sub[, start[, end]])

- _Función_: Similar a index(), pero busca desde el final de la cadena.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.rindex("o")) # Salida: 8

### 26. rjust(width[, fillchar])

- _Función_: Alinea la cadena a la derecha dentro de un campo de ancho width, rellenando con fillchar (por defecto es un espacio).
- _Ejemplo_:
  python
  s = "hola"
  print(s.rjust(10)) # Salida: " hola"

### 27. rpartition(sep)

- _Función_: Similar a partition(), pero busca desde el final de la cadena.
- _Ejemplo_:
  python
  s = "hola mundo"
  print(s.rpartition(" ")) # Salida: ('hola ', ' ', 'mundo')
