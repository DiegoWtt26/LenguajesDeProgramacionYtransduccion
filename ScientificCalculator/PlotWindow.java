import javax.swing.*;
import java.awt.*;
import java.text.DecimalFormat;
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

    private static final DecimalFormat FORMATO = new DecimalFormat("#.##");
    private static final int MARGEN = 40;

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
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

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

        int width = getWidth() - 2 * MARGEN;
        int height = getHeight() - 2 * MARGEN;

        int divisiones = 10;
        g2.setColor(new Color(220, 220, 220));

        for (int i = 0; i <= divisiones; i++) {
            double xVal = xmin + i * (xmax - xmin) / divisiones;
            int px = MARGEN + (int) ((xVal - xmin) / (xmax - xmin) * width);
            g2.drawLine(px, MARGEN, px, MARGEN + height);

            double yVal = yminUsado + i * (ymaxUsado - yminUsado) / divisiones;
            int py = MARGEN + height - (int) ((yVal - yminUsado) / (ymaxUsado - yminUsado) * height);
            g2.drawLine(MARGEN, py, MARGEN + width, py);
        }

        g2.setColor(Color.DARK_GRAY);
        for (int i = 0; i <= divisiones; i++) {
            double xVal = xmin + i * (xmax - xmin) / divisiones;
            int px = MARGEN + (int) ((xVal - xmin) / (xmax - xmin) * width);
            g2.drawString(FORMATO.format(xVal), px - 10, MARGEN + height + 15);

            double yVal = yminUsado + i * (ymaxUsado - yminUsado) / divisiones;
            int py = MARGEN + height - (int) ((yVal - yminUsado) / (ymaxUsado - yminUsado) * height);
            g2.drawString(FORMATO.format(yVal), 5, py + 5);
        }

        g2.setColor(Color.BLACK);
        if (xmin <= 0 && xmax >= 0) {
            int px0 = MARGEN + (int) ((0 - xmin) / (xmax - xmin) * width);
            g2.drawLine(px0, MARGEN, px0, MARGEN + height);
        }
        if (yminUsado <= 0 && ymaxUsado >= 0) {
            int py0 = MARGEN + height - (int) ((0 - yminUsado) / (ymaxUsado - yminUsado) * height);
            g2.drawLine(MARGEN, py0, MARGEN + width, py0);
        }

        g2.drawRect(MARGEN, MARGEN, width, height);

        for (int s = 0; s < seriesXs.size(); s++) {
            List<Double> xs = seriesXs.get(s);
            List<Double> ys = seriesYs.get(s);

            if (xs.size() < 2) continue;

            g2.setColor(COLORES[s % COLORES.length]);
            g2.setStroke(new BasicStroke(2));

            for (int i = 1; i < xs.size(); i++) {

                double x1 = xs.get(i - 1);
                double y1 = ys.get(i - 1);

                double x2 = xs.get(i);
                double y2 = ys.get(i);

                int px1 = MARGEN + (int) ((x1 - xmin) / (xmax - xmin) * width);
                int py1 = MARGEN + height - (int) ((y1 - yminUsado) / (ymaxUsado - yminUsado) * height);

                int px2 = MARGEN + (int) ((x2 - xmin) / (xmax - xmin) * width);
                int py2 = MARGEN + height - (int) ((y2 - yminUsado) / (ymaxUsado - yminUsado) * height);

                g2.drawLine(px1, py1, px2, py2);
            }
        }
    }
}
