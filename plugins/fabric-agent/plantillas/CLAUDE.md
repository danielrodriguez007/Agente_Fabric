# <PROYECTO>

Proyecto de Microsoft Fabric para <ORGANIZACIÓN>.

## Perfil del agente

Este proyecto usa el plugin **fabric-agent**, que trae el perfil
`fabric-specialist` y lo adopta automáticamente al abrir la sesión mediante un
hook `SessionStart`. No hay que invocarlo como subagente: Claude ya responde con
ese perfil desde el primer mensaje.

Instalación en un proyecto nuevo:

```
/plugin marketplace add <org>/fabric-agent
/plugin install fabric-agent@fabric-agent-marketplace
```

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
