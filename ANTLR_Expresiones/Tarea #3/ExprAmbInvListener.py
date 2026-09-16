# Generated from ExprAmbInv.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprAmbInvParser import ExprAmbInvParser
else:
    from ExprAmbInvParser import ExprAmbInvParser

# This class defines a complete listener for a parse tree produced by ExprAmbInvParser.
class ExprAmbInvListener(ParseTreeListener):

    # Enter a parse tree produced by ExprAmbInvParser#prog.
    def enterProg(self, ctx:ExprAmbInvParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprAmbInvParser#prog.
    def exitProg(self, ctx:ExprAmbInvParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprAmbInvParser#Suma.
    def enterSuma(self, ctx:ExprAmbInvParser.SumaContext):
        pass

    # Exit a parse tree produced by ExprAmbInvParser#Suma.
    def exitSuma(self, ctx:ExprAmbInvParser.SumaContext):
        pass


    # Enter a parse tree produced by ExprAmbInvParser#Mult.
    def enterMult(self, ctx:ExprAmbInvParser.MultContext):
        pass

    # Exit a parse tree produced by ExprAmbInvParser#Mult.
    def exitMult(self, ctx:ExprAmbInvParser.MultContext):
        pass


    # Enter a parse tree produced by ExprAmbInvParser#Num.
    def enterNum(self, ctx:ExprAmbInvParser.NumContext):
        pass

    # Exit a parse tree produced by ExprAmbInvParser#Num.
    def exitNum(self, ctx:ExprAmbInvParser.NumContext):
        pass



del ExprAmbInvParser