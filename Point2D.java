package OOП;
//dry -- don't repeat yourself == не повторяйся

/**
 * Point2D
 */
public class Point2D {
    int x, y;
    
    // ctor
    public Point2D(int valueX, int valueY) {
        x = valueX;
        y = valueY;
    }

    // // перегрузка метода Point2D 1
    // public Point2D() {
    //     x = 0;
    //     y = 0;
    // }

    // // перегрузка метода Point2D 2
    // public Point2D(int value) {
    //     x = value;
    //     y = value;
    // }

    // из-за dry
    public Point2D(int value) {
        this(value, value);
    }
    
    public Point2D() {
        this(0);
    }

    public String getInfo() {
        return String.format("x: %d; y: %d;", x, y);
    }

    //переопределение методов
    @Override
    public String toString() {
        return getInfo();
    }
}