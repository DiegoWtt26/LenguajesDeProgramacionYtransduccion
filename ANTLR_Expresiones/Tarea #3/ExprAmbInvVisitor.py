# Generated from ExprAmbInv.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprAmbInvParser import ExprAmbInvParser
else:
    from ExprAmbInvParser import ExprAmbInvParser

# This class defines a complete generic visitor for a parse tree produced by ExprAmbInvParser.

class ExprAmbInvVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprAmbInvParser#prog.
    def visitProg(self, ctx:ExprAmbInvParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbInvParser#Suma.
    def visitSuma(self, ctx:ExprAmbInvParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbInvParser#Mult.
    def visitMult(self, ctx:ExprAmbInvParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprAmbInvParser#Num.
    def visitNum(self, ctx:ExprAmbInvParser.NumContext):
        return self.visitChildren(ctx)



del ExprAmbInvParser