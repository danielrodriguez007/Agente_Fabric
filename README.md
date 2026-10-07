# Fabric Agent

Plugin de Claude Code que empaqueta un especialista en Microsoft Fabric y el
procedimiento para adoptarlo en un proyecto nuevo. Un mismo repositorio sirve de
catálogo (*marketplace*) y de plugin.

## La regla que no se negocia

**De los proyectos sale el aprendizaje, nunca el contenido.** La regla general
entra; el caso concreto se queda afuera. Aquí no aparece ningún nombre de
cliente, de sus fuentes, personas, áreas, olas ni workspaces. Lo que cambia entre
proyectos se parametriza en `plantillas/contexto-cliente.md`.

## Instalación

Se instala **por proyecto**, no a nivel de usuario. Sus hooks se disparan en
cada sesión donde el plugin está activo: instalado a nivel de usuario, el perfil
de Fabric se cargaría también en proyectos que no tienen nada que ver.

Desde la carpeta del proyecto:

```
claude plugin marketplace add danielrodriguez007/Agente_Fabric --scope project
claude plugin install fabric-agent@fabric-agent-marketplace --scope project
```

`project` deja la instalación en `.claude/settings.json`, compartida con quien
clone el repositorio. Para que quede solo en tu máquina, usa `--scope local`.

Para probarlo sin instalar:

```
claude --plugin-dir /ruta/a/fabric-agent/plugins/fabric-agent
```

**Requisitos.** Python 3 disponible como `python3`, `python` o `py`. Claude
Code ejecuta los hooks con `sh` en macOS y Linux, y con Git Bash en Windows.

**Validación.** Antes de publicar un cambio:

```
claude plugin validate . --strict
claude plugin validate plugins/fabric-agent --strict
```

## Qué trae

| Componente | Qué hace |
|---|---|
| `agents/fabric-specialist.md` | El perfil: doble lente analista/ingeniero, principios de arquitectura, conceptos que se confunden, gobierno, secretos, CI/CD, costo y convenciones de salida |
| `skills/guia-fabric/` | Procedimiento de adopción en 9 fases, de cero a la primera fuente en Bronze, cada fase con su criterio de salida. Se activa diciendo "guía fabric" |
| `skills/estilo-notion/` | Sistema visual monocromático para los documentos HTML del proyecto, con CSS y JS listos |
| `hooks/` | `SessionStart` adopta el perfil sin delegar; `turn_timer` avisa si un turno pasa de 10 minutos; `py.sh` elige el intérprete de Python disponible |
| `docs/MCP-SETUP.md` | Cómo activar los MCP de Fabric y la Fabric CLI, separando lo comprobado en uso de lo que solo describe la documentación |
| `plantillas/` | `contexto-cliente.md`, `PREFERENCIAS.md` y un `CLAUDE.md` de arranque |

## Por qué el hook en vez de un subagente

El perfil queda disponible como subagente, pero el hook `SessionStart` hace lo
contrario: le pide a Claude que **lea el archivo y lo adopte** como sus propias
instrucciones desde el primer mensaje. Tratarlo como subagente agrega un
intermediario —hay que invocarlo, pierde el hilo de la conversación y devuelve un
informe en vez de conversar—. El perfil se incorpora, no se consulta.

## Cómo arrancar un proyecto nuevo

1. Instalar el plugin.
2. Copiar `plantillas/contexto-cliente.md` al repositorio del proyecto y llenarlo
   con el usuario. Lo que no se sepa queda como `POR DEFINIR`: es una pregunta,
   no un hueco que se rellena inventando.
3. Copiar `plantillas/PREFERENCIAS.md` y `plantillas/CLAUDE.md`, ajustar nombres.
4. Decir **"guía fabric"** para entrar al procedimiento de fases.

## Estado

Versión 0.2.0. Pasa `claude plugin validate --strict` sin errores ni avisos.

Lo que falta:

- Una referencia escrita por fase de la guía. Mientras no exista, la skill guía
  con el mapa de fases y confirma cada paso en Microsoft Learn.
- Dos decisiones abiertas del procedimiento: si las 9 fases sirven en ese orden,
  y si el patrón de workspace lleva el ambiente (`ws-<dominio>-<entorno>`) o no.
