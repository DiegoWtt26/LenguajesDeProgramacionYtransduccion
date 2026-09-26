from antlr4.error.ErrorListener import ErrorListener


class ListenerErroresLexicos(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        caracter = msg.split("at: ", 1)[-1]
        self.errores.append(
            f"[Error léxico] línea {line}, columna {column + 1}: "
            f"carácter no reconocido {caracter}"
        )


class ListenerErroresSintacticos(ErrorListener):

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        encontrado = offendingSymbol.text
        if encontrado == "<EOF>":
            encontrado = "fin de archivo"

        esperados = recognizer.getExpectedTokens().toString(
            recognizer.literalNames, recognizer.symbolicNames
        )
        esperados = esperados.replace("<EOF>", "fin de archivo")

        if msg.startswith("missing"):
            detalle = f"falta un token antes de '{encontrado}'"
        elif msg.startswith("extraneous"):
            detalle = f"sobra el token '{encontrado}'"
        else:
            detalle = f"token inesperado '{encontrado}'"

        anterior = recognizer.getTokenStream().LT(-1)
        if "';'" in esperados and anterior is not None and anterior.line < line:
            detalle += f" (¿falta ';' al final de la línea {anterior.line}?)"

        self.errores.append(
            f"[Error sintáctico] línea {line}, columna {column + 1}: "
            f"{detalle}. Se esperaba: {esperados}"
        )
