"""Cierre de sesion al despedirse.

UserPromptSubmit: si el mensaje es una despedida corta (adios, chao, bye...),
inyecta las tareas de cierre: guardar lo valioso de la sesion y, si el proyecto
lleva registro de insumos de entregables, anotar ahi lo hecho.

En Windows la entrada estandar llega en UTF-8 pero Python la lee con la pagina
de codigos local: se decodifica a mano o "adios" con tilde no coincide.
"""
import json
import os
import re
import sys
import unicodedata

MAX_LARGO = 80
INSUMOS = os.path.join("project", "INSUMOS-ENTREGABLES.md")

DESPEDIDAS = re.compile(
    r"\b(adios|chao|chau|bye|goodbye|good bye|hasta luego|hasta manana|"
    r"hasta pronto|nos vemos|see you|me voy|cerramos|terminamos por hoy)\b"
)

GUARDAR = (
    "El usuario se esta despidiendo. Antes de responder, haz el cierre de sesion:\n"
    "1. Revisa toda la conversacion de esta sesion y guarda lo que enriquece el "
    "proyecto: decisiones, hallazgos, preferencias y estado nuevo. Va a la memoria "
    "(un archivo por hecho + su linea en MEMORY.md, actualizando antes que "
    "duplicando), a project/PREFERENCIAS.md si es una preferencia, y a CLAUDE.md "
    "solo si es una decision efectivamente tomada. No guardes lo que ya esta en "
    "los archivos ni lo que solo importa a esta conversacion.\n"
)
ANOTAR = (
    "2. Asigna lo hecho en la sesion a los entregables y anotalo en "
    "project/INSUMOS-ENTREGABLES.md, bajo el entregable que corresponda: fecha, "
    "que paso y donde esta la evidencia. Solo lo hecho, medido o decidido; si algo "
    "corrige una entrada anterior, corrigela.\n"
)
CERRAR = "Responde en pocas lineas: que guardaste y donde."


def normalizar(texto):
    sin_tildes = unicodedata.normalize("NFKD", texto)
    sin_tildes = "".join(c for c in sin_tildes if not unicodedata.combining(c))
    return sin_tildes.lower().strip()


def main():
    try:
        entrada = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace"))
    except ValueError:
        return
    prompt = normalizar(entrada.get("prompt", ""))
    if not prompt or len(prompt) > MAX_LARGO or not DESPEDIDAS.search(prompt):
        return
    proyecto = os.environ.get("CLAUDE_PROJECT_DIR") or entrada.get("cwd") or "."
    texto = GUARDAR
    if os.path.isfile(os.path.join(proyecto, INSUMOS)):
        texto += ANOTAR
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": texto + CERRAR,
        }
    }))


if __name__ == "__main__":
    main()
