# Respuestas Teóricas - Checkpoint 4


1. **¿Cuál es la diferencia entre una lista y una tupla en Python?**

La diferencia principal es la mutabilidad. Por un lado las listas `[]` son mutables, es decir, que se puede cambiar, añadir o eliminar elementos después de haberlas creado.

Por otro lado, las tuplas `()` son inmutables, es decir, que una vez definidas no se puede cambiar su contenido, así que si se quiere cambiar algo se debe hacer una nueva.

Según la documentación de python "Memory Management" las tuplas ocupan menos espacio en la memoria RAM que las listas. Al ser inmutables, Python sabe exactamente cuánto espacio necesitan desde el principio. Las listas, al ser dinámicas, necesitan "espacio extra" por si decides añadir más elementos. Por lo que las tuplas son ideales para procesar grandes volúmenes de datos constantes (Big Data)

**Buena práctica:** Usar listas cuando se usa una colección de datos que necesite actualizarse (como un carrito de compras). Usar tuplas para datos que deben permanecer constantes y protegidos (como las coordenadas de una ciudad o los meses del año).

**Ejemplo:**
`mi_lista.append("nuevo")` --> correcto
`mi_tupla.append("nuevo")` --> error (las tuplas no tienen ese método).


---

2. **¿Cuál es el orden de las operaciones?**

En Python, el orden de las operaciones sigue la regla mnemotécnica PEMDAS. Es el orden de prioridad que el código usa para resolver cálculos matemáticos:

1. Paréntesis `()`
2. Exponentes `**`
3. Multiplicación `*` y División `/` (tienen la misma prioridad, se resuelven de izquierda a derecha).
4. Adición `+` y Sustracción `-` (igual prioridad, de izquierda a derecha).

**Ejemplo:** En `2 + 3 * 4`, Python primero hace `3 * 4 = 12` y luego suma `2`, dando `14`. Si queremos que sume primero, usamos paréntesis: `(2 + 3) * 4 = 20`.

El orden de las operaciones es una parte de la 'Precedencia de Operadores'. Es vital usar paréntesis no solo para cambiar el resultado, sino por legibilidad, facilitando que otros programadores entiendan la intención del código sin tener que memorizar toda la tabla de prioridades.

---

3. **¿Qué es un diccionario Python?**

Un diccionario es un conjunto de datos que almacena información en pares de Llave-Valor (Key-Value). A diferencia de las listas, donde buscas por posición (índice), en un diccionario buscas por una "etiqueta" única (la llave).

**Analogía:** Es como una agenda de contactos. La "llave" es el nombre de la persona y el "valor" es su número de teléfono. No buscas a alguien por ser "el contacto número 5", lo buscas por su nombre.

**Ejemplo:** `usuario = {"nombre": "Manuela", "edad": 22}`. Accedes con `usuario["nombre"]`.

Técnicamente, un diccionario es una implementación de una 'Hash Table'. Esto garantiza que el tiempo de búsqueda sea extremadamente rápido, sin importar si el diccionario tiene 10 o 10 millones de registros, buscar un elemento en un diccionario es casi instantáneo tiempo constante, mientras que en una lista, si el elemento está al final, Python tiene que recorrerlo todo, tiempo lineal.

---

4. **¿Cuál es la diferencia entre el método ordenado y la función de ordenación?**

Ambos sirven para ordenar, pero la diferencia está en cómo afectan a los datos originales:

* `.sort()` (Método): Ordena la lista in-place (en el sitio). Esto significa que modifica la lista original de forma permanente y no devuelve nada (retorna None). Solo funciona en listas.
* `sorted()` (Función): Crea una nueva copia ordenada de la colección y deja la original intacta. Es más flexible porque puede ordenar listas, tuplas o diccionarios.

**Buena práctica:** Usar `sorted()` si se necesita conservar los datos originales para otros procesos. Usar `.sort()` si no importa cambiar el original y se quiere ahorrar un poco de memoria.

En el desarrollo moderno se prefiere a menudo sorted() para seguir principios de programación funcional, evitando 'efectos secundarios' inesperados que podrían ocurrir si otra parte del programa intenta usar la lista original mientras esta es modificada por .sort().

---

5. **¿Qué es un operador de reasignación?**

Un operador de reasignación es una forma abreviada de actualizar el valor de una variable basándose en su valor anterior. En lugar de escribir el nombre de la variable dos veces, combinamos el operador aritmético con el signo igual `=`.

**Ejemplos:**
* `puntos += 10` es lo mismo que `puntos = puntos + 10`.
* `total *= 2` es lo mismo que `total = total * 2`.

**Caso especial en Tuplas:** Como las tuplas son inmutables, cuando hacemos `mi_tupla += (4,)`, no estamos "añadiendo" al objeto original, sino que estamos reasignando la variable a una tupla completamente nueva que combina la anterior con el nuevo dato.

Dato extra: Estos operadores se llaman técnicamente Operadores de Asignación Aumentada. Los cuales no son solo 'atajos' para escribir menos; también pueden ayudar en la optimización interna de Python, ya que en algunos casos permiten al intérprete realizar la operación de manera más eficiente directamente sobre el valor almacenado.