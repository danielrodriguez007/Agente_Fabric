# Guía de activación de MCP servers para Microsoft Fabric

Este documento solo describe **cómo** activar cada MCP server cuando decidas hacerlo. No se ha instalado ni configurado nada todavía — no existe `.mcp.json` en este proyecto. Cuando quieras activar alguno, crea (o pide que se cree) `.mcp.json` en la raíz de este proyecto con el bloque correspondiente.

Todos los MCP oficiales de Microsoft para Fabric/Power BI requieren una cuenta **Microsoft Entra ID** con acceso al tenant/capacidad de Fabric correspondiente. Confirma que tienes ese acceso antes de intentar usarlos.

## 1. Fabric Core MCP Server (remoto) — recomendado para empezar

Qué hace: expone las APIs públicas de Fabric como herramientas MCP tipadas — workspaces, items, permisos, carpetas. Autenticación OAuth 2.0 vía Entra ID, respeta tu rol (Admin/Member/Contributor/Viewer) y queda auditado en los logs de Fabric.

Estado: **Preview** — la configuración puede cambiar antes de GA.

Instalación: ninguna, es un endpoint remoto. Solo agrega la URL a tu `.mcp.json` y autentica con tu cuenta la primera vez que se use (flujo interactivo de login).

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

Repo: https://github.com/microsoft/fabric-cli
Docs: https://learn.microsoft.com/en-us/rest/api/fabric/articles/fabric-command-line-interface

## Plantilla de `.mcp.json` (ejemplo, ajustar cuando decidas activarlos)

```json
{
  "mcpServers": {
    "fabric-core": {
      "type": "http",
      "url": "<URL del endpoint remoto de Fabric Core MCP — confirmar en la doc oficial al momento de activarlo>"
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

No se han rellenado los valores exactos de comando/URL a propósito: cambian con las versiones y requieren que confirmes la más reciente en la documentación oficial (enlaces arriba) en el momento en que actives cada uno.
