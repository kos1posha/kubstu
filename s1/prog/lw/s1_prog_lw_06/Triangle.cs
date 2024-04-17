using System;

namespace s1_prog_lw_06
{
    class Triangle
    {
        Point A { get; set; }
        Point B { get; set; }
        Point C { get; set; }   // Точки треугольника
        public Triangle(Point a, Point b, Point c) { A = a; B = b; C = c; }    // Конструктор треугольника
        public bool Correct()   // Проверка на корректность треугольника
        {
            if (A.X == B.X && B.X == C.X && A.X == C.X) { return false; }
            if (A.Y == B.Y && B.Y == C.Y && A.Y == C.Y) { return false; }
            return true;
        }
        public double Side(Point A, Point B) => Math.Sqrt(Math.Pow(B.X - A.X, 2) + Math.Pow(B.Y - A.Y, 2));   // Длина стороны по координатам точек
        public double Angle(Point A, Point B, Point C) => Math.Acos((Math.Pow(Side(A, B), 2) + Math.Pow(Side(B, C), 2) - Math.Pow(Side(A, C), 2)) / (2 * Side(A, B) * Side(B, C))) * 180 / Math.PI;   // Углы треугольника
        public double Perimeter => Side(A, B) + Side(B, C) + Side(A, C);   // Периметр
        public double Area => Math.Abs((B.X - A.X) * (C.Y - A.Y) - (C.X - A.X) * (B.Y - A.Y)) / 2;   // Площадь
        public Point Centroid => new Point((A.X + B.X + C.X) / 2, (A.Y + B.Y + C.Y) / 2);   // Точка пересечения медиан
        public void ShiftUp() { A.Y += 1; B.Y += 1; C.Y += 1; }
        public void ShiftUp(double shift) { A.Y += shift; B.Y += shift; C.Y += shift; }
        public void ShifDown() { A.Y -= 1; B.Y -= 1; C.Y -= 1; }
        public void ShiftDown(double shift) { A.Y -= shift; B.Y -= shift; C.Y -= shift; }
        public void ShiftRight() { A.X += 1; B.X += 1; C.X += 1; }
        public void ShiftRight(double shift) { A.X += shift; B.X += shift; C.X += shift; }
        public void ShiftLeft() { A.X -= 1; B.X -= 1; C.X -= 1; }
        public void ShiftLeft(double shift) { A.X -= shift; B.X -= shift; C.X -= shift; }
        public void MultipleIncrease(double increase)   // Увеличение или уменьшение треугольника в increase раз
        {
            A.X = ((A.X - Centroid.X) * increase) + Centroid.X;
            A.Y = ((A.Y - Centroid.Y) * increase) + Centroid.Y;
            B.X = ((B.X - Centroid.X) * increase) + Centroid.X;
            B.Y = ((B.Y - Centroid.Y) * increase) + Centroid.Y;
            C.X = ((C.X - Centroid.X) * increase) + Centroid.X;
            C.Y = ((C.Y - Centroid.Y) * increase) + Centroid.Y;
        }
        public void Tilt(double alfa)   // Поворот треугольника на угол alfa
        {
            var centroidX = Centroid.X;
            var centroidY = Centroid.Y;
            alfa *= Math.PI / 180;
            A.X = Convert.ToSingle((A.X - centroidX) * Math.Cos(alfa) + (A.Y - centroidY) * Math.Sin(alfa));
            A.Y = Convert.ToSingle(-(A.X - centroidX) * Math.Sin(alfa) + (A.Y - centroidY) * Math.Cos(alfa));
            B.X = Convert.ToSingle((B.X - centroidX) * Math.Cos(alfa) + (B.Y - centroidY) * Math.Sin(alfa));
            B.Y = Convert.ToSingle(-(B.X - centroidX) * Math.Sin(alfa) + (B.Y - centroidY) * Math.Cos(alfa));
            C.X = Convert.ToSingle((C.X - centroidX) * Math.Cos(alfa) + (C.Y - centroidY) * Math.Sin(alfa));
            C.Y = Convert.ToSingle(-(C.X - centroidX) * Math.Sin(alfa) + (C.Y - centroidY) * Math.Cos(alfa));
        }
    }
}