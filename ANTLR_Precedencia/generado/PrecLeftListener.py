# Generated from gramatica/PrecLeft.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PrecLeftParser import PrecLeftParser
else:
    from PrecLeftParser import PrecLeftParser

# This class defines a complete listener for a parse tree produced by PrecLeftParser.
class PrecLeftListener(ParseTreeListener):

    # Enter a parse tree produced by PrecLeftParser#prog.
    def enterProg(self, ctx:PrecLeftParser.ProgContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#prog.
    def exitProg(self, ctx:PrecLeftParser.ProgContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#A_T.
    def enterA_T(self, ctx:PrecLeftParser.A_TContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#A_T.
    def exitA_T(self, ctx:PrecLeftParser.A_TContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#SumaResta.
    def enterSumaResta(self, ctx:PrecLeftParser.SumaRestaContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#SumaResta.
    def exitSumaResta(self, ctx:PrecLeftParser.SumaRestaContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#A_F.
    def enterA_F(self, ctx:PrecLeftParser.A_FContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#A_F.
    def exitA_F(self, ctx:PrecLeftParser.A_FContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#MultDiv.
    def enterMultDiv(self, ctx:PrecLeftParser.MultDivContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#MultDiv.
    def exitMultDiv(self, ctx:PrecLeftParser.MultDivContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#Num.
    def enterNum(self, ctx:PrecLeftParser.NumContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#Num.
    def exitNum(self, ctx:PrecLeftParser.NumContext):
        pass


    # Enter a parse tree produced by PrecLeftParser#Parens.
    def enterParens(self, ctx:PrecLeftParser.ParensContext):
        pass

    # Exit a parse tree produced by PrecLeftParser#Parens.
    def exitParens(self, ctx:PrecLeftParser.ParensContext):
        pass



del PrecLeftParser