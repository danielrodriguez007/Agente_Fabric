#!/bin/sh
# Ejecuta un script con el primer Python 3 que funcione: python3 en macOS/Linux,
# python o py en Windows (donde python3 suele ser un acceso directo de la Store
# que no ejecuta nada). exec conserva la entrada estandar que manda Claude Code.
for p in python3 python py; do
  if "$p" -c "import sys; sys.exit(0 if sys.version_info[0] == 3 else 1)" >/dev/null 2>&1; then
    exec "$p" "$@"
  fi
done
echo "fabric-agent: no se encontro Python 3 (python3, python o py)." >&2
exit 1
