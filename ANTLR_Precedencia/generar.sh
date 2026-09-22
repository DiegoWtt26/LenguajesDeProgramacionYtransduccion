#!/usr/bin/env bash
# Genera los 4 lexers/parsers Python con ANTLR 4.13.2
# Uso: ./generar.sh
# Opcional: export ANTLR_JAR=/ruta/a/antlr-4.13.2-complete.jar
set -e
JAR="${ANTLR_JAR:-/tmp/antlr-4.13.2-complete.jar}"
if [ ! -f "$JAR" ]; then
  echo "No se encontro \"$JAR\""
  echo "Descarga antlr-4.13.2-complete.jar de https://www.antlr.org/download/ y exporta ANTLR_JAR"
  exit 1
fi
java -jar "$JAR" -Dlanguage=Python3 -visitor -o generado gramatica/PrecLeft.g4 gramatica/PrecRight.g4 gramatica/PrecInv.g4 gramatica/PrecFlat.g4
echo "Listo. 4 parsers generados en generado/ (PrecLeft/Right/Inv/Flat)."
