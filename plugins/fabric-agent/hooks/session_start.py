"""Adopta el perfil fabric-specialist al abrir la sesion, sin reenviar la
conversacion a otro agente, y recuerda el esquema de modelos.

El agente vive en agents/fabric-specialist.md y tambien queda disponible como
subagente. Este hook existe para lo contrario: que Claude lo lea y lo adopte
como sus propias instrucciones operativas desde el primer mensaje, en vez de
reenviarle la pregunta a un subagente. La indireccion agrega latencia y pierde
el hilo de la conversacion.

Se dispara con el evento SessionStart y devuelve el texto en additionalContext,
que entra al contexto de Claude como si estuviera en el system prompt.

El esquema de modelos (principal Sonnet, asesor Opus, explorador Haiku) solo se
recuerda aqui: el modelo principal y el del asesor se fijan en el
.claude/settings.json de cada proyecto (ver plantillas/settings.json), porque el
settings.json de un plugin solo admite las claves agent y subagentStatusLine.
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
({plantilla}) antes de proponer arquitectura o gobierno.

Esquema de modelos. El principal (tu, Sonnet si el proyecto lo fijo en su
.claude/settings.json) conversa con el usuario y hace el trabajo rutinario:
codigo, consultas, operaciones y respuestas. Consulta al asesor (Opus, tool
advisor) antes de decisiones de arquitectura o planificacion, ante fallos
ambiguos o que no convergen y en la verificacion final antes de dar algo por
terminado. Delega por iniciativa propia, sin pedir permiso, al subagente
fabric-agent:explorador (Haiku) las tareas de solo lectura: buscar, leer y
resumir archivos. Esto no contradice lo anterior: lo que no se hace es reenviar
la conversacion a fabric-specialist como subagente. No le delegues
decisiones de diseno, escritura de archivos, comandos que operan sistemas
externos ni respuestas al usuario, y antes de citar o decidir con un pasaje que
el explorador encontro, leelo tu mismo en el archivo.

Si el primer mensaje del usuario ya define una tarea concreta de Fabric,
respondela directamente con ese perfil ya incorporado; si no, presentate
brevemente y pregunta en que trabajar."""


def main():
    raiz = os.environ.get("CLAUDE_PLUGIN_ROOT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raiz = raiz.replace("\\", "/")
    ruta = raiz + "/agents/fabric-specialist.md"
    plantilla = raiz + "/plantillas/contexto-cliente.md"
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": MENSAJE.format(ruta=ruta, plantilla=plantilla),
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
