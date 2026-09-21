# Generated from gramatica/PrecLeft.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecLeftParser import PrecLeftParser
else:
    from PrecLeftParser import PrecLeftParser

# This class defines a complete generic visitor for a parse tree produced by PrecLeftParser.

class PrecLeftVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrecLeftParser#prog.
    def visitProg(self, ctx:PrecLeftParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#A_T.
    def visitA_T(self, ctx:PrecLeftParser.A_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#SumaResta.
    def visitSumaResta(self, ctx:PrecLeftParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#A_F.
    def visitA_F(self, ctx:PrecLeftParser.A_FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#MultDiv.
    def visitMultDiv(self, ctx:PrecLeftParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#Num.
    def visitNum(self, ctx:PrecLeftParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecLeftParser#Parens.
    def visitParens(self, ctx:PrecLeftParser.ParensContext):
        return self.visitChildren(ctx)



del PrecLeftParser