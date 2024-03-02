# Función print en Python

Para entender mejor el concepto de la función print en Python, vamos a definirla de manera sencilla y luego a través de ejercicios prácticos.

## Definición de la función print:

La función print en Python es una función incorporada que permite imprimir datos en la salida estándar, que normalmente es la terminal o la consola. La función print es muy versátil, ya que puede aceptar múltiples argumentos y permite personalizar la salida de diferentes maneras, como agregar espacios, especificar el final de línea, y más.

## Ejercicios prácticos:

1. *Imprimir un mensaje simple:*
   python
   print("¡Hola, mundo!")
   
   Este es el ejemplo más básico de cómo usar la función print para imprimir un mensaje simple.

2. *Imprimir múltiples argumentos:*
   python
   print("Hola", "mundo", sep=", ")
   
   Aquí, print se utiliza para imprimir dos cadenas de texto, "Hola" y "mundo", separadas por una coma y un espacio.

3. *Imprimir con un salto de línea al final:*
   python
   print("Hola, mundo!", end="\n")
   
   Por defecto, print agrega un salto de línea al final de la salida. Sin embargo, puedes personalizar el final de la salida utilizando el argumento end.

4. *Imprimir sin espacio entre argumentos:*
   python
   print("Hola", "mundo", sep="")
   
   En este caso, se especifica que no se debe agregar ningún espacio entre los argumentos, por lo que la salida será "Hola mundo".

5. *Imprimir una variable:*
   python
   nombre = "Juan"
   print("Hola,", nombre)
   
   La función print puede imprimir el valor de una variable, como se muestra aquí, donde se imprime "Hola, Juan".

6. *Imprimir el resultado de una operación:*
   python
   suma = 3 + 5
   print("La suma es", suma)
   
   Aquí, print imprime el resultado de una operación matemática, mostrando "La suma es 8".

7. *Imprimir con formato:*
   python
   print(f"La suma es {3 + 5}")
   
   La función print puede utilizar f-strings para insertar el resultado de una expresión dentro de una cadena de texto, como se muestra aquí.

8. *Imprimir una lista:*
   python
   lista = [1, 2, 3, 4, 5]
   print(lista)
   
   Para imprimir una lista, simplemente puedes pasar la lista como argumento a print, y se imprimirá la representación de la lista.

## Ejercicios en Clases💪🏾

Ejercicio 1: 

Imprimir los elementos de una lista
Enunciado: Escribe un programa que imprima los elementos de una lista de números. El programa debe crear una lista de números y luego imprimir cada número de la lista.

Ejercicio 2: 

Formatear la salida de una lista de números
Enunciado: Escribe un programa que imprima los elementos de una lista de números, pero esta vez, utiliza la función print con f-strings para formatear la salida de manera que cada número esté en una línea nueva y precedido por "El número es: ".

`Ejercicio 3: `

Imprimir el resultado de una operación matemática
Enunciado: Escribe un programa que realice una operación matemática y luego imprima el resultado utilizando la función print.

Ejercicio 5: 

    Imprimir un mensaje personalizado
Enunciado: Escribe un programa que pida al usuario su nombre y luego imprima un mensaje personalizado que incluya el nombre del usuario.
