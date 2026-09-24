---
name: fabric-cero-a-bronce
description: Procedimiento lineal y portable para adoptar Microsoft Fabric en una organización desde cero hasta tener la primera fuente aterrizada en la capa Bronze, con fases, compuertas de salida, checklists y plantillas. Úsala cuando el usuario quiera arrancar Fabric desde cero, planear la adopción inicial, preparar tenant/capacidad/workspaces, inventariar y conectar fuentes, o hacer la primera ingesta a Bronze en un proyecto nuevo. No cubre Silver ni Gold.
---

# Fabric: de cero a Bronze

Procedimiento para llevar una organización desde "no tenemos Fabric" hasta "la primera fuente aterriza en Bronze de forma desatendida, gobernada y repetible". Es independiente de cualquier cliente: todo lo que cambia entre proyectos vive en `plantillas/proyecto.config.md`.

## Cómo usar esta skill (instrucciones para el agente)

1. **Primero, la configuración del proyecto.** Busca `proyecto.config.md` en el repo del proyecto. Si no existe, copia `plantillas/proyecto.config.md` al repo (pregunta al usuario dónde) y llénalo con él. No inventes valores: lo que no se sepa queda como `POR DEFINIR` y se convierte en pregunta.
2. **Ubica la fase actual.** Pregunta en qué punto está el proyecto o dedúcelo de `proyecto.config.md` (sección "Estado por fase"). No asumas que se empieza en la Fase 0.
3. **Lee solo la referencia de la fase en curso** (`referencias/fase-N-*.md`) y guía al usuario paso a paso: dónde está cada opción en el portal, quién la ejecuta y qué pasa si se configura mal.
4. **Respeta las compuertas.** No avances a la fase siguiente hasta que se cumpla su *criterio de salida*. Si el usuario quiere saltarse una, dile explícitamente qué riesgo asume y regístralo en `proyecto.config.md`.
5. **Verifica antes de afirmar.** Fabric cambia cada mes. Antes de decir que algo es GA, está en preview o "no se puede", confírmalo en learn.microsoft.com/fabric y cita la URL. Cada referencia indica la fecha de su última verificación.
6. **El trabajo de otros se pide por escrito, no se ejecuta.** Tenant, red, credenciales y firewall suelen ser de TI o del dueño de la fuente. Ayuda a redactar el requerimiento (`plantillas/correo-requerimiento-fuente.md`) en vez de asumir que el usuario tiene los permisos.
7. Al cerrar cada fase, actualiza "Estado por fase" en `proyecto.config.md`.

## Mapa de fases

Las fases son secuenciales. Algunas pueden solaparse en el calendario (por ejemplo, la 5 y la 6 arrancan mientras avanza la 4), pero sus compuertas se cierran en orden.

| Fase | Nombre | Pregunta que responde | Criterio de salida (resumen) | Referencia |
|---|---|---|---|---|
| 0 | Arranque | ¿Para qué y con qué fuente empezamos? | Pregunta de negocio, sponsor y fuente piloto escritos y aprobados | `referencias/fase-0-arranque.md` |
| 1 | Tenant y roles | ¿Fabric está habilitado y quién lo administra? | Fabric activo para un grupo de Entra; administradores nombrados | `referencias/fase-1-tenant-roles.md` |
| 2 | Capacidad | ¿Dónde corre y cuánto cuesta? | Capacidad asignada (trial o F-SKU), región fijada, Capacity Metrics instalada | `referencias/fase-2-capacidad.md` |
| 3 | Gobierno base | ¿Quién ve qué y cómo se llama cada cosa? | Convención de nombres, roles por grupo y etiquetas de sensibilidad definidos | `referencias/fase-3-gobierno.md` |
| 4 | Workspaces y entornos | ¿Dónde vive el código y el dato? | Workspace(s) por entorno, Lakehouse de Bronze y control de versiones decidido | `referencias/fase-4-workspaces.md` |
| 5 | Inventario de fuentes | ¿Qué fuentes hay y cuál sigue? | Inventario priorizado; cinco preguntas enviadas y respondidas para la fuente piloto | `referencias/fase-5-inventario.md` |
| 6 | Conectividad | ¿Cómo llega Fabric a la fuente? | Connection creada y probada con credencial de servicio de solo lectura | `referencias/fase-6-conectividad.md` |
| 7 | Ingesta a Bronze | ¿Cómo aterriza el dato crudo? | Primera carga en Bronze con metadata de trazabilidad, relectura verificada | `referencias/fase-7-ingesta-bronze.md` |
| 8 | Orquestación y operación | ¿Corre solo y sabemos si falla? | Pipeline programado, alertas, consumo revisado, definición de "Bronze terminado" cumplida | `referencias/fase-8-operacion.md` |

## Documentos transversales

- `referencias/cinco-preguntas-por-fuente.md`: protocolo estándar para abordar cualquier fuente nueva (fases 5 y 6).
- `referencias/matriz-conexiones.md`: ubicación de la fuente → forma de conexión → autenticación (fase 6).
- `referencias/lecciones-aprendidas.md`: errores reales que ya costaron tiempo. Léela antes de escribir el primer notebook.
- `plantillas/checklist-fases.md`: todas las compuertas en una sola lista, para seguimiento.

## Plantillas

- `plantillas/proyecto.config.md`: lo único que cambia entre proyectos.
- `plantillas/correo-requerimiento-fuente.md`: requerimiento escrito para TI o el dueño de la fuente.
- `plantillas/nb_fuente_bootstrap.py`: autorización OAuth2 interactiva, una sola vez.
- `plantillas/nb_fuente_bronze.py`: ingesta desatendida a Bronze.

## Principios que aplican a todas las fases

- **Bronze es inmutable y crudo.** Cada extracción es un snapshot nuevo, nunca sobrescribe. No se transforma el contenido; solo se envuelve con metadata de trazabilidad.
- **Medallion y entornos son ejes distintos.** Dev, Test y Prod tienen cada uno su propio Bronze. Entre entornos se promueve el código, nunca los datos.
- **OneLake es la única copia.** Si el dato ya está en otro almacenamiento compatible, primero se evalúa un shortcut antes que copiarlo.
- **El piloto es la semilla de producción.** El primer notebook o pipeline se escribe para evolucionar, con la config separada de la lógica y sin credenciales persistentes en el código, no para tirarlo.
- **Gobierno desde el primer dato real**, no después.
- **La ubicación de la fuente decide la conexión**, no la preferencia de nadie.
