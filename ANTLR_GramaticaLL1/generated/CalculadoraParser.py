# Generated from Calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,28,8,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,47,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,69,8,6,1,7,1,7,1,7,3,7,74,8,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        91,8,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,2,0,1,3,5,
        5,96,0,20,1,0,0,0,2,27,1,0,0,0,4,29,1,0,0,0,6,34,1,0,0,0,8,46,1,
        0,0,0,10,48,1,0,0,0,12,68,1,0,0,0,14,73,1,0,0,0,16,90,1,0,0,0,18,
        92,1,0,0,0,20,21,3,2,1,0,21,22,5,0,0,1,22,1,1,0,0,0,23,24,3,4,2,
        0,24,25,3,2,1,0,25,28,1,0,0,0,26,28,1,0,0,0,27,23,1,0,0,0,27,26,
        1,0,0,0,28,3,1,0,0,0,29,30,5,6,0,0,30,31,5,14,0,0,31,32,3,6,3,0,
        32,33,5,17,0,0,33,5,1,0,0,0,34,35,3,10,5,0,35,36,3,8,4,0,36,7,1,
        0,0,0,37,38,5,8,0,0,38,39,3,10,5,0,39,40,3,8,4,0,40,47,1,0,0,0,41,
        42,5,9,0,0,42,43,3,10,5,0,43,44,3,8,4,0,44,47,1,0,0,0,45,47,1,0,
        0,0,46,37,1,0,0,0,46,41,1,0,0,0,46,45,1,0,0,0,47,9,1,0,0,0,48,49,
        3,14,7,0,49,50,3,12,6,0,50,11,1,0,0,0,51,52,5,10,0,0,52,53,3,14,
        7,0,53,54,3,12,6,0,54,69,1,0,0,0,55,56,5,11,0,0,56,57,3,14,7,0,57,
        58,3,12,6,0,58,69,1,0,0,0,59,60,5,4,0,0,60,61,3,14,7,0,61,62,3,12,
        6,0,62,69,1,0,0,0,63,64,5,12,0,0,64,65,3,14,7,0,65,66,3,12,6,0,66,
        69,1,0,0,0,67,69,1,0,0,0,68,51,1,0,0,0,68,55,1,0,0,0,68,59,1,0,0,
        0,68,63,1,0,0,0,68,67,1,0,0,0,69,13,1,0,0,0,70,71,5,9,0,0,71,74,
        3,14,7,0,72,74,3,16,8,0,73,70,1,0,0,0,73,72,1,0,0,0,74,15,1,0,0,
        0,75,91,5,7,0,0,76,91,5,6,0,0,77,78,5,15,0,0,78,79,3,6,3,0,79,80,
        5,16,0,0,80,91,1,0,0,0,81,82,5,13,0,0,82,83,3,6,3,0,83,84,5,13,0,
        0,84,91,1,0,0,0,85,86,3,18,9,0,86,87,5,15,0,0,87,88,3,6,3,0,88,89,
        5,16,0,0,89,91,1,0,0,0,90,75,1,0,0,0,90,76,1,0,0,0,90,77,1,0,0,0,
        90,81,1,0,0,0,90,85,1,0,0,0,91,17,1,0,0,0,92,93,7,0,0,0,93,19,1,
        0,0,0,5,27,46,68,73,90
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'mod'", "'abs'", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'|'", "'='", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "SIN", "COS", "TAN", "MOD", "ABS", "ID", 
                      "NUM", "MAS", "MENOS", "POR", "DIV", "PORCENTAJE", 
                      "BARRA", "ASIGNAR", "PAR_IZQ", "PAR_DER", "PUNTOYCOMA", 
                      "COMENTARIO", "ESPACIOS" ]

    RULE_inicio = 0
    RULE_programa = 1
    RULE_sentencia = 2
    RULE_expr = 3
    RULE_exprP = 4
    RULE_term = 5
    RULE_termP = 6
    RULE_factor = 7
    RULE_primario = 8
    RULE_func = 9

    ruleNames =  [ "inicio", "programa", "sentencia", "expr", "exprP", "term", 
                   "termP", "factor", "primario", "func" ]

    EOF = Token.EOF
    SIN=1
    COS=2
    TAN=3
    MOD=4
    ABS=5
    ID=6
    NUM=7
    MAS=8
    MENOS=9
    POR=10
    DIV=11
    PORCENTAJE=12
    BARRA=13
    ASIGNAR=14
    PAR_IZQ=15
    PAR_DER=16
    PUNTOYCOMA=17
    COMENTARIO=18
    ESPACIOS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programa(self):
            return self.getTypedRuleContext(CalculadoraParser.ProgramaContext,0)


        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_inicio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInicio" ):
                return visitor.visitInicio(self)
            else:
                return visitor.visitChildren(self)




    def inicio(self):

        localctx = CalculadoraParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.programa()
            self.state = 21
            self.match(CalculadoraParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self):
            return self.getTypedRuleContext(CalculadoraParser.SentenciaContext,0)


        def programa(self):
            return self.getTypedRuleContext(CalculadoraParser.ProgramaContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = CalculadoraParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programa)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.sentencia()
                self.state = 24
                self.programa()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def ASIGNAR(self):
            return self.getToken(CalculadoraParser.ASIGNAR, 0)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(CalculadoraParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_sentencia

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = CalculadoraParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sentencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(CalculadoraParser.ID)
            self.state = 30
            self.match(CalculadoraParser.ASIGNAR)
            self.state = 31
            self.expr()
            self.state = 32
            self.match(CalculadoraParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(CalculadoraParser.TermContext,0)


        def exprP(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprPContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CalculadoraParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.term()
            self.state = 35
            self.exprP()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAS(self):
            return self.getToken(CalculadoraParser.MAS, 0)

        def term(self):
            return self.getTypedRuleContext(CalculadoraParser.TermContext,0)


        def exprP(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprPContext,0)


        def MENOS(self):
            return self.getToken(CalculadoraParser.MENOS, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_exprP

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprP" ):
                return visitor.visitExprP(self)
            else:
                return visitor.visitChildren(self)




    def exprP(self):

        localctx = CalculadoraParser.ExprPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exprP)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(CalculadoraParser.MAS)
                self.state = 38
                self.term()
                self.state = 39
                self.exprP()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(CalculadoraParser.MENOS)
                self.state = 42
                self.term()
                self.state = 43
                self.exprP()
                pass
            elif token in [13, 16, 17]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(CalculadoraParser.FactorContext,0)


        def termP(self):
            return self.getTypedRuleContext(CalculadoraParser.TermPContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CalculadoraParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.factor()
            self.state = 49
            self.termP()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermPContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POR(self):
            return self.getToken(CalculadoraParser.POR, 0)

        def factor(self):
            return self.getTypedRuleContext(CalculadoraParser.FactorContext,0)


        def termP(self):
            return self.getTypedRuleContext(CalculadoraParser.TermPContext,0)


        def DIV(self):
            return self.getToken(CalculadoraParser.DIV, 0)

        def MOD(self):
            return self.getToken(CalculadoraParser.MOD, 0)

        def PORCENTAJE(self):
            return self.getToken(CalculadoraParser.PORCENTAJE, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_termP

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermP" ):
                return visitor.visitTermP(self)
            else:
                return visitor.visitChildren(self)




    def termP(self):

        localctx = CalculadoraParser.TermPContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_termP)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(CalculadoraParser.POR)
                self.state = 52
                self.factor()
                self.state = 53
                self.termP()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(CalculadoraParser.DIV)
                self.state = 56
                self.factor()
                self.state = 57
                self.termP()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(CalculadoraParser.MOD)
                self.state = 60
                self.factor()
                self.state = 61
                self.termP()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.match(CalculadoraParser.PORCENTAJE)
                self.state = 64
                self.factor()
                self.state = 65
                self.termP()
                pass
            elif token in [8, 9, 13, 16, 17]:
                self.enterOuterAlt(localctx, 5)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENOS(self):
            return self.getToken(CalculadoraParser.MENOS, 0)

        def factor(self):
            return self.getTypedRuleContext(CalculadoraParser.FactorContext,0)


        def primario(self):
            return self.getTypedRuleContext(CalculadoraParser.PrimarioContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CalculadoraParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_factor)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(CalculadoraParser.MENOS)
                self.state = 71
                self.factor()
                pass
            elif token in [1, 2, 3, 5, 6, 7, 13, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.primario()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(CalculadoraParser.NUM, 0)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def PAR_IZQ(self):
            return self.getToken(CalculadoraParser.PAR_IZQ, 0)

        def expr(self):
            return self.getTypedRuleContext(CalculadoraParser.ExprContext,0)


        def PAR_DER(self):
            return self.getToken(CalculadoraParser.PAR_DER, 0)

        def BARRA(self, i:int=None):
            if i is None:
                return self.getTokens(CalculadoraParser.BARRA)
            else:
                return self.getToken(CalculadoraParser.BARRA, i)

        def func(self):
            return self.getTypedRuleContext(CalculadoraParser.FuncContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_primario

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimario" ):
                return visitor.visitPrimario(self)
            else:
                return visitor.visitChildren(self)




    def primario(self):

        localctx = CalculadoraParser.PrimarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primario)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(CalculadoraParser.NUM)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(CalculadoraParser.ID)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.match(CalculadoraParser.PAR_IZQ)
                self.state = 78
                self.expr()
                self.state = 79
                self.match(CalculadoraParser.PAR_DER)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.match(CalculadoraParser.BARRA)
                self.state = 82
                self.expr()
                self.state = 83
                self.match(CalculadoraParser.BARRA)
                pass
            elif token in [1, 2, 3, 5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 85
                self.func()
                self.state = 86
                self.match(CalculadoraParser.PAR_IZQ)
                self.state = 87
                self.expr()
                self.state = 88
                self.match(CalculadoraParser.PAR_DER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(CalculadoraParser.SIN, 0)

        def COS(self):
            return self.getToken(CalculadoraParser.COS, 0)

        def TAN(self):
            return self.getToken(CalculadoraParser.TAN, 0)

        def ABS(self):
            return self.getToken(CalculadoraParser.ABS, 0)

        def getRuleIndex(self):
            return CalculadoraParser.RULE_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = CalculadoraParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 46) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





