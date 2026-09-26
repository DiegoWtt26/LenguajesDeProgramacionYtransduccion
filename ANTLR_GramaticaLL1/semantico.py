import math

from generated.CalculadoraVisitor import CalculadoraVisitor


class ErrorSemantico(Exception):
    def __init__(self, mensaje, token):
        super().__init__(
            f"[Error semántico] línea {token.line}, columna {token.column + 1}: {mensaje}"
        )


class AnalizadorSemantico(CalculadoraVisitor):

    def __init__(self):
        self.tabla_simbolos = {}
        self.errores = []

    # inicio : programa EOF
    def visitInicio(self, ctx):
        self.visit(ctx.programa())

    # programa : sentencia programa | ε
    def visitPrograma(self, ctx):
        while ctx is not None and ctx.sentencia() is not None:
            self.visit(ctx.sentencia())
            ctx = ctx.programa()

    # sentencia : ID ASIGNAR expr PUNTOYCOMA
    def visitSentencia(self, ctx):
        nombre = ctx.ID().getText()
        try:
            valor = self.visit(ctx.expr())
            self.tabla_simbolos[nombre] = valor
            print(f"  {nombre} = {formato(valor)}")
        except ErrorSemantico as error:
            self.errores.append(str(error))
            print(f"  {nombre} = (no asignada por error)")

    # expr : term exprP
    def visitExpr(self, ctx):
        izquierdo = self.visit(ctx.term())
        return self.evaluar_exprP(ctx.exprP(), izquierdo)

    # exprP : MAS term exprP | MENOS term exprP | ε
    def evaluar_exprP(self, ctx, izquierdo):
        if ctx.term() is None:
            return izquierdo
        derecho = self.visit(ctx.term())
        if ctx.MAS() is not None:
            resultado = izquierdo + derecho
        else:
            resultado = izquierdo - derecho
        return self.evaluar_exprP(ctx.exprP(), resultado)

    # term : factor termP
    def visitTerm(self, ctx):
        izquierdo = self.visit(ctx.factor())
        return self.evaluar_termP(ctx.termP(), izquierdo)

    # termP : POR factor termP | DIV factor termP | MOD factor termP | PORCENTAJE factor termP | ε
    def evaluar_termP(self, ctx, izquierdo):
        if ctx.factor() is None:
            return izquierdo
        derecho = self.visit(ctx.factor())

        if ctx.POR() is not None:
            resultado = izquierdo * derecho
        elif ctx.DIV() is not None:
            if derecho == 0:
                raise ErrorSemantico("división entre cero", ctx.DIV().getSymbol())
            resultado = izquierdo / derecho
        else:
            operador = ctx.MOD() if ctx.MOD() is not None else ctx.PORCENTAJE()
            if derecho == 0:
                raise ErrorSemantico("módulo entre cero", operador.getSymbol())
            resultado = izquierdo % derecho
        return self.evaluar_termP(ctx.termP(), resultado)

    # factor : MENOS factor | primario
    def visitFactor(self, ctx):
        if ctx.MENOS() is not None:
            return -self.visit(ctx.factor())
        return self.visit(ctx.primario())

    # primario : NUM | ID | ( expr ) | BARRA expr BARRA | func ( expr )
    def visitPrimario(self, ctx):
        if ctx.NUM() is not None:
            return float(ctx.NUM().getText())

        if ctx.ID() is not None:
            nombre = ctx.ID().getText()
            if nombre not in self.tabla_simbolos:
                raise ErrorSemantico(
                    f"la variable '{nombre}' no ha sido declarada",
                    ctx.ID().getSymbol())
            return self.tabla_simbolos[nombre]

        if ctx.BARRA(0) is not None:
            return abs(self.visit(ctx.expr()))

        if ctx.func() is not None:
            return self.evaluar_funcion(ctx.func(), self.visit(ctx.expr()))

        return self.visit(ctx.expr())

    # func : SIN | COS | TAN | ABS
    def evaluar_funcion(self, ctx_func, argumento):
        if ctx_func.SIN() is not None:
            return math.sin(argumento)
        if ctx_func.COS() is not None:
            return math.cos(argumento)
        if ctx_func.ABS() is not None:
            return abs(argumento)
        if abs(math.cos(argumento)) < 1e-12:
            raise ErrorSemantico(
                f"tan no está definida para {formato(argumento)}",
                ctx_func.TAN().getSymbol())
        return math.tan(argumento)


def formato(valor):
    if abs(valor - round(valor)) < 1e-12:
        return str(int(round(valor)))
    return f"{valor:.6f}".rstrip("0").rstrip(".")
