# Generated from gramatica/PrecInv.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecInvParser import PrecInvParser
else:
    from PrecInvParser import PrecInvParser

# This class defines a complete generic visitor for a parse tree produced by PrecInvParser.

class PrecInvVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrecInvParser#prog.
    def visitProg(self, ctx:PrecInvParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#A_T.
    def visitA_T(self, ctx:PrecInvParser.A_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#MultDiv.
    def visitMultDiv(self, ctx:PrecInvParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#A_F.
    def visitA_F(self, ctx:PrecInvParser.A_FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#SumaResta.
    def visitSumaResta(self, ctx:PrecInvParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#Num.
    def visitNum(self, ctx:PrecInvParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecInvParser#Parens.
    def visitParens(self, ctx:PrecInvParser.ParensContext):
        return self.visitChildren(ctx)



del PrecInvParser