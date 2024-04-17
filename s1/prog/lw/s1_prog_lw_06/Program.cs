using System;

namespace s1_prog_lw_06
{
    class Program
    {
        static void Main(string[] args)
        {
            Point A = new Point();
            Point B = new Point(-4, -2);
            Point C = new Point(-1, 4);
            Triangle ABC = new Triangle(A, B, C);

            //ABC.Tilt(90);
            ABC.ShiftDown(2);
            //ABC.MultipleIncrease(2);

            Console.WriteLine($"Координаты вершин: A{Point.Show(A)}   B{Point.Show(B)}   C{Point.Show(C)}");
            Console.WriteLine($"Центроид: {Point.Show(ABC.Centroid)}");
            Console.WriteLine($"Сторона AB = {ABC.Side(A, B):F2}   Сторона BC = {ABC.Side(B, C):F2}   Сторона AC = {ABC.Side(A, C):F2}");
            Console.WriteLine($"Периметр = {ABC.Perimeter:F2}");
            Console.WriteLine($"Площадь = {ABC.Area:F2}");
            Console.WriteLine($"Угол A = {ABC.Angle(B, A, C):F2}°   Угол B = {ABC.Angle(A, B, C):F2}°   Угол C = {ABC.Angle(A, C, B):F2}°");
        }
    }
}