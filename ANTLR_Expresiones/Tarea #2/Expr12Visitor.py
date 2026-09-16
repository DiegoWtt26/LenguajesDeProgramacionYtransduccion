# Generated from Expr12.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expr12Parser import Expr12Parser
else:
    from Expr12Parser import Expr12Parser

# This class defines a complete generic visitor for a parse tree produced by Expr12Parser.

class Expr12Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by Expr12Parser#prog.
    def visitProg(self, ctx:Expr12Parser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Suma.
    def visitSuma(self, ctx:Expr12Parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#A_T.
    def visitA_T(self, ctx:Expr12Parser.A_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Mult.
    def visitMult(self, ctx:Expr12Parser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#A_F.
    def visitA_F(self, ctx:Expr12Parser.A_FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Id.
    def visitId(self, ctx:Expr12Parser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Num.
    def visitNum(self, ctx:Expr12Parser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Expr12Parser#Parens.
    def visitParens(self, ctx:Expr12Parser.ParensContext):
        return self.visitChildren(ctx)



del Expr12Parser