"""Aviso de turno largo (regla del usuario, 2026-09-17).

Si un turno lleva mas de 10 minutos, avisa al usuario y le pide a Claude que
explique por que tarda y proponga como seguir. Se vuelve a avisar cada 10 min.

  start  -> UserPromptSubmit: guarda la hora de inicio del turno.
  check  -> PostToolUse: compara contra el limite y avisa si corresponde.
"""
import json
import os
import sys
import tempfile
import time

LIMITE_SEG = 10 * 60


def ruta_estado(session_id):
    carpeta = os.path.join(tempfile.gettempdir(), "claude-turn-timer")
    os.makedirs(carpeta, exist_ok=True)
    return os.path.join(carpeta, f"{session_id or 'sin-sesion'}.json")


def main():
    modo = sys.argv[1] if len(sys.argv) > 1 else "check"
    try:
        entrada = json.load(sys.stdin)
    except Exception:
        entrada = {}
    ruta = ruta_estado(entrada.get("session_id"))
    ahora = time.time()

    if modo == "start":
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump({"inicio": ahora, "ultimo_aviso": ahora}, f)
        return

    try:
        with open(ruta, encoding="utf-8") as f:
            estado = json.load(f)
    except Exception:
        return

    if ahora - estado["ultimo_aviso"] < LIMITE_SEG:
        return

    minutos = int((ahora - estado["inicio"]) // 60)
    estado["ultimo_aviso"] = ahora
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(estado, f)

    print(json.dumps({
        "systemMessage": f"Aviso: este turno ya lleva {minutos} min en curso.",
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                f"REGLA DEL USUARIO: este turno ya lleva {minutos} minutos. "
                "Antes de seguir, escribe al usuario un mensaje breve (tuteo, nunca voseo) con: "
                "que llevas hecho, por que esta tardando, cuanto falta estimado, y opciones concretas "
                "(seguir, acotar el alcance, dividir la tarea o detenerse). Luego continua solo si "
                "la tarea sigue teniendo sentido."
            ),
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
