/* ============================================================
   Comportamiento compartido — sistema Notion monocromático
   Norma del proyecto: project/ESTILO-NOTION.md
   Enlazar con: <script src="_estilo-notion.js" defer></script>
   ============================================================ */

(function () {
  "use strict";

  function onReady(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  /* ---- Botón de tema ---- */
  function initTema() {
    var btn = document.getElementById("toggle-theme");
    if (!btn) return;
    var html = document.documentElement;

    // Recupera la preferencia previa de este navegador, si existe.
    try {
      var guardado = localStorage.getItem("tema-notion");
      if (guardado === "dark" || guardado === "light") {
        html.setAttribute("data-theme", guardado);
      }
    } catch (e) {}

    function esOscuroAhora() {
      var attr = html.getAttribute("data-theme");
      if (attr === "dark") return true;
      if (attr === "light") return false;
      return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    }

    function pintarIcono() {
      btn.textContent = esOscuroAhora() ? "☀️" : "🌙";
    }

    btn.addEventListener("click", function () {
      var oscuro = esOscuroAhora();
      var nuevo = oscuro ? "light" : "dark";
      html.setAttribute("data-theme", nuevo);
      try { localStorage.setItem("tema-notion", nuevo); } catch (e) {}
      pintarIcono();
    });

    pintarIcono();
  }

  /* ---- Checklists con persistencia y barra de progreso ----
     Cada .checklist con [data-store] guarda su estado en este navegador.
     La barra se declara como:
       <div class="progress" data-for="<id del checklist>">
         <div class="track"><div class="fill"></div></div>
         <p class="lbl"><b>0/0</b> …</p>
       </div>                                                    */
  function initChecklists() {
    var listas = document.querySelectorAll(".checklist");
    Array.prototype.forEach.call(listas, function (lista) {
      var clave = lista.getAttribute("data-store");
      var boxes = lista.querySelectorAll('input[type="checkbox"]');
      if (!boxes.length) return;

      var barra = lista.id
        ? document.querySelector('.progress[data-for="' + lista.id + '"]')
        : null;
      var fill = barra ? barra.querySelector(".fill") : null;
      var etiqueta = barra ? barra.querySelector(".lbl b") : null;

      function leerEstado() {
        if (!clave) return {};
        try { return JSON.parse(localStorage.getItem(clave) || "{}"); }
        catch (e) { return {}; }
      }
      function guardarEstado(s) {
        if (!clave) return;
        try { localStorage.setItem(clave, JSON.stringify(s)); } catch (e) {}
      }

      function actualizarProgreso() {
        var marcados = 0;
        Array.prototype.forEach.call(boxes, function (b) { if (b.checked) marcados++; });
        var pct = Math.round((marcados / boxes.length) * 100);
        if (fill) fill.style.width = pct + "%";
        if (etiqueta) etiqueta.textContent = marcados + "/" + boxes.length;
      }

      var estado = leerEstado();
      Array.prototype.forEach.call(boxes, function (b) {
        if (b.id && estado[b.id]) b.checked = true;
        b.addEventListener("change", function () {
          if (b.id) {
            var s = leerEstado();
            s[b.id] = b.checked;
            guardarEstado(s);
          }
          actualizarProgreso();
        });
      });

      actualizarProgreso();
    });
  }

  /* ---- Filtro de tablas ----
     <input data-filtra="<id de la tabla>"> filtra sus filas.
     Las filas .grouprow (encabezados de grupo) se ocultan si
     no les queda ninguna fila visible debajo.
     Un [data-contador="<id>"] recibe el conteo.                 */
  function initFiltros() {
    var inputs = document.querySelectorAll("input[data-filtra]");
    Array.prototype.forEach.call(inputs, function (input) {
      var tabla = document.getElementById(input.getAttribute("data-filtra"));
      if (!tabla) return;

      var cuerpo = tabla.tBodies[0];
      if (!cuerpo) return;

      var todas = Array.prototype.slice.call(cuerpo.rows);
      var datos = todas.filter(function (tr) { return !tr.classList.contains("grouprow"); });
      var grupos = todas.filter(function (tr) { return tr.classList.contains("grouprow"); });
      var contador = document.querySelector('[data-contador="' + tabla.id + '"]');

      function normalizar(s) {
        return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "");
      }

      function pintarContador(n) {
        if (!contador) return;
        contador.textContent = n === datos.length
          ? datos.length + " filas"
          : n + " de " + datos.length;
      }

      function filtrar() {
        var q = normalizar(input.value.trim());
        var visibles = 0;
        datos.forEach(function (tr) {
          var ok = !q || normalizar(tr.innerText).indexOf(q) !== -1;
          tr.style.display = ok ? "" : "none";
          if (ok) visibles++;
        });
        grupos.forEach(function (g) {
          var hay = false;
          var n = g.nextElementSibling;
          while (n && !n.classList.contains("grouprow")) {
            if (n.style.display !== "none") { hay = true; break; }
            n = n.nextElementSibling;
          }
          g.style.display = hay ? "" : "none";
        });
        pintarContador(visibles);
      }

      input.addEventListener("input", filtrar);
      pintarContador(datos.length);
    });
  }

  /* ---- Copiar al portapapeles ----
     <button data-copia="<id del bloque>">Copiar</button>        */
  function initCopiar() {
    var botones = document.querySelectorAll("button[data-copia]");
    Array.prototype.forEach.call(botones, function (btn) {
      var origen = document.getElementById(btn.getAttribute("data-copia"));
      if (!origen) return;

      btn.addEventListener("click", function () {
        var texto = origen.innerText;
        var previo = btn.textContent;

        function ok() {
          btn.textContent = "Copiado ✓";
          setTimeout(function () { btn.textContent = previo; }, 2000);
        }
        function fallback() {
          var ta = document.createElement("textarea");
          ta.value = texto;
          ta.style.position = "fixed";
          ta.style.opacity = "0";
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand("copy"); ok(); }
          catch (e) { btn.textContent = "Selecciona y copia a mano"; }
          document.body.removeChild(ta);
        }

        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(texto).then(ok, fallback);
        } else {
          fallback();
        }
      });
    });
  }

  onReady(function () {
    initTema();
    initChecklists();
    initFiltros();
    initCopiar();
  });
})();
