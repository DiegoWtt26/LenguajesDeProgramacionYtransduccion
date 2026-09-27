# Generated from Calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraParser import CalculadoraParser
else:
    from CalculadoraParser import CalculadoraParser

# This class defines a complete generic visitor for a parse tree produced by CalculadoraParser.

class CalculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculadoraParser#inicio.
    def visitInicio(self, ctx:CalculadoraParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#programa.
    def visitPrograma(self, ctx:CalculadoraParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#sentencia.
    def visitSentencia(self, ctx:CalculadoraParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#expr.
    def visitExpr(self, ctx:CalculadoraParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#exprP.
    def visitExprP(self, ctx:CalculadoraParser.ExprPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#term.
    def visitTerm(self, ctx:CalculadoraParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#termP.
    def visitTermP(self, ctx:CalculadoraParser.TermPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#factor.
    def visitFactor(self, ctx:CalculadoraParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#primario.
    def visitPrimario(self, ctx:CalculadoraParser.PrimarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculadoraParser#func.
    def visitFunc(self, ctx:CalculadoraParser.FuncContext):
        return self.visitChildren(ctx)



del CalculadoraParser