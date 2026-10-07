# Guía de activación de MCP servers para Microsoft Fabric

Este documento describe **cómo** activar cada MCP server en un proyecto. El plugin no instala ninguno: cada proyecto decide cuáles usa y los declara en su propio `.mcp.json`, en la raíz del repositorio.

**Qué está comprobado en uso y qué no.** El Fabric Core MCP (sección 1) y la Fabric CLI (al final) se usaron contra un tenant real el 2026-10-06. Las demás secciones describen opciones según la documentación de Microsoft: confirma su estado en el enlace de cada una al momento de activarlas.

Todos los MCP oficiales de Microsoft para Fabric/Power BI requieren una cuenta **Microsoft Entra ID** con acceso al tenant/capacidad de Fabric correspondiente. Confirma que tienes ese acceso antes de intentar usarlos.

## 1. Fabric Core MCP Server (remoto) — recomendado para empezar

Qué hace: expone las APIs públicas de Fabric como herramientas MCP tipadas — workspaces, items, permisos, carpetas. Autenticación OAuth 2.0 vía Entra ID, respeta tu rol (Admin/Member/Contributor/Viewer) y queda auditado en los logs de Fabric.

Estado: **Preview** — la configuración puede cambiar antes de GA.

Instalación: ninguna, es un endpoint remoto. Agrega este bloque a `.mcp.json` y autentica con tu cuenta la primera vez que se use (flujo interactivo de login):

```json
{
  "mcpServers": {
    "fabric": {
      "type": "http",
      "url": "https://api.fabric.microsoft.com/v1/mcp/core"
    }
  }
}
```

Lo que se comprobó en uso (2026-10-06):

- **Solo administra recursos**: workspaces, items, permisos, carpetas y capacidades. No lee filas de tablas ni ejecuta pipelines.
- **Su login es independiente del de la Fabric CLI.** Autenticar uno no autentica el otro.
- **Para inspeccionar un tenant rinde más la CLI** (`fab ls`, `fab export`, `fab job run-list`): ver el final de este documento.

Referencia: https://learn.microsoft.com/en-us/rest/api/fabric/articles/mcp-servers/core-remote/overview-core-mcp-server

## 2. Fabric MCP Server (local) — para desarrollo offline

Qué hace: subproceso local open source que da acceso a la documentación completa de las APIs de Fabric (specs OpenAPI empaquetadas), operaciones sobre OneLake y creación de items base — sin necesitar conexión en vivo a un workspace.

Estado: Public Preview, open source.

Instalación: vía extensión de VS Code, o directamente desde el repo open source:
- Repo: https://github.com/microsoft/mcp/tree/main/servers/Fabric.Mcp.Server

Úsalo cuando quieras que el agente conozca la API/mejores prácticas de Fabric sin depender de que el workspace esté disponible en ese momento.

## 3. Fabric Real-Time Intelligence MCP (RTI)

Qué hace: herramientas para Eventhouse, KQL y Azure Data Explorer — consultas y análisis de datos en tiempo real.

Repo: https://github.com/microsoft/fabric-rti-mcp

## 4. Power BI MCP (remoto y local)

Qué hace:
- **Remoto**: endpoint hospedado que permite conversar en lenguaje natural con modelos semánticos de Power BI; usa Copilot para generar y ejecutar consultas DAX.
- **Local**: corre en tu máquina y actúa directamente sobre modelos en Power BI Desktop, workspaces de Fabric o archivos de proyecto Power BI (PBIP) — los cambios siguen tu flujo normal de control de versiones.

Referencia: https://learn.microsoft.com/en-us/power-bi/developer/mcp/mcp-servers-overview

Alternativa open source de la comunidad (útil para TMDL/DAX/deploy más granular): `microsoft/fabric-toolbox` → `SemanticModelMCPServer` — https://github.com/microsoft/fabric-toolbox/tree/main/tools/SemanticModelMCPServer

## 5. Microsoft SQL MCP

Qué hace: consultas en lenguaje natural sobre bases de datos SQL — aplicable al SQL endpoint de un Lakehouse o a un Warehouse de Fabric.

## 6. Azure MCP / Azure DevOps MCP (opcionales)

- **Azure MCP** (GA): agrupa todas las herramientas de Azure en un solo servidor — útil si la solución Fabric se integra con otros recursos de Azure (Key Vault, Storage, etc.).
- **Azure DevOps MCP**: útil si el pipeline de CI/CD de las soluciones Fabric vive en Azure DevOps en vez de GitHub Actions.

## Complemento (no es MCP): Fabric CLI (`fab`)

Ya es **GA** (General Availability) y es la forma más robusta hoy de automatizar Fabric por línea de comandos o en CI/CD:
- Comando `fab deploy` integra la librería `fabric-cicd` para desplegar un workspace completo con un solo comando (funciona en terminal local, GitHub Actions y Azure DevOps Pipelines).
- Navegación tipo sistema de archivos sobre workspaces/items (`cd`, `ls`, `cp`, `rm`).
- Soporte de primera clase para Power BI: rebind de reportes, refresh de modelos semánticos, gestión de propiedades — sin pasar por el portal.
- Disparo y monitoreo de Data Pipelines desde la terminal.
- Modo REPL interactivo, capa de ejecución para agentes de IA.

Instalación: `pip install ms-fabric-cli` (paquete `ms-fabric-cli` en PyPI) o ver el repo oficial.

Lo que se comprobó en uso (2026-10-06):

- **El login es interactivo** (`fab auth login`) y la CLI mantiene **una sola sesión** a la vez. Si Claude corre en una terminal no interactiva, el login se hace en una ventana aparte; en Windows: `Start-Process powershell -ArgumentList '-NoExit','-Command','fab auth login'`.
- **Antes de pedirle al usuario que verifique algo en el portal, se revisa con la CLI**: `fab ls` para recorrer workspaces e items, `fab export` para comparar un notebook del portal con el del repositorio, `fab job run-list` para ver si un pipeline corrió. Al comparar notebooks, enmascara cualquier secreto en la salida.

Repo: https://github.com/microsoft/fabric-cli
Docs: https://learn.microsoft.com/en-us/rest/api/fabric/articles/fabric-command-line-interface

## Plantilla de `.mcp.json` (ejemplo, ajustar cuando decidas activarlos)

```json
{
  "mcpServers": {
    "fabric": {
      "type": "http",
      "url": "https://api.fabric.microsoft.com/v1/mcp/core"
    },
    "fabric-local": {
      "command": "<comando de arranque del Fabric MCP Server local, según instrucciones de microsoft/mcp>"
    },
    "fabric-rti": {
      "command": "<comando de arranque de fabric-rti-mcp, según README del repo>"
    },
    "powerbi": {
      "type": "http",
      "url": "<URL del Power BI MCP remoto, o comando local según la doc oficial>"
    }
  }
}
```

Solo la URL de Fabric Core está rellenada, porque es la única comprobada en uso. Las demás cambian con las versiones: confirma la vigente en la documentación oficial (enlaces arriba) al activar cada una.
