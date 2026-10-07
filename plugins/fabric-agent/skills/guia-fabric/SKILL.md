---
name: guia-fabric
description: Procedimiento lineal y portable para adoptar Microsoft Fabric en una organización desde cero hasta tener la primera fuente aterrizada en la capa Bronze, en 9 fases con criterio de salida. Úsala cuando el usuario diga "guía fabric", quiera arrancar Fabric desde cero, planear la adopción inicial, preparar tenant, capacidad o workspaces, inventariar y conectar fuentes, o hacer la primera ingesta a Bronze en un proyecto nuevo. No cubre Silver ni Gold.
---

# Fabric: de cero a Bronze

Procedimiento para llevar una organización desde "no tenemos Fabric" hasta "la primera fuente aterriza en Bronze de forma desatendida, gobernada y repetible". Es independiente de cualquier cliente: todo lo que cambia entre proyectos vive en `proyecto.config.md`.

## Cómo usar esta skill (instrucciones para el agente)

1. **Primero, la configuración del proyecto.** Busca `proyecto.config.md` en el repo del proyecto. Si no existe, copia `${CLAUDE_PLUGIN_ROOT}/skills/guia-fabric/plantillas/proyecto.config.md` al repo (pregunta al usuario dónde) y llénalo con él. No inventes valores: lo que no se sepa queda como `POR DEFINIR` y se convierte en pregunta.
2. **Ubica la fase actual.** Pregunta en qué punto está el proyecto o dedúcelo de `proyecto.config.md` (sección "Estado por fase"). No asumas que se empieza en la Fase 0.
3. **Guía la fase en curso paso a paso** con el mapa de abajo: dónde está cada opción en el portal, quién la ejecuta y qué pasa si se configura mal. Esta versión no trae una referencia escrita por fase, así que cada paso de portal o de configuración se confirma en Microsoft Learn antes de darlo (punto 5).
4. **Respeta las compuertas.** No avances a la fase siguiente hasta que se cumpla su *criterio de salida*. Si el usuario quiere saltarse una, dile explícitamente qué riesgo asume y regístralo en `proyecto.config.md`.
5. **Verifica antes de afirmar.** Fabric cambia cada mes. Antes de decir que algo es GA, está en preview o "no se puede", confírmalo en learn.microsoft.com/fabric y cita la URL.
6. **El trabajo de otros se pide por escrito, no se ejecuta.** Tenant, red, credenciales y firewall suelen ser de TI o del dueño de la fuente. Ayuda a redactar el requerimiento en vez de asumir que el usuario tiene los permisos.
7. Al cerrar cada fase, actualiza "Estado por fase" en `proyecto.config.md`.

## Mapa de fases

Las fases son secuenciales. Algunas pueden solaparse en el calendario (por ejemplo, la 5 y la 6 arrancan mientras avanza la 4), pero sus compuertas se cierran en orden.

| Fase | Nombre | Pregunta que responde | Criterio de salida |
|---|---|---|---|
| 0 | Arranque | ¿Para qué y con qué fuente empezamos? | Pregunta de negocio, sponsor y fuente piloto escritos y aprobados |
| 1 | Tenant y roles | ¿Fabric está habilitado y quién lo administra? | Fabric activo para un grupo de Entra; administradores nombrados |
| 2 | Capacidad | ¿Dónde corre y cuánto cuesta? | Capacidad asignada (trial o F-SKU), región fijada y forma de medir el consumo definida |
| 3 | Gobierno base | ¿Quién ve qué y cómo se llama cada cosa? | Convención de nombres, roles por grupo y etiquetas de sensibilidad definidos |
| 4 | Workspaces y entornos | ¿Dónde vive el código y el dato? | Workspace(s) por entorno, Lakehouse de Bronze y control de versiones decidido |
| 5 | Inventario de fuentes | ¿Qué fuentes hay y cuál sigue? | Inventario priorizado; cinco preguntas enviadas y respondidas para la fuente piloto |
| 6 | Conectividad | ¿Cómo llega Fabric a la fuente? | Connection creada y probada con credencial de servicio de solo lectura |
| 7 | Ingesta a Bronze | ¿Cómo aterriza el dato crudo? | Primera carga en Bronze con metadata de trazabilidad, relectura verificada |
| 8 | Orquestación y operación | ¿Corre solo y sabemos si falla? | Pipeline programado, alertas, consumo revisado, definición de "Bronze terminado" cumplida |

## Las cinco preguntas por fuente (fases 5 y 6)

Protocolo para cualquier fuente nueva. Se mandan juntas, no por tandas:

1. ¿Dónde está desplegada?
2. ¿Qué tipo de conexión aplica?
3. ¿Con qué credenciales se accede?
4. ¿Quién habilita el acceso?
5. ¿Quién lo autoriza?

La primera decide las otras dos técnicas: la ubicación de la fuente determina la forma de conexión, no la preferencia de nadie.

## Principios que aplican a todas las fases

- **Bronze es crudo y trazable.** No se transforma el contenido; solo se agregan columnas de trazabilidad. Cómo se guarda depende de la ruta: por API, cada extracción es un snapshot nuevo que no se sobrescribe; por gateway con Copy, la tabla queda en su último estado (Overwrite) y la historia, si hace falta, se construye con marca de agua e incremental. El detalle está en el perfil `fabric-specialist`, sección Bronze.
- **Medallion y entornos son ejes distintos.** Dev, Test y Prod tienen cada uno su propio Bronze. Entre entornos se promueve el código, nunca los datos.
- **OneLake es la única copia.** Si el dato ya está en otro almacenamiento compatible, primero se evalúa un shortcut antes que copiarlo.
- **El piloto es la semilla de producción.** El primer notebook o pipeline se escribe para evolucionar, con la config separada de la lógica y sin credenciales persistentes en el código, no para tirarlo.
- **Gobierno desde el primer dato real**, no después.
