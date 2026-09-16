#!/usr/bin/env bash
# Genera los lexers/parsers Python desde ambas gramaticas (ANTLR 4.13.2)
# Uso: ./generar.sh
# Opcional: export ANTLR_JAR=/ruta/a/antlr-4.13.2-complete.jar
set -e
JAR="${ANTLR_JAR:-/tmp/antlr-4.13.2-complete.jar}"
if [ ! -f "$JAR" ]; then
  echo "No se encontro \"$JAR\""
  echo "Descarga antlr-4.13.2-complete.jar de https://www.antlr.org/download/ y exporta ANTLR_JAR"
  exit 1
fi
java -jar "$JAR" -Dlanguage=Python3 -visitor ExprAmb.g4 ExprAmbInv.g4
echo "Listo."
