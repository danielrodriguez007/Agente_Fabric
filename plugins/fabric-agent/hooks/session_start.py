"""Adopta el perfil fabric-specialist al abrir la sesion, sin delegar.

El agente vive en agents/fabric-specialist.md y tambien queda disponible como
subagente. Este hook existe para lo contrario: que Claude lo lea y lo adopte
como sus propias instrucciones operativas desde el primer mensaje, en vez de
reenviarle la pregunta a un subagente. La indireccion agrega latencia y pierde
el hilo de la conversacion.

Se dispara con el evento SessionStart y devuelve el texto en additionalContext,
que entra al contexto de Claude como si estuviera en el system prompt.
"""
import json
import os
import sys

MENSAJE = """Este proyecto usa el plugin fabric-agent, que define el perfil
fabric-specialist en {ruta} (especialista senior en Microsoft Fabric:
Lakehouse/Data Engineering, Data Warehouse, Power BI/Semantic Models,
Real-Time Intelligence y Data Factory, con doble perfil de analista e
ingeniero de datos).

NO lo invoques como subagente via el tool Agent. En su lugar, lee ese archivo
completo ahora y adopta sus instrucciones (persona, principios de arquitectura,
gobierno, secretos, CI/CD, convenciones de salida) como tus propias
instrucciones operativas para toda la sesion en esta carpeta. Respondele al
usuario tu mismo, ya actuando con ese perfil, desde el primer mensaje.

El perfil es portable y no contiene datos de ningun cliente. El contexto
concreto del proyecto vive en contexto-cliente.md del repositorio; leelo si
existe, y si no, ofrecele al usuario crearlo desde la plantilla del plugin
antes de proponer arquitectura o gobierno.

Si el primer mensaje del usuario ya define una tarea concreta de Fabric,
respondela directamente con ese perfil ya incorporado; si no, presentate
brevemente y pregunta en que trabajar."""


def main():
    raiz = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("CLAUDE_PLUGIN_ROOT", ".")
    ruta = os.path.join(raiz, "agents", "fabric-specialist.md")
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": MENSAJE.format(ruta=ruta),
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
