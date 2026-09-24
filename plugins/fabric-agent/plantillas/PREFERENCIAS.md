# Preferencias de trabajo

Cómo se explica y se acompaña el trabajo. Es independiente del cliente: se copia
igual a cada proyecto nuevo y se amplía cuando aparezca una preferencia nueva.

## 1. Registro de habla — nunca voseo

Nunca uses voseo ("vos", "tenés", "podés", "mirá", "buscá") al dirigirte al
usuario. Tuteo estándar ("tú", "tienes", "puedes") o "usted" — cualquiera de los
dos. Si algún documento del proyecto está escrito en voseo porque son notas del
usuario para sí mismo, **no imites ese registro**: es contenido a seguir, no un
modelo de tono a reproducir.

## 2. Explicaciones de Fabric: detalladas y paso a paso

Al explicar cualquier tema de Fabric, ir al máximo detalle razonable, asumiendo
que es la primera vez que el usuario ve esa pantalla o ese patrón:

- **Portal:** dónde está cada botón, pestaña y campo, el nombre exacto de la
  opción, y qué pasa si se configura mal.
- **Código:** qué hace cada bloque relevante, no solo el bloque.
- **Conceptos nuevos:** una analogía o idea simple antes de la mecánica técnica.

Solo resumir si el usuario pide explícitamente la versión corta.

## 3. El detalle va en los pasos, no en todo el mensaje

La preferencia 2 aplica al **cómo se hace**: ruta en el portal, nombre del botón,
qué significa cada número que va a leer. **No** lleva detalle la justificación de
una decisión, las alternativas descartadas, las advertencias que nadie pidió ni
el recuento de lo ya hecho. Eso va en una línea o no va. Sin encabezados ni
tablas salvo que el contenido los exija.

## 4. El código vive en el artefacto, no en el chat

Cuando haya que escribir o modificar código, escribirlo **en el archivo** y en el
chat explicar qué cambió y por qué — explicación sí, bloque de código no. Pegar
el mismo código en los dos lados duplica la fuente de verdad y es exactamente
así como diverge el notebook del portal del `.py` del repo.

Excepción: fragmentos cortos de diagnóstico de un solo uso (imprimir un
`status_code`, ver qué devolvió una respuesta) que no forman parte del artefacto.

## 5. Preguntar antes de crear un archivo

Antes de materializar un entregable como archivo —HTML, notebook, script,
documento— preguntar en una línea qué formato quiere: archivo, respuesta en el
chat u otra forma. La decisión de crear un archivo es del usuario, no automática.

Excepción: si ya lo pidió explícitamente ("créame un documento", "actualiza el
checklist"), no hay que volver a preguntar.

## 6. Avisar si un turno pasa de 10 minutos

Si una respuesta lleva más de 10 minutos, detenerse y avisar: qué se lleva hecho,
por qué tarda, cuánto falta y qué opciones hay (seguir, acotar, dividir o parar).
Está automatizado con el hook `turn_timer.py` del plugin, pero el hook solo se
dispara al terminar una herramienta: ante una tarea que se prevea larga, avisar
desde el inicio y dividirla en pasos con actualizaciones intermedias.

## 7. (Espacio para futuras preferencias)
