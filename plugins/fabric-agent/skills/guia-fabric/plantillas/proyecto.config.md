# Configuración del proyecto Fabric

> Copia este archivo al repo del proyecto y llénalo. Es lo único que cambia entre proyectos: la skill `fabric-cero-a-bronce` lo lee antes de guiar cualquier fase.
> Si un valor no se conoce, escribe `POR DEFINIR`. No lo inventes.

## 1. Identidad del proyecto

| Campo | Valor |
|---|---|
| Organización | POR DEFINIR |
| Nombre del proyecto | POR DEFINIR |
| Sponsor (quién decide) | POR DEFINIR |
| Líder técnico | POR DEFINIR |
| Fecha de inicio | POR DEFINIR |

## 2. Pregunta de negocio y fuente piloto (Fase 0)

- **Decisión que soporta el piloto:** POR DEFINIR
- **Área usuaria:** POR DEFINIR
- **Fuente piloto:** POR DEFINIR
- **Por qué esta fuente:** POR DEFINIR

## 3. Tenant, roles y responsables (Fases 1 y 3)

| Rol | Persona o grupo | Notas |
|---|---|---|
| Fabric Administrator (tenant) | POR DEFINIR | |
| Capacity Administrator | POR DEFINIR | |
| Grupo de Entra habilitado para crear en Fabric | POR DEFINIR | |
| Dueño de datos por dominio | POR DEFINIR | |
| Responsable de protección de datos personales | POR DEFINIR | Según la regulación local aplicable |
| Equipo de red / infraestructura | POR DEFINIR | |

## 4. Capacidad (Fase 2)

| Campo | Valor |
|---|---|
| Tipo | Trial / F-SKU: POR DEFINIR |
| SKU inicial | POR DEFINIR |
| Región de Azure | POR DEFINIR (debe coincidir con la región de los gateways) |
| Modelo de pago | PAYG / reservado: POR DEFINIR |
| Horario de pausa | POR DEFINIR |
| Suscripción y grupo de recursos de Azure | POR DEFINIR |

## 5. Convención de nombres (Fase 3)

Ajusta los patrones al estándar de la organización si ya existe uno.

| Item | Patrón | Ejemplo |
|---|---|---|
| Workspace | `ws-<dominio>-<entorno>` | `ws-ventas-dev` |
| Lakehouse | `lh_<dominio>` | `lh_ventas` |
| Pipeline | `pl_<fuente>_<frecuencia>` | `pl_erp_diario` |
| Notebook | `nb_<fuente>_<capa-o-propósito>` | `nb_erp_bronze` |
| Connection | `cn_<fuente>_<entorno>` | `cn_erp_dev` |
| Carpeta Bronze | `Files/bronze/<fuente>/<endpoint-o-tabla>/` | `Files/bronze/erp/proveedores/` |

## 6. Entornos y control de versiones (Fase 4)

| Campo | Valor |
|---|---|
| Entornos | Dev / Test / Prod: POR DEFINIR |
| Repositorio Git | Azure DevOps / GitHub: POR DEFINIR |
| Mecanismo de promoción | Deployment Pipelines / fabric-cicd: POR DEFINIR |

## 7. Inventario de fuentes (Fase 5)

| Fuente | Dominio | Dónde está desplegada | Forma de conexión | Autenticación | Quién habilita | Quién autoriza | Prioridad | Estado |
|---|---|---|---|---|---|---|---|---|
| POR DEFINIR | | | | | | | | |

## 8. Exclusiones de datos

Datos que **no se ingestan** en Fabric por sensibilidad o por contrato, aunque sea técnicamente posible:

- POR DEFINIR

## 9. Estado por fase

| Fase | Estado | Fecha de cierre | Riesgos aceptados o notas |
|---|---|---|---|
| 0 · Arranque | Pendiente | | |
| 1 · Tenant y roles | Pendiente | | |
| 2 · Capacidad | Pendiente | | |
| 3 · Gobierno base | Pendiente | | |
| 4 · Workspaces y entornos | Pendiente | | |
| 5 · Inventario de fuentes | Pendiente | | |
| 6 · Conectividad | Pendiente | | |
| 7 · Ingesta a Bronze | Pendiente | | |
| 8 · Orquestación y operación | Pendiente | | |
