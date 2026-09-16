# Generated from Expr11.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,42,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,5,4,26,8,4,10,4,12,
        4,29,9,4,1,5,4,5,32,8,5,11,5,12,5,33,1,6,4,6,37,8,6,11,6,12,6,38,
        1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,4,3,0,65,90,95,95,
        97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,
        32,44,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,
        0,7,21,1,0,0,0,9,23,1,0,0,0,11,31,1,0,0,0,13,36,1,0,0,0,15,16,5,
        43,0,0,16,2,1,0,0,0,17,18,5,42,0,0,18,4,1,0,0,0,19,20,5,40,0,0,20,
        6,1,0,0,0,21,22,5,41,0,0,22,8,1,0,0,0,23,27,7,0,0,0,24,26,7,1,0,
        0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,10,
        1,0,0,0,29,27,1,0,0,0,30,32,7,2,0,0,31,30,1,0,0,0,32,33,1,0,0,0,
        33,31,1,0,0,0,33,34,1,0,0,0,34,12,1,0,0,0,35,37,7,3,0,0,36,35,1,
        0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,40,1,0,0,0,40,
        41,6,6,0,0,41,14,1,0,0,0,4,0,27,33,38,1,6,0,0
    ]

class Expr11Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    ID = 5
    NUM = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "NUM", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "ID", "NUM", "WS" ]

    grammarFileName = "Expr11.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


