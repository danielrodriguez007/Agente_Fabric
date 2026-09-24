# Guía de estilo — Notion monocromático (blanco/negro)

> Instrucción para el agente: usa este sistema como look visual por defecto en cualquier interfaz HTML que construyas en este proyecto, salvo que se indique lo contrario. Adapta el contenido, pero mantén los tokens de color, la tipografía y los patrones de componentes descritos abajo.

## Principios

- **Monocromático real**: solo blanco, negro y grises. Nada de color en fondos, bordes ni acentos. Los emojis de los íconos son la única excepción (son glifos, no color de marca).
- **Modo claro/oscuro funcional, no decorativo**: todo tiene que verse bien invertido, con un botón real que cambia `data-theme` en `<html>`.
- **Bloques al estilo Notion**: portada, ícono grande, propiedades, *callouts*, *toggles* colapsables, checklist, tablas — no tarjetas genéricas con sombra.
- **Dinamismo real antes que animación decorativa**: preferir interacciones que hacen algo (togglear tema, marcar checklist, cambiar de vista, barra de progreso que se recalcula) sobre efectos puramente visuales.

## Tokens de color

```css
:root{
  --bg:#FFFFFF; --fg:#000000; --muted:#6B6B6B; --border:#000000; --hover:#F2F2F2; --surface:#FFFFFF;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#000000; --fg:#FFFFFF; --muted:#A0A0A0; --border:#FFFFFF; --hover:#1A1A1A; --surface:#000000;
  }
}
:root[data-theme="dark"]{
  --bg:#000000; --fg:#FFFFFF; --muted:#A0A0A0; --border:#FFFFFF; --hover:#1A1A1A; --surface:#000000;
}
```

La portada (`.cover`) es la única excepción: se queda en `#0F0F0F` fijo en ambos temas, como una marca constante en la parte superior de la página.

## Tipografía

- Familia: `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif`
- Pesos usados: 400 (texto), 500 (etiquetas), 600 (subtítulos/summary), 700 (título principal)
- Título de página: 34–40px, peso 700
- Subtítulos de bloque (`h2.bt`): 21px, peso 600
- Texto de párrafo: 15.5–16px, `line-height:1.65`
- Texto muted/metadata: 12.5–14px, color `var(--muted)`

## Layout

- Ancho de contenido efectivo: ~640px para texto de lectura, hasta 900–1100px para tablas/paneles.
- Gutter horizontal de página: `68px` en escritorio, `20–22px` por debajo de `640px` de ancho (ajustar todo con una sola media query).
- Portada (`.cover`): `height:140px`, fondo `#0F0F0F` sólido.
- Ícono: emoji a `font-size:60px`, con `margin-top:-30px` para que se monte sobre la portada.
- Botón de tema: fijo en `top:16px; right:16px`, 30×30px, `border-radius:6px`, `border:1px solid var(--border)`.

## Componentes

**Botón de tema (JS)**
```js
document.getElementById('toggle-theme').addEventListener('click', function(){
  var html = document.documentElement;
  var esOscuro = html.getAttribute('data-theme') === 'dark';
  html.setAttribute('data-theme', esOscuro ? 'light' : 'dark');
  this.textContent = esOscuro ? '🌙' : '☀️';
});
```

**Pills / etiquetas**
```css
.pill{ background:#F1F1EF; color:#000; border:1px solid #000; border-radius:4px; padding:2px 8px; font-size:12.5px; }
:root[data-theme="dark"] .pill{ background:#242424; color:#fff; border-color:#fff; }
```

**Callout**
```css
.callout{ background:#F2F2F2; border-left:3px solid #000; border-radius:6px; padding:14px 16px 14px 13px; display:flex; gap:10px; }
:root[data-theme="dark"] .callout{ background:#1A1A1A; border-left-color:#fff; }
```

**Toggle colapsable** — usar `<details><summary>` nativo, con un triángulo `▶` que rota 90° al abrir (`.toggle[open] summary::before{ transform:rotate(90deg); }`).

**Checklist** — checkbox nativo, `accent-color:#000` (blanco en oscuro), y tachado automático:
```css
.check-item input:checked + label{ color:var(--muted); text-decoration:line-through; }
```

