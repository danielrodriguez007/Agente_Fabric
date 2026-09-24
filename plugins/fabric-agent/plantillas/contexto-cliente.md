# Contexto del cliente — <ORGANIZACIÓN>

Este archivo es lo único que cambia entre proyectos. El perfil `fabric-specialist`
del plugin es portable y no sabe nada del cliente: lo que sepa, lo sabe de aquí.

**Regla de llenado:** lo que no se sepa queda como `POR DEFINIR` y se convierte en
pregunta al usuario. Nunca se inventa un valor para no dejar el hueco.

## 1. Organización y alcance

- **Cliente:** POR DEFINIR
- **Sector / tipo de organización:** POR DEFINIR
- **Qué se está construyendo:** POR DEFINIR
- **Fuente de verdad del discovery:** POR DEFINIR (ruta a los documentos del cliente)

## 2. Decisiones ya tomadas por el cliente

Lo que el discovery o el cliente ya prescribió. **Esto manda sobre cualquier
supuesto del perfil.** Si aquí hay una convención, no se proponen alternativas.

| Tema | Decisión | Dónde consta |
|---|---|---|
| Plataforma | POR DEFINIR | |
| Naming de workspaces | POR DEFINIR | |
| Naming de Lakehouse / Warehouse | POR DEFINIR | |
| Naming de pipelines / notebooks | POR DEFINIR | |
| Capacidad (SKU, región) | POR DEFINIR | |

## 3. Decisiones deliberadamente abiertas

Lo que **no** se ha decidido y no debe cerrarse por inercia. Anotar por qué sigue
abierto y qué haría falta para cerrarlo.

| Tema | Por qué sigue abierto | Qué lo cierra |
|---|---|---|
| | | |

## 4. Dominios y áreas

Quién es dueño de qué. Un dominio agrupa varias áreas bajo un mismo dueño de dato.
Los dueños sin confirmar se dicen explícitamente, no se asumen.

| Dominio | Áreas | Data Owner |
|---|---|---|
| | | |

## 5. Fuentes de datos

| Fuente | Dónde está desplegada | Forma de conexión | Estado |
|---|---|---|---|
| | | | |

Las **cinco preguntas por fuente** (dónde está desplegada · qué tipo de conexión
aplica · con qué credenciales se accede · quién habilita · quién autoriza) son el
protocolo para cualquier fuente nueva. Ver la skill `fabric-cero-a-bronce`.

## 6. Secuencia de trabajo

Olas, fases o prioridades acordadas, y quién decide el orden.

- POR DEFINIR

## 7. Gobierno y restricciones no negociables

Datos que no se ingestan, quién valida el acceso a datos personales, marco legal
aplicable, exclusiones permanentes.

- POR DEFINIR

## 8. Personas y roles

| Nombre | Rol | Para qué se le busca |
|---|---|---|
| | | |

## 9. Estado actual

Dónde está el proyecto hoy, en dos o tres líneas. Se actualiza al cerrar cada hito.

- POR DEFINIR
