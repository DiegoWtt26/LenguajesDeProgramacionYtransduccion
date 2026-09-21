# Generated from gramatica/PrecRight.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecRightParser import PrecRightParser
else:
    from PrecRightParser import PrecRightParser

# This class defines a complete generic visitor for a parse tree produced by PrecRightParser.

class PrecRightVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PrecRightParser#prog.
    def visitProg(self, ctx:PrecRightParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#SumaResta.
    def visitSumaResta(self, ctx:PrecRightParser.SumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#A_T.
    def visitA_T(self, ctx:PrecRightParser.A_TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#MultDiv.
    def visitMultDiv(self, ctx:PrecRightParser.MultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#A_F.
    def visitA_F(self, ctx:PrecRightParser.A_FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#Num.
    def visitNum(self, ctx:PrecRightParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PrecRightParser#Parens.
    def visitParens(self, ctx:PrecRightParser.ParensContext):
        return self.visitChildren(ctx)



del PrecRightParser