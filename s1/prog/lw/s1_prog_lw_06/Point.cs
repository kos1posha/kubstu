namespace s1_prog_lw_06
{
    class Point
    {
        public double X, Y;   // Координаты точки
        public Point() { X = 0; Y = 0; } // Конструктор нулевой точки
        public Point(double x, double y) { X = x; Y = y; } // Конструктор точки
        public static string Show(Point point) => $"({point.X}; {point.Y})";   // Ввывод координат точки
    }
}