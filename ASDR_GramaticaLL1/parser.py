import sys

from lexico import Lexico, ErrorLexico

INICIO_EXPR = {"id", "num", "-", "(", "|", "sin", "cos", "tan", "abs"}
INICIO_PRIMARIO = {"id", "num", "(", "|", "sin", "cos", "tan", "abs"}
FUNCIONES = {"sin", "cos", "tan", "abs"}
SIGUIENTES_EXPRP = {";", ")", "|"}
SIGUIENTES_TERMP = {";", ")", "|", "+", "-"}


class ErrorSintactico(Exception):
    pass


class Parser:
    def __init__(self, texto):
        self.lexico = Lexico(texto)
        self.token = self.lexico.siguiente()
        self.anterior = None

    def error(self, esperado):
        t = self.token
        encontrado = "fin de archivo" if t.tipo == "$" else f"'{t.lexema}'"
        mensaje = (f"[Error sintáctico] línea {t.linea}, columna {t.columna}: "
                   f"se esperaba {esperado} pero se encontró {encontrado}")
        if "';'" in esperado and self.anterior and self.anterior.linea < t.linea:
            mensaje += f" (¿falta ';' al final de la línea {self.anterior.linea}?)"
        raise ErrorSintactico(mensaje)

    def emparejar(self, esperado):
        if self.token.tipo != esperado:
            self.error(f"'{esperado}'")
        self.anterior = self.token
        self.token = self.lexico.siguiente()
        return self.anterior

    # 1. inicio -> programa $
    def inicio(self):
        sentencias = self.programa()
        self.emparejar("$")
        return sentencias

    # 2. programa -> sentencia programa      PRED = { id }
    # 3. programa -> ε                       PRED = { $ }
    def programa(self):
        if self.token.tipo == "id":
            primera = self.sentencia()
            resto = self.programa()
            return [primera] + resto
        if self.token.tipo == "$":
            return []
        self.error("una variable o el fin de archivo")

    # 4. sentencia -> id = expr ;
    def sentencia(self):
        variable = self.emparejar("id")
        self.emparejar("=")
        valor = self.expr()
        self.emparejar(";")
        return ("asignacion", variable, valor)

    # 5. expr -> term exprP                  PRED = { id, num, -, (, |, sin, cos, tan, abs }
    def expr(self):
        if self.token.tipo not in INICIO_EXPR:
            self.error("un número, una variable, una función, '-', '(' o '|'")
        izquierdo = self.term()
        return self.exprP(izquierdo)

    # 6. exprP -> + term exprP               PRED = { + }
    # 7. exprP -> - term exprP               PRED = { - }
    # 8. exprP -> ε                          PRED = { ;, ), | }
    def exprP(self, izquierdo):
        if self.token.tipo in ("+", "-"):
            operador = self.emparejar(self.token.tipo)
            derecho = self.term()
            return self.exprP(("operacion", operador, izquierdo, derecho))
        if self.token.tipo in SIGUIENTES_EXPRP:
            return izquierdo
        self.error("un operador, ';', ')' o '|'")

    # 9. term -> factor termP
    def term(self):
        izquierdo = self.factor()
        return self.termP(izquierdo)

    # 10. termP -> * factor termP            PRED = { * }
    # 11. termP -> / factor termP            PRED = { / }
    # 12. termP -> mod factor termP          PRED = { mod }
    # 13. termP -> % factor termP            PRED = { % }
    # 14. termP -> ε                         PRED = { ;, +, -, ), | }
    def termP(self, izquierdo):
        if self.token.tipo in ("*", "/", "mod", "%"):
            operador = self.emparejar(self.token.tipo)
            derecho = self.factor()
            return self.termP(("operacion", operador, izquierdo, derecho))
        if self.token.tipo in SIGUIENTES_TERMP:
            return izquierdo
        self.error("un operador, ';', ')' o '|'")

    # 15. factor -> - factor                 PRED = { - }
    # 16. factor -> primario                 PRED = { id, num, (, |, sin, cos, tan, abs }
    def factor(self):
        if self.token.tipo == "-":
            operador = self.emparejar("-")
            return ("negativo", operador, self.factor())
        if self.token.tipo in INICIO_PRIMARIO:
            return self.primario()
        self.error("un número, una variable, una función, '-', '(' o '|'")

    # 17. primario -> num                    PRED = { num }
    # 18. primario -> id                     PRED = { id }
    # 19. primario -> ( expr )               PRED = { ( }
    # 20. primario -> | expr |               PRED = { | }
    # 21. primario -> func ( expr )          PRED = { sin, cos, tan, abs }
    def primario(self):
        tipo = self.token.tipo
        if tipo == "num":
            return ("numero", self.emparejar("num"))
        if tipo == "id":
            return ("variable", self.emparejar("id"))
        if tipo == "(":
            self.emparejar("(")
            valor = self.expr()
            self.emparejar(")")
            return valor
        if tipo == "|":
            barra = self.emparejar("|")
            valor = self.expr()
            self.emparejar("|")
            return ("absoluto", barra, valor)
        if tipo in FUNCIONES:
            nombre = self.func()
            self.emparejar("(")
            valor = self.expr()
            self.emparejar(")")
            return ("funcion", nombre, valor)
        self.error("un número, una variable, una función, '(' o '|'")

    # 22-25. func -> sin | cos | tan | abs
    def func(self):
        if self.token.tipo in FUNCIONES:
            return self.emparejar(self.token.tipo)
        self.error("sin, cos, tan o abs")


def partes(nodo):
    tipo = nodo[0]
    if tipo == "asignacion":
        return f"{nodo[1].lexema} =", [nodo[2]]
    if tipo == "operacion":
        return nodo[1].lexema, [nodo[2], nodo[3]]
    if tipo == "negativo":
        return "- (negativo)", [nodo[2]]
    if tipo == "absoluto":
        return "| | (valor absoluto)", [nodo[2]]
    if tipo == "funcion":
        return f"{nodo[1].lexema}( )", [nodo[2]]
    return nodo[1].lexema, []


def mostrar_arbol(nodo, prefijo="", ultimo=True, raiz=True):
    etiqueta, hijos = partes(nodo)
    if raiz:
        print(etiqueta)
        nuevo_prefijo = ""
    else:
        print(prefijo + ("└── " if ultimo else "├── ") + etiqueta)
        nuevo_prefijo = prefijo + ("    " if ultimo else "│   ")
    for i, hijo in enumerate(hijos):
        mostrar_arbol(hijo, nuevo_prefijo, i == len(hijos) - 1, False)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        texto = f.read()
    try:
        for sentencia in Parser(texto).inicio():
            mostrar_arbol(sentencia)
            print()
        print("Análisis sintáctico correcto")
    except (ErrorLexico, ErrorSintactico) as e:
        print(e)
