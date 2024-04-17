using System;

namespace s1_prog_lw_03_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите шаг = ");
            double dx = double.Parse(Console.ReadLine());
            Console.WriteLine("|    x   |   y    |");
            for (double x = -9, y = 0; x <= 5; x += dx)
            {
                if (x < -5) y = 2 - Math.Sqrt(4 - Math.Pow(x + 7, 2));
                if ((x >= -5) && (x <= -4)) y = 2;
                if ((x > -4) && (x <= 0)) y = -x / 2;
                if ((x > 0) && (x < Math.PI)) y = Math.Sin(x);
                if (x >= Math.PI) y = x - Math.PI;
                if (x < 0) Console.WriteLine($"|{x:F4} | {y:F4} |"); else Console.WriteLine($"| {x:F4} | {y:F4} |");
            }
        }
    }
}
