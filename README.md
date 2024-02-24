# Bucle While

Para entender mejor el concepto del bucle `while`, vamos a definirlo de manera sencilla y luego a través de ejercicios prácticos.

**Definición del bucle `while`:**

El bucle `while` es una estructura de control en programación que permite ejecutar un bloque de código repetidamente mientras una condición específica se mantenga verdadera. En otras palabras, el bucle `while` sigue ejecutándose hasta que la `condición evaluada se vuelve falsa.`

**Ejercicios prácticos:**

1. **Imprimir números del  1 al  5:**
   ```python
   numero =  1
   while numero <=  5:
       print(numero)
       numero +=  1
   ```
   -----
   Vamos a desglosar paso a paso cómo funciona el código para `Imprimir números del  1 al  5`, que es un ejemplo de un bucle `while` en Python:

2. **Inicialización de la variable `numero`:**
   Al inicio, se establece la variable `numero` con el valor  1.

    ```python
    numero =  1
    ```

3. **Evaluación de la condición del bucle `while`:**
   La condición del bucle `while` es `numero <=  5`. Esto significa que el bucle continuará ejecutándose mientras el valor de `numero` sea menor o igual a  5.

    ```python
    numero <=  5
    ```

4. **Ejecución del bloque de código dentro del bucle:**
   - Si la condición es verdadera (en este caso, inicialmente es verdadera porque `numero` es  1), se ejecutan las instrucciones dentro del bloque del bucle.
   - Primero, se ejecuta `print(numero)`, que imprime el valor actual de `numero` en la consola.
   - Luego, se ejecuta `numero +=  1`, que incrementa el valor de `numero` en  1.

   ```python
     print(numero)
       numero +=  1
   ```


5. **Repetición del bucle:**
   - Después de ejecutar el bloque de código, el programa vuelve a evaluar la condición del bucle `while`.
   - Si la condición sigue siendo verdadera (por ejemplo, después de incrementar `numero` a  2,  3,  4, o  5), el bucle se repite desde el principio, ejecutando nuevamente las instrucciones dentro del bloque.

6. **Terminación del bucle:**
   - Una vez que la condición del bucle `while` se vuelve falsa (por ejemplo, cuando `numero` se incrementa a  6), el bucle se detiene y el programa continúa con cualquier instrucción que siga después del bucle
   -----
2. **Sumar números hasta que la suma sea mayor que  10:**
   ```python
   suma =  0
   numero =  1
   while suma <=  10:
       suma += numero
       numero +=  1
   print(suma)
   ```

3. **Validar la entrada de un usuario para asegurar que es un número entero positivo:**
   ```python
   entrada = ""
   while not entrada.isdigit():
       entrada = input("Ingrese un número entero positivo: ")
   print("Número válido:", entrada)
   ```

4. **Contar las vocales en una cadena de texto:**
   ```python
   texto = "Hola Mundo"
   vocales = "aeiou"
   contador =  0
   for letra in texto.lower():
       if letra in vocales:
           contador +=  1
   print("Cantidad de vocales:", contador)
   ```

5. **Simular un contador regresivo desde  10 hasta  1:**
   ```python
   contador =  10
   while contador >  0:
       print(contador)
       contador -=  1
   print("¡Feliz Año Nuevo!")
   ```

## Ejercicios en Clases💪🏾

`Ejercicio 1:` 

Sumar números hasta un límite
Enunciado: Escribe un programa que sume todos los números desde 1 hasta un número dado n. El programa debe pedir al usuario que introduzca un número n y luego sumar todos los números desde 1 hasta n.

`Ejercicio 2:` 

Contar palabras en una frase
Enunciado: Escribe un programa que cuente el número de palabras en una frase. El programa debe pedir al usuario que introduzca una frase y luego contar cuántas palabras hay en esa frase.

La función `.split()` en Python es una de las formas más comunes de dividir una cadena de texto (string) en una lista de subcadenas basadas en un delimitador específico. Esta función es muy útil para manipular y analizar textos, ya que permite separar palabras, frases, o cualquier tipo de datos en partes más pequeñas y manejables.

Funcionamiento Básico de .split()
Cuando se llama a .split() sin argumentos, la función divide la cadena en cada espacio en blanco (espacios, tabulaciones, saltos de línea) y devuelve una lista de las subcadenas resultantes. Por ejemplo:

```
texto = "Hola mundo"
lista = texto.split()
print(lista)  # Salida: ['Hola', 'mundo']

```

`Ejercicio 3: `

Tabla de multiplicar
Enunciado: Escribe un programa que muestre la tabla de multiplicar de un número dado n hasta 10. El programa debe pedir al usuario que introduzca un número n.

`Ejercicio 5:` 

    Verificar si un número es par
Enunciado: Escribe un programa que verifique si un número es par. El programa debe pedir al usuario que introduzca un número y luego decir si el número es par o impar.
