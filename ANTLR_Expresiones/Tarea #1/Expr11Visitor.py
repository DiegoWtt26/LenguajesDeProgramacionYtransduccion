# Generated from Expr11.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expr11Parser import Expr11Parser
else:
    from Expr11Parser import Expr11Parser

# This class defines a complete generic visitor for a parse tree produced by Expr11Parser.

class Expr11Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr11Parser#prog.
    def visitProg(self, ctx:Expr11Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Suma.
    def visitSuma(self, ctx:Expr11Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#A_T.
    def visitA_T(self, ctx:Expr11Parser.A_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Mult.
    def visitMult(self, ctx:Expr11Parser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#A_F.
    def visitA_F(self, ctx:Expr11Parser.A_FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Id.
    def visitId(self, ctx:Expr11Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Num.
    def visitNum(self, ctx:Expr11Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr11Parser#Parens.
    def visitParens(self, ctx:Expr11Parser.ParensContext):
        return self.visitChildren(ctx)



del Expr11Parser