import javax.swing.*;
import java.awt.*;
import java.util.List;

public class PlotWindow extends JPanel {

    private List<List<Double>> seriesXs;
    private List<List<Double>> seriesYs;
    private boolean rangoFijo;
    private double ymin;
    private double ymax;

    private static final Color[] COLORES = {
        Color.BLUE, Color.RED, Color.GREEN, Color.ORANGE, Color.MAGENTA
    };

    public PlotWindow(List<List<Double>> seriesXs, List<List<Double>> seriesYs) {
        this.seriesXs = seriesXs;
        this.seriesYs = seriesYs;
        this.rangoFijo = false;
        abrirVentana();
    }

    public PlotWindow(List<List<Double>> seriesXs, List<List<Double>> seriesYs, double ymin, double ymax) {
        this.seriesXs = seriesXs;
        this.seriesYs = seriesYs;
        this.rangoFijo = true;
        this.ymin = ymin;
        this.ymax = ymax;
        abrirVentana();
    }

    private void abrirVentana() {
        JFrame frame = new JFrame("Scientific Calculator");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setSize(800, 600);
        frame.add(this);
        frame.setVisible(true);
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        Graphics2D g2 = (Graphics2D) g;

        double xmin = Double.POSITIVE_INFINITY;
        double xmax = Double.NEGATIVE_INFINITY;
        double yminCalc = Double.POSITIVE_INFINITY;
        double ymaxCalc = Double.NEGATIVE_INFINITY;

        for (int s = 0; s < seriesXs.size(); s++) {
            for (double x : seriesXs.get(s)) {
                if (x < xmin) xmin = x;
                if (x > xmax) xmax = x;
            }
            for (double y : seriesYs.get(s)) {
                if (y < yminCalc) yminCalc = y;
                if (y > ymaxCalc) ymaxCalc = y;
            }
        }

        double yminUsado = rangoFijo ? ymin : yminCalc;
        double ymaxUsado = rangoFijo ? ymax : ymaxCalc;

        for (int s = 0; s < seriesXs.size(); s++) {
            List<Double> xs = seriesXs.get(s);
            List<Double> ys = seriesYs.get(s);

            if (xs.size() < 2) continue;

            g2.setColor(COLORES[s % COLORES.length]);

            for (int i = 1; i < xs.size(); i++) {

                double x1 = xs.get(i - 1);
                double y1 = ys.get(i - 1);

                double x2 = xs.get(i);
                double y2 = ys.get(i);

                int px1 = (int) ((x1 - xmin) / (xmax - xmin) * getWidth());
                int py1 = getHeight() - (int) ((y1 - yminUsado) / (ymaxUsado - yminUsado) * getHeight());

                int px2 = (int) ((x2 - xmin) / (xmax - xmin) * getWidth());
                int py2 = getHeight() - (int) ((y2 - yminUsado) / (ymaxUsado - yminUsado) * getHeight());

                g2.drawLine(px1, py1, px2, py2);
            }
        }
    }
}
