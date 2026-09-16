# Generated from ExprAmb.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprAmbParser import ExprAmbParser
else:
    from ExprAmbParser import ExprAmbParser

# This class defines a complete listener for a parse tree produced by ExprAmbParser.
class ExprAmbListener(ParseTreeListener):

    # Enter a parse tree produced by ExprAmbParser#prog.
    def enterProg(self, ctx:ExprAmbParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprAmbParser#prog.
    def exitProg(self, ctx:ExprAmbParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprAmbParser#Suma.
    def enterSuma(self, ctx:ExprAmbParser.SumaContext):
        pass

    # Exit a parse tree produced by ExprAmbParser#Suma.
    def exitSuma(self, ctx:ExprAmbParser.SumaContext):
        pass


    # Enter a parse tree produced by ExprAmbParser#Mult.
    def enterMult(self, ctx:ExprAmbParser.MultContext):
        pass

    # Exit a parse tree produced by ExprAmbParser#Mult.
    def exitMult(self, ctx:ExprAmbParser.MultContext):
        pass


    # Enter a parse tree produced by ExprAmbParser#Num.
    def enterNum(self, ctx:ExprAmbParser.NumContext):
        pass

    # Exit a parse tree produced by ExprAmbParser#Num.
    def exitNum(self, ctx:ExprAmbParser.NumContext):
        pass



del ExprAmbParser