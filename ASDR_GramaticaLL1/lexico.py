import sys

PALABRAS_RESERVADAS = {"sin", "cos", "tan", "abs", "mod"}
SIMBOLOS = {"=", ";", "+", "-", "*", "/", "%", "(", ")", "|"}


class Token:
    def __init__(self, tipo, lexema, linea, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna


class ErrorLexico(Exception):
    def __init__(self, mensaje, linea, columna):
        super().__init__(f"[Error léxico] línea {linea}, columna {columna}: {mensaje}")


class Lexico:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.linea = 1
        self.columna = 1

    def actual(self):
        return self.texto[self.pos] if self.pos < len(self.texto) else ""

    def avanzar(self):
        if self.actual() == "\n":
            self.linea += 1
            self.columna = 1
        else:
            self.columna += 1
        self.pos += 1

    def siguiente(self):
        while True:
            c = self.actual()
            if c != "" and c.isspace():
                self.avanzar()
            elif c == "#":
                while self.actual() not in ("", "\n"):
                    self.avanzar()
            else:
                break

        linea, columna = self.linea, self.columna
        c = self.actual()

        if c == "":
            return Token("$", "$", linea, columna)

        if c.isdigit():
            lexema = ""
            while self.actual().isdigit():
                lexema += self.actual()
                self.avanzar()
            if self.actual() == ".":
                lexema += "."
                self.avanzar()
                if not self.actual().isdigit():
                    raise ErrorLexico(f"número mal formado '{lexema}'", linea, columna)
                while self.actual().isdigit():
                    lexema += self.actual()
                    self.avanzar()
            return Token("num", lexema, linea, columna)

        if c.isalpha() or c == "_":
            lexema = ""
            while self.actual().isalnum() or self.actual() == "_":
                lexema += self.actual()
                self.avanzar()
            tipo = lexema if lexema in PALABRAS_RESERVADAS else "id"
            return Token(tipo, lexema, linea, columna)

        if c in SIMBOLOS:
            self.avanzar()
            return Token(c, c, linea, columna)

        raise ErrorLexico(f"carácter no reconocido '{c}'", linea, columna)


def todos_los_tokens(texto):
    lexico = Lexico(texto)
    tokens = []
    while True:
        token = lexico.siguiente()
        tokens.append(token)
        if token.tipo == "$":
            return tokens


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        texto = f.read()
    try:
        for t in todos_los_tokens(texto):
            print(f"{t.tipo:<6}{t.lexema:<10}línea {t.linea}, columna {t.columna}")
    except ErrorLexico as e:
        print(e)
