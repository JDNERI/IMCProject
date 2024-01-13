Explicaré a continuación el funcionamiento de mi código:

  1. `def input_number(answer)`:

     Esta es una función que toma un argumento llamado `answer`. Se utiliza para solicitar al usuario que introduzca un número.
     Dentro de un bucle infinito, el programa intenta convertir la entrada del usuario en un número flotante. Si la conversión es exitosa y el
     número no es cero, el número se devuelve y la función termina. Si la conversión falla (lo que lanza un `ValueError`) o si el número es cero,
     el programa imprime un mensaje de error y el bucle continúa, solicitando al usuario que introduzca un número de nuevo.
  
  3. El programa solicita al usuario que introduzca su nombre, apellido paterno y apellido materno. Para cada uno, el programa entra en un bucle
     que continúa hasta que el usuario proporciona una respuesta que no sea una cadena vacía o solo espacios.
  
  4. Luego, el programa utiliza la función `input_number(answer)` para solicitar al usuario que introduzca su edad, peso (en kg) y altura (en metros).
     Para cada uno, el programa entra en un bucle que continúa hasta que el usuario proporciona un número válido.
  
  5. El programa calcula el IMC utilizando la fórmula `peso / (altura * altura)`.
  
  6. Luego, el programa imprime el nombre completo del usuario, su edad y su IMC.
  
  7. Finalmente, el programa determina e imprime si el usuario está bajo de peso, en su peso normal, tiene sobrepeso, tiene obesidad leve, obesidad media
     u obesidad mórbida, basándose en el valor del IMC. Esto se hace con una serie de declaraciones `if` y `elif` que comprueban en qué rango cae el IMC.


Conclusion:

  "Fue un verdadero reto llevar a cabo este proyecto, ya que quise añadir el uso de bucles y una función. El primer desafío fue validar que el usuario,
  cada vez que no ingresara lo que se estaba solicitando, volviera a pedir nuevamente que ingresara los datos. Al final, logré conseguirlo; considero que
  fue lo más complicado a lo que me enfrenté en este proyecto. Después, no tuve tantos problemas con lo demás y pude realizar satisfactoriamente lo que se pidió.
  
  En cuanto al BootCamp, realmente se necesita compromiso para no procrastinar, ya que el esfuerzo, lo que estudiamos y demás, depende completamente de nosotros.
  Sin embargo, considero que es una buena forma de aprender y demostrar hasta dónde podemos llegar. Además, tenemos la confianza de que si nos atascamos en algo,
  siempre hay un profesor al que le podemos consultar nuestras dudas."
