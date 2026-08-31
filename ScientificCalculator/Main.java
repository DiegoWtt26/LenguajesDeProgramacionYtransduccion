import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import org.antlr.v4.runtime.misc.ParseCancellationException;

public class Main {

    public static void main(String[] args) throws Exception {

        CharStream input = CharStreams.fromStream(System.in);

        ScientificCalcLexer lexer = new ScientificCalcLexer(input);
        lexer.removeErrorListeners();
        lexer.addErrorListener(new ErrorReporter());

        CommonTokenStream tokens = new CommonTokenStream(lexer);

        ScientificCalcParser parser = new ScientificCalcParser(tokens);
        parser.removeErrorListeners();
        parser.addErrorListener(new ErrorReporter());

        try {
            ParseTree tree = parser.prog();

            ScientificEvalVisitor visitor = new ScientificEvalVisitor();
            visitor.visit(tree);

        } catch (ParseCancellationException e) {
            System.err.println("Error de sintaxis: " + e.getMessage());
            System.err.println("Revisa la expresion escrita e intenta de nuevo.");
        } catch (Exception e) {
            System.err.println("Error inesperado: " + e.getMessage());
        }
    }
}

class ErrorReporter extends BaseErrorListener {
    @Override
    public void syntaxError(Recognizer<?, ?> recognizer,
                             Object offendingSymbol,
                             int line, int charPositionInLine,
                             String msg, RecognitionException e) {
        throw new ParseCancellationException(
            "linea " + line + ":" + charPositionInLine + " - " + msg
        );
    }
}
