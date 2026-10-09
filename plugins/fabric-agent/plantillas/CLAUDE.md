# <PROYECTO>

Proyecto de Microsoft Fabric para <ORGANIZACIÓN>.

## Perfil del agente

Este proyecto usa el plugin **fabric-agent**, que trae el perfil
`fabric-specialist` y lo adopta automáticamente al abrir la sesión mediante un
hook `SessionStart`. No hay que invocarlo como subagente: Claude ya responde con
ese perfil desde el primer mensaje.

Instalación en un proyecto nuevo, desde su carpeta y con alcance de proyecto
para que el perfil no se cargue en otros repositorios:

```
claude plugin marketplace add danielrodriguez007/Agente_Fabric --scope project
claude plugin install fabric-agent@fabric-agent-marketplace --scope project
```

Después, agregar a `.claude/settings.json` del proyecto las dos claves de
`plantillas/settings.json` del plugin (`"model": "sonnet"` y
`"advisorModel": "opus"`). Se agregan, no se copia el archivo encima: la
instalación anterior ya escribió ahí el plugin habilitado.

## Esquema de modelos: principal Sonnet, asesor Opus, subagente Haiku

- **Principal (Sonnet):** conversa con el usuario y hace el trabajo rutinario
  (código, consultas, operaciones y respuestas).
- **Asesor (Opus, tool advisor):** se consulta antes de decisiones de
  arquitectura o planificación, ante fallos ambiguos o que no convergen y en la
  verificación final.
- **Subagente explorador (Haiku, `fabric-agent:explorador`):** el principal
  puede delegarle sin pedir permiso las tareas de solo lectura. No se le delegan
  las decisiones de diseño, la escritura de archivos, los comandos que operan
  sistemas externos ni las respuestas al usuario. Lo que el explorador encuentra
  lo ubica; antes de citarlo o decidir con él, el principal lee el pasaje en el
  archivo.
- Para sesiones de arquitectura pesadas, el usuario puede usar `/model opus`
  solo en esa sesión.

El perfil `fabric-specialist` no se invoca como subagente: la conversación no se
reenvía a otro agente. El explorador es la excepción, porque no conversa, solo
lee.

## Documentos de este proyecto

- `contexto-cliente.md` — **todo lo que el agente sabe del cliente vive aquí.**
  Copiado de la plantilla del plugin. Se actualiza cuando se cierra una decisión.
- `PREFERENCIAS.md` — cómo se explica y se acompaña el trabajo. Copiado igual del
  plugin.
- `decisiones.md` — bitácora de lo que se fue decidiendo, con fecha y motivo.

## Estructura de carpetas

Tres tipos de contenido, cada uno en su carpeta, sin mezclarse:

- **`knowledge-base/`** — lo que aportó el cliente. Nunca generado por Claude.
  **No se versiona en un repositorio público ni se sube fuera del control del
  cliente**: es material de él, no del proyecto.
- **`project/`** — cómo se trabaja en este proyecto.
- **`artifacts/`** — lo que Claude construye: `reports/`, `notebooks/`,
  `scripts/`, `sql/`, `data/`.

## Convenciones

Las que el cliente ya prescribió y las que siguen abiertas están en
`contexto-cliente.md`, no aquí. Una convención propuesta sin decisión se
convierte en estándar por accidente: lo abierto se deja escrito como abierto.
