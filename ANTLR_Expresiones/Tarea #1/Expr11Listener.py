# Generated from Expr11.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .Expr11Parser import Expr11Parser
else:
    from Expr11Parser import Expr11Parser

# This class defines a complete listener for a parse tree produced by Expr11Parser.
class Expr11Listener(ParseTreeListener):

    # Enter a parse tree produced by Expr11Parser#prog.
    def enterProg(self, ctx:Expr11Parser.ProgContext):
        pass

    # Exit a parse tree produced by Expr11Parser#prog.
    def exitProg(self, ctx:Expr11Parser.ProgContext):
        pass


    # Enter a parse tree produced by Expr11Parser#Suma.
    def enterSuma(self, ctx:Expr11Parser.SumaContext):
        pass

    # Exit a parse tree produced by Expr11Parser#Suma.
    def exitSuma(self, ctx:Expr11Parser.SumaContext):
        pass


    # Enter a parse tree produced by Expr11Parser#A_T.
    def enterA_T(self, ctx:Expr11Parser.A_TContext):
        pass

    # Exit a parse tree produced by Expr11Parser#A_T.
    def exitA_T(self, ctx:Expr11Parser.A_TContext):
        pass


    # Enter a parse tree produced by Expr11Parser#Mult.
    def enterMult(self, ctx:Expr11Parser.MultContext):
        pass

    # Exit a parse tree produced by Expr11Parser#Mult.
    def exitMult(self, ctx:Expr11Parser.MultContext):
        pass


    # Enter a parse tree produced by Expr11Parser#A_F.
    def enterA_F(self, ctx:Expr11Parser.A_FContext):
        pass

    # Exit a parse tree produced by Expr11Parser#A_F.
    def exitA_F(self, ctx:Expr11Parser.A_FContext):
        pass


    # Enter a parse tree produced by Expr11Parser#Id.
    def enterId(self, ctx:Expr11Parser.IdContext):
        pass

    # Exit a parse tree produced by Expr11Parser#Id.
    def exitId(self, ctx:Expr11Parser.IdContext):
        pass


    # Enter a parse tree produced by Expr11Parser#Num.
    def enterNum(self, ctx:Expr11Parser.NumContext):
        pass

    # Exit a parse tree produced by Expr11Parser#Num.
    def exitNum(self, ctx:Expr11Parser.NumContext):
        pass


    # Enter a parse tree produced by Expr11Parser#Parens.
    def enterParens(self, ctx:Expr11Parser.ParensContext):
        pass

    # Exit a parse tree produced by Expr11Parser#Parens.
    def exitParens(self, ctx:Expr11Parser.ParensContext):
        pass



del Expr11Parser