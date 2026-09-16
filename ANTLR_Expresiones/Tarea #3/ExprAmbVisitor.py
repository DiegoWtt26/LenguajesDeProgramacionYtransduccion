# Generated from ExprAmb.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprAmbParser import ExprAmbParser
else:
    from ExprAmbParser import ExprAmbParser

# This class defines a complete generic visitor for a parse tree produced by ExprAmbParser.

class ExprAmbVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprAmbParser#prog.
    def visitProg(self, ctx:ExprAmbParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbParser#Suma.
    def visitSuma(self, ctx:ExprAmbParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbParser#Mult.
    def visitMult(self, ctx:ExprAmbParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbParser#Num.
    def visitNum(self, ctx:ExprAmbParser.NumContext):
        return self.visitChildren(ctx)



del ExprAmbParser