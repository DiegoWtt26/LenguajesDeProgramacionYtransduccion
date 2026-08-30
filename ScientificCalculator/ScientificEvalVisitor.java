import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

public class ScientificEvalVisitor
        extends ScientificCalcBaseVisitor<Double> {

    Map<String, Double> memory = new HashMap<>();
    Map<String, String> funcParams = new HashMap<>();
    Map<String, ScientificCalcParser.ExprContext> funcBodies = new HashMap<>();

    @Override
    public Double visitNumber(ScientificCalcParser.NumberContext ctx) {
        return Double.parseDouble(ctx.NUMBER().getText());
    }

    @Override
    public Double visitAddSub(ScientificCalcParser.AddSubContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == ScientificCalcParser.ADD) {
            return left + right;
        }
        return left - right;
    }

    @Override
    public Double visitMulDiv(ScientificCalcParser.MulDivContext ctx) {
        double left = visit(ctx.expr(0));
        double right = visit(ctx.expr(1));
        if (ctx.op.getType() == ScientificCalcParser.MUL) {
            return left * right;
        }
        return left / right;
    }

    @Override
    public Double visitParens(ScientificCalcParser.ParensContext ctx) {
        return visit(ctx.expr());
    }

    @Override
    public Double visitPrintExpr(ScientificCalcParser.PrintExprContext ctx) {
        double value = visit(ctx.expr());
        System.out.println(value);
        return value;
    }

    @Override
    public Double visitAssign(ScientificCalcParser.AssignContext ctx) {
        String id = ctx.ID().getText();
        double value = visit(ctx.expr());
        memory.put(id, value);
        return value;
    }

    @Override
    public Double visitId(ScientificCalcParser.IdContext ctx) {
        String id = ctx.ID().getText();
        if (memory.containsKey(id)) {
            return memory.get(id);
        }
        System.err.println("Variable no definida: " + id);
        return 0.0;
    }

    @Override
    public Double visitPower(ScientificCalcParser.PowerContext ctx) {
        double base = visit(ctx.expr(0));
        double exponent = visit(ctx.expr(1));
        return Math.pow(base, exponent);
    }

    @Override
    public Double visitFunctionCall(ScientificCalcParser.FunctionCallContext ctx) {
        String function = ctx.function().getText();
        double value = visit(ctx.expr());

        switch (function) {
            case "sin": return Math.sin(value);
            case "cos": return Math.cos(value);
            case "tan": return Math.tan(value);
            case "sqrt": return Math.sqrt(value);
            case "log": return Math.log10(value);
            case "ln": return Math.log(value);
            case "abs": return Math.abs(value);
            case "exp": return Math.exp(value);
            case "asin":  return Math.asin(value);
            case "acos":  return Math.acos(value);
            case "atan":  return Math.atan(value);
            case "floor": return Math.floor(value);
            case "ceil":  return Math.ceil(value);
            default:
                throw new RuntimeException("Funcion desconocida: " + function);
        }
    }

    @Override
    public Double visitFunctionCall2(ScientificCalcParser.FunctionCall2Context ctx) {
        String function = ctx.function2().getText();
        double a = visit(ctx.expr(0));
        double b = visit(ctx.expr(1));

        switch (function) {
            case "pow": return Math.pow(a, b);
            case "max": return Math.max(a, b);
            case "min": return Math.min(a, b);
            default:
                throw new RuntimeException("Funcion desconocida: " + function);
        }
    }

    @Override
    public Double visitFuncDef(ScientificCalcParser.FuncDefContext ctx) {
        String nombreFuncion = ctx.ID(0).getText();
        String nombreParametro = ctx.ID(1).getText();

        funcParams.put(nombreFuncion, nombreParametro);
        funcBodies.put(nombreFuncion, ctx.expr());

        System.out.println("Funcion definida: " + nombreFuncion + "(" + nombreParametro + ")");
        return 0.0;
    }

    @Override
    public Double visitUserFunctionCall(ScientificCalcParser.UserFunctionCallContext ctx) {
        String nombreFuncion = ctx.ID().getText();

        if (!funcBodies.containsKey(nombreFuncion)) {
            System.err.println("Funcion no definida: " + nombreFuncion);
            return 0.0;
        }

        String nombreParametro = funcParams.get(nombreFuncion);
        ScientificCalcParser.ExprContext cuerpo = funcBodies.get(nombreFuncion);

        double valorArgumento = visit(ctx.expr());

        Double valorPrevio = memory.get(nombreParametro);
        memory.put(nombreParametro, valorArgumento);

        double resultado = visit(cuerpo);

        if (valorPrevio != null) {
            memory.put(nombreParametro, valorPrevio);
        } else {
            memory.remove(nombreParametro);
        }

        return resultado;
    }

    @Override
    public Double visitUnary(ScientificCalcParser.UnaryContext ctx) {
        double value = visit(ctx.expr());
        if (ctx.op.getText().equals("-")) {
            return -value;
        }
        return value;
    }

    @Override
    public Double visitConstantExpr(ScientificCalcParser.ConstantExprContext ctx) {
        String constant = ctx.constant().getText();
        if (constant.equals("pi")) {
            return Math.PI;
        }
        if (constant.equals("e")) {
            return Math.E;
        }
        return 0.0;
    }

    @Override
    public Double visitClear(ScientificCalcParser.ClearContext ctx) {
        memory.clear();
        System.out.println("Memoria eliminada.");
        return 0.0;
    }

    @Override
    public Double visitShowVars(ScientificCalcParser.ShowVarsContext ctx) {
        if (memory.isEmpty()) {
            System.out.println("No hay variables definidas.");
            return 0.0;
        }
        for (Map.Entry<String, Double> entry : memory.entrySet()) {
            System.out.println(entry.getKey() + " = " + entry.getValue());
        }
        return 0.0;
    }

    @Override
    public Double visitPlotExpr(ScientificCalcParser.PlotExprContext ctx) {
        double xmin = visit(ctx.xmin);
        double xmax = visit(ctx.xmax);

        int samples = 800;

        List<List<Double>> seriesXs = new ArrayList<>();
        List<List<Double>> seriesYs = new ArrayList<>();

        for (var funcExpr : ctx.funcs) {
            List<Double> xs = new ArrayList<>();
            List<Double> ys = new ArrayList<>();

            for (int i = 0; i < samples; i++) {
                double x = xmin + i * (xmax - xmin) / (samples - 1);
                memory.put("x", x);
                double y = visit(funcExpr);

                if (Double.isFinite(y)) {
                    xs.add(x);
                    ys.add(y);
                }
            }

            seriesXs.add(xs);
            seriesYs.add(ys);
        }

        if (ctx.ymin != null && ctx.ymax != null) {
            double ymin = visit(ctx.ymin);
            double ymax = visit(ctx.ymax);
            new PlotWindow(seriesXs, seriesYs, ymin, ymax);
        } else {
            new PlotWindow(seriesXs, seriesYs);
        }

        return 0.0;
    }
}
