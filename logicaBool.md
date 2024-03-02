# Operadores Lógicos en Python: Una Introducción Amigable

Para entender mejor los operadores lógicos en Python, vamos a explicarlo de una manera sencilla y amigable, utilizando solo ejercicios prácticos que involucren la función print y el tema de los operadores lógicos.

## ¿Qué son los operadores lógicos?

Imagina que tienes una caja llena de juguetes, pero solo quieres jugar con los juguetes que te gustan. Los operadores lógicos en Python son como las reglas que te ayudan a decidir cuáles juguetes jugar. Estas reglas pueden decirte si quieres jugar con un juguete si cumple con múltiples condiciones, como tener un color específico y no estar roto.

## Ejercicios prácticos:

1. *Usar el operador and:*
   python
   juguete_favorito = True
   juguete_nuevo = True
   print(juguete_favorito and juguete_nuevo)
   
   Aquí, decimos que queremos jugar con un juguete si es nuestro favorito y también es nuevo. Si ambas condiciones son verdaderas, entonces el resultado es True.

2. *Usar el operador or:*
   python
   juguete_favorito = True
   juguete_roto = False
   print(juguete_favorito or juguete_roto)
   
   Ahora, decimos que queremos jugar con un juguete si es nuestro favorito o si no está roto. Si al menos una de estas condiciones es verdadera, entonces el resultado es True.

3. *Usar el operador not:*
   python
   juguete_favorito = True
   print(not juguete_favorito)
   
   Este es un poco diferente. Decimos que queremos jugar con un juguete si NO es nuestro favorito. Si nuestro juguete favorito es verdadero, entonces el resultado de not será False.

4. *Combinar operadores lógicos:*
   python
   juguete_favorito = True
   juguete_nuevo = False
   juguete_roto = True
   print(juguete_favorito and not juguete_nuevo or not juguete_roto)
   
   Aquí, decimos que queremos jugar con un juguete si es nuestro favorito y NO es nuevo, O si NO está roto. Si alguna de estas condiciones es verdadera, entonces el resultado es True.

## Ejercicios en Clases💪🏾

Ejercicio 1: 

Crear reglas para jugar con juguetes
Enunciado: Escribe un programa que cree tres juguetes diferentes y use operadores lógicos para crear reglas que decidan cuándo puedes jugar con cada juguete. Luego, usa la función print para decir si puedes jugar con cada juguete según las reglas.

Ejercicio 2: 

Cambiar las reglas para jugar con juguetes
Enunciado: Escribe un programa que cambie las reglas para jugar con uno de los juguetes que creaste y luego usa la función print para decir si puedes jugar con ese juguete según las nuevas reglas.

`Ejercicio 3: `

Aplicar múltiples reglas para jugar con juguetes
Enunciado: Escribe un programa que aplique varias reglas para jugar con un juguete, utilizando los operadores lógicos and, or, y not. Luego, usa la función print para decir si puedes jugar con ese juguete según todas las reglas.

Ejercicio 5: 

    Cambiar las reglas y probar nuevas combinaciones
Enunciado: Escribe un programa que cambie las reglas para jugar con los juguetes y luego pruebe diferentes combinaciones de reglas para ver si puedes jugar con los juguetes según estas nuevas reglas. Usa la función print para decir si puedes jugar con cada juguete según las combinaciones de reglas.
