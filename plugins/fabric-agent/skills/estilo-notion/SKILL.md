---
name: estilo-notion
description: Sistema de estilo visual monocromático tipo Notion para cualquier documento o infografía HTML que se genere en un proyecto. Úsalo antes de escribir el primer HTML de un reporte, checklist, matriz o guía entregable. Incluye la hoja de estilos y el JS de modo claro/oscuro listos para copiar, y los patrones de componente (portada, ícono grande, propiedades, callouts, toggles, checklists con barra de progreso).
---

# Estilo Notion para documentos HTML

Norma única de estilo visual para las interfaces HTML de un proyecto. Sistema monocromático: solo blanco, negro y grises, tipografía Inter, modo claro/oscuro funcional con botón real.

## Cómo usarlo

1. **No repitas el CSS inline en cada documento.** Copia `assets/estilo-notion.css` y `assets/estilo-notion.js` una sola vez a la carpeta de reportes del proyecto (por ejemplo `artifacts/reports/`), con los nombres `_estilo-notion.css` y `_estilo-notion.js`, y enlázalos con rutas relativas desde cada HTML.
2. Si los archivos ya existen en el proyecto, úsalos tal cual: son la versión vigente. No los reescribas para un documento nuevo.
3. Lee `referencia.md` para los tokens de color, la tipografía y los patrones de componente antes de inventar un elemento que ya está definido.
4. Adapta el contenido, nunca los tokens: el sistema es monocromático a propósito. Si un documento necesita color, es señal de que el dato debería ir en una tabla o un gráfico, no en un adorno.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| `referencia.md` | La norma completa: tokens, tipografía, componentes |
| `assets/estilo-notion.css` | Hoja de estilos, lista para copiar al proyecto |
| `assets/estilo-notion.js` | Alternancia de modo claro/oscuro |