**Tabla / vista de base de datos** — bordes `1px solid var(--border)`, encabezado con `background:var(--hover)` y texto muted en mayúsculas pequeñas.

**Barra de progreso ligada a un checklist** — recalcular el ancho con JS cada vez que cambia un checkbox:
```js
function actualizarProgreso(){
  var boxes = document.querySelectorAll('.checklist input[type=checkbox]');
  var marcados = 0;
  boxes.forEach(function(b){ if(b.checked) marcados++; });
  var pct = Math.round((marcados / boxes.length) * 100);
  barraFill.style.width = pct + '%';
}
```

**Pestañas de vista (ej. Tabla/Galería)** — pestaña activa con `border-bottom:2px solid var(--fg)`, resto en `var(--muted)`.

## Cuándo desviarse

Si el proyecto ya tiene una identidad de marca con color, o el usuario pide explícitamente otra paleta, no forzar este sistema — mencionar que existe como opción, no como regla fija.

---

## Aplicación en este proyecto (nota operativa, 2026-09-16)

Esta guía **reemplaza** la norma de estilo anterior registrada en `project/RECOMENDACIONES.md` sección 9 (monocromo con `"PT Sans", Avenir`, sin modo oscuro). Esa sección quedó marcada como superada — si la lees en una sesión futura, esta guía es la que manda.

El sistema está implementado en una hoja de estilos compartida: **`artifacts/reports/_estilo-notion.css`**. Todo artefacto HTML nuevo bajo `artifacts/reports/` la enlaza con `<link rel="stylesheet" href="_estilo-notion.css">` en vez de repetir el CSS inline. Si un documento necesita estilos propios, van en un `<style>` corto después del `<link>`, no reemplazándolo.

Estructura mínima de página que espera esa hoja de estilos:

```html
<button id="toggle-theme" aria-label="Cambiar tema">🌙</button>
<div class="cover"></div>
<div class="page">
  <div class="page-icon">📊</div>
  <h1>Título de la página</h1>
  <div class="props">…propiedades estilo Notion…</div>
  …contenido…
</div>
```

El JS del botón de tema y de las barras de progreso también vive en la hoja compartida `artifacts/reports/_estilo-notion.js`, para no repetirlo en cada archivo.

---

## Exportación a PDF (procedimiento, 2026-09-21)

Los documentos de `artifacts/reports/` se exportan a PDF renderizando el HTML con **Edge en modo headless**, no imprimiendo a mano desde el navegador: así el resultado es reproducible y conserva el sistema Notion completo.

```powershell
$edge = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
& $edge --headless --disable-gpu --no-first-run --no-pdf-header-footer `
        "--user-data-dir=$env:TEMP\edge_pdf_profile" `
        "--print-to-pdf=<destino>.pdf" "file:///<ruta-absoluta>.html"
```

Tres cosas que cuestan un intento fallido si no se saben:

- **`--user-data-dir` con un perfil aparte no es opcional.** Si el usuario tiene Edge abierto, el modo headless se engancha a esa instancia y `--print-to-pdf` **falla en silencio**: exit code vacío, ningún archivo, ningún error. El perfil aislado lo evita.
- **Un `<details>` cerrado no imprime su contenido.** Los toggles se pierden enteros en el PDF. La solución es generar el PDF desde una copia temporal del HTML con `<details class="toggle" open>`, dejando el archivo original con los toggles colapsados para la lectura en pantalla. La copia va en la misma carpeta para que las rutas relativas al CSS sigan resolviendo, y se borra después.
- **Si el PDF está abierto en un visor, no se puede sobrescribir.** Generar a un nombre temporal y reemplazar con `Move-Item -Force`.

### Los estilos de impresión son compartidos

El bloque `@media print` vive en `_estilo-notion.css` y aplica a todos los documentos. Comprime tipografía, tablas y espaciado, oculta el botón de tema y el pie de página, y libera el ancho de línea (quitar el límite de 640px es lo que más páginas ahorra, sin tocar el tamaño de letra). En el caso medido, un informe pasó de 9 páginas a 5 sin perder legibilidad.

No repitas ese bloque en cada documento. Si uno necesita otra densidad, redefine solo lo que cambie en su propio `<style>`, después del `<link>`.
