# Generated from gramatica/PrecRight.g4 by ANTLR 4.13.2
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
        4,1,8,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,3,1,17,8,1,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,3,1,3,1,3,1,
        3,1,3,3,3,31,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,1,2,1,0,3,4,31,0,8,1,
        0,0,0,2,16,1,0,0,0,4,23,1,0,0,0,6,30,1,0,0,0,8,9,3,2,1,0,9,10,5,
        0,0,1,10,1,1,0,0,0,11,12,3,4,2,0,12,13,7,0,0,0,13,14,3,2,1,0,14,
        17,1,0,0,0,15,17,3,4,2,0,16,11,1,0,0,0,16,15,1,0,0,0,17,3,1,0,0,
        0,18,19,3,6,3,0,19,20,7,1,0,0,20,21,3,4,2,0,21,24,1,0,0,0,22,24,
        3,6,3,0,23,18,1,0,0,0,23,22,1,0,0,0,24,5,1,0,0,0,25,31,5,7,0,0,26,
        27,5,5,0,0,27,28,3,2,1,0,28,29,5,6,0,0,29,31,1,0,0,0,30,25,1,0,0,
        0,30,26,1,0,0,0,31,7,1,0,0,0,3,16,23,30
    ]

class PrecRightParser ( Parser ):

    grammarFileName = "PrecRight.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_prog = 0
    RULE_e = 1
    RULE_t = 2
    RULE_f = 3

    ruleNames =  [ "prog", "e", "t", "f" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUM=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e(self):
            return self.getTypedRuleContext(PrecRightParser.EContext,0)


        def EOF(self):
            return self.getToken(PrecRightParser.EOF, 0)

        def getRuleIndex(self):
            return PrecRightParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PrecRightParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.e()
            self.state = 9
            self.match(PrecRightParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrecRightParser.RULE_e

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class A_TContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(PrecRightParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_T" ):
                listener.enterA_T(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_T" ):
                listener.exitA_T(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_T" ):
                return visitor.visitA_T(self)
            else:
                return visitor.visitChildren(self)


    class SumaRestaContext(EContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.EContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def t(self):
            return self.getTypedRuleContext(PrecRightParser.TContext,0)

        def e(self):
            return self.getTypedRuleContext(PrecRightParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSumaResta" ):
                listener.enterSumaResta(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSumaResta" ):
                listener.exitSumaResta(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumaResta" ):
                return visitor.visitSumaResta(self)
            else:
                return visitor.visitChildren(self)



    def e(self):

        localctx = PrecRightParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_e)
        self._la = 0 # Token type
        try:
            self.state = 16
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = PrecRightParser.SumaRestaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.t()
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.e()
                pass

            elif la_ == 2:
                localctx = PrecRightParser.A_TContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.t()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrecRightParser.RULE_t

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class A_FContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def f(self):
            return self.getTypedRuleContext(PrecRightParser.FContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_F" ):
                listener.enterA_F(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_F" ):
                listener.exitA_F(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA_F" ):
                return visitor.visitA_F(self)
            else:
                return visitor.visitChildren(self)


    class MultDivContext(TContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.TContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def f(self):
            return self.getTypedRuleContext(PrecRightParser.FContext,0)

        def t(self):
            return self.getTypedRuleContext(PrecRightParser.TContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultDiv" ):
                return visitor.visitMultDiv(self)
            else:
                return visitor.visitChildren(self)



    def t(self):

        localctx = PrecRightParser.TContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_t)
        self._la = 0 # Token type
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = PrecRightParser.MultDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.f()
                self.state = 19
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.t()
                pass

            elif la_ == 2:
                localctx = PrecRightParser.A_FContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.f()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PrecRightParser.RULE_f

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParensContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def e(self):
            return self.getTypedRuleContext(PrecRightParser.EContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(FContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PrecRightParser.FContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(PrecRightParser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)



    def f(self):

        localctx = PrecRightParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_f)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = PrecRightParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(PrecRightParser.NUM)
                pass
            elif token in [5]:
                localctx = PrecRightParser.ParensContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(PrecRightParser.T__4)
                self.state = 27
                self.e()
                self.state = 28
                self.match(PrecRightParser.T__5)
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





