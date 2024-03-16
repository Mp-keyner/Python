Para crear un archivo similar al proporcionado pero enfocado en condicionales en Python, puedes seguir la estructura y el enfoque del archivo original, adaptándolo al tema de los condicionales. Aquí tienes un esquema que puedes seguir:

---

# Operadores Condicionales en Python: Una Introducción Amigable

Para entender mejor los operadores condicionales en Python, vamos a explicarlo de una manera sencilla y amigable, utilizando solo ejercicios prácticos que involucren la función `print` y el tema de los operadores condicionales.

## ¿Qué son los operadores condicionales?

Imagina que tienes una caja llena de libros, pero solo quieres leer los libros que te gustan. Los operadores condicionales en Python son como las reglas que te ayudan a decidir cuáles libros leer. Estas reglas pueden decirte si quieres leer un libro si cumple con múltiples condiciones, como tener un género específico y no estar ya leído.

## Ejercicios prácticos:

1. *Usar el operador `if`:*
   ```python
   libro_favorito = True
   if libro_favorito:
       print("Voy a leer este libro.")
   ```
   Aquí, decimos que queremos leer un libro si es nuestro favorito. Si esta condición es verdadera, entonces el resultado es que vamos a leer este libro.

2. *Usar el operador `elif`:*
   ```python
   libro_favorito = False
   libro_nuevo = True
   if libro_favorito:
       print("Voy a leer este libro.")
   elif libro_nuevo:
       print("Voy a leer este libro nuevo.")
   ```
   Ahora, decimos que queremos leer un libro si es nuestro favorito, o si es nuevo. Si al menos una de estas condiciones es verdadera, entonces el resultado es que vamos a leer este libro o este libro nuevo.

3. *Usar el operador `else`:*
   ```python
   libro_favorito = False
   libro_nuevo = False
   if libro_favorito:
       print("Voy a leer este libro.")
   elif libro_nuevo:
       print("Voy a leer este libro nuevo.")
   else:
       print("No voy a leer ningún libro.")
   ```
   Este es un poco diferente. Decimos que queremos leer un libro si es nuestro favorito o si es nuevo, y si ninguna de estas condiciones es verdadera, entonces el resultado es que no vamos a leer ningún libro.

4. *Combinar operadores condicionales:*
   ```python
   libro_favorito = True
   libro_nuevo = False
   libro_leido = True
   if libro_favorito and not libro_leido:
       print("Voy a leer este libro.")
   elif not libro_nuevo:
       print("Voy a leer este libro no nuevo.")
   else:
       print("No voy a leer ningún libro.")
   ```
   Aquí, decimos que queremos leer un libro si es nuestro favorito y no lo hemos leído, o si no es nuevo. Si alguna de estas condiciones es verdadera, entonces el resultado es que vamos a leer este libro o este libro no nuevo.

## Ejercicios en Clases💪🏾

Ejercicio 1: 

Crear reglas para leer libros
Enunciado: Escribe un programa que cree tres libros diferentes y use operadores condicionales para crear reglas que decidan cuándo puedes leer cada libro. Luego, usa la función `print` para decir si puedes leer cada libro según las reglas.

Ejercicio 2: 

Cambiar las reglas para leer libros
Enunciado: Escribe un programa que cambie las reglas para leer uno de los libros que creaste y luego usa la función `print` para decir si puedes leer ese libro según las nuevas reglas.

Ejercicio 3: 

Aplicar múltiples reglas para leer libros
Enunciado: Escribe un programa que aplique varias reglas para leer un libro, utilizando los operadores condicionales `if`, `elif`, y `else`. Luego, usa la función `print` para decir si puedes leer ese libro según todas las reglas.

Ejercicio 4: 

Cambiar las reglas y probar nuevas combinaciones
Enunciado: Escribe un programa que cambie las reglas para leer los libros y luego pruebe diferentes combinaciones de reglas para ver si puedes leer los libros según estas nuevas reglas. Usa la función `print` para decir si puedes leer cada libro según las combinaciones de reglas.
