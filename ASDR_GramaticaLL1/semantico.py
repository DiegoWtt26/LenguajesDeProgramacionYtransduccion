import math


class ErrorSemantico(Exception):
    def __init__(self, mensaje, token):
        super().__init__(
            f"[Error semántico] línea {token.linea}, columna {token.columna}: {mensaje}"
        )


class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = {}
        self.errores = []

    def ejecutar(self, sentencias):
        for sentencia in sentencias:
            _, variable, expresion = sentencia
            try:
                valor = self.evaluar(expresion)
                self.tabla_simbolos[variable.lexema] = valor
                print(f"  {variable.lexema} = {formato(valor)}")
            except ErrorSemantico as error:
                self.errores.append(str(error))
                print(f"  {variable.lexema} = (no asignada por error)")

    def evaluar(self, nodo):
        tipo = nodo[0]

        if tipo == "numero":
            return float(nodo[1].lexema)

        if tipo == "variable":
            nombre = nodo[1].lexema
            if nombre not in self.tabla_simbolos:
                raise ErrorSemantico(f"la variable '{nombre}' no ha sido declarada", nodo[1])
            return self.tabla_simbolos[nombre]

        if tipo == "negativo":
            return -self.evaluar(nodo[2])

        if tipo == "absoluto":
            return abs(self.evaluar(nodo[2]))

        if tipo == "funcion":
            nombre = nodo[1]
            argumento = self.evaluar(nodo[2])
            if nombre.tipo == "sin":
                return math.sin(argumento)
            if nombre.tipo == "cos":
                return math.cos(argumento)
            if nombre.tipo == "abs":
                return abs(argumento)
            if abs(math.cos(argumento)) < 1e-12:
                raise ErrorSemantico(f"tan no está definida para {formato(argumento)}", nombre)
            return math.tan(argumento)

        operador = nodo[1]
        izquierdo = self.evaluar(nodo[2])
        derecho = self.evaluar(nodo[3])
        if operador.tipo == "+":
            return izquierdo + derecho
        if operador.tipo == "-":
            return izquierdo - derecho
        if operador.tipo == "*":
            return izquierdo * derecho
        if derecho == 0:
            texto = "división entre cero" if operador.tipo == "/" else "módulo entre cero"
            raise ErrorSemantico(texto, operador)
        if operador.tipo == "/":
            return izquierdo / derecho
        return izquierdo % derecho


def formato(valor):
    if abs(valor - round(valor)) < 1e-12:
        return str(int(round(valor)))
    texto = f"{valor:.6f}".rstrip("0").rstrip(".")
    return "0" if texto == "-0" else texto


if __name__ == "__main__":
    import sys
    from lexico import ErrorLexico
    from parser import ErrorSintactico, Parser

    with open(sys.argv[1], encoding="utf-8") as f:
        texto = f.read()
    try:
        sentencias = Parser(texto).inicio()
    except (ErrorLexico, ErrorSintactico) as e:
        print(e)
        sys.exit(1)

    semantico = AnalizadorSemantico()
    semantico.ejecutar(sentencias)
    for error in semantico.errores:
        print(error)
    print("Tabla de símbolos:", {k: formato(v) for k, v in semantico.tabla_simbolos.items()})
