using System;

namespace s1_prog_lw_02_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("X = ");
            double x = double.Parse(Console.ReadLine()), y = 0;
            if ((x < -9) || (x > 5))
                Console.WriteLine("Y не определен при данном X");
            else
            {
                if (x < -5) y = 2 - Math.Sqrt(4 - Math.Pow(x + 7, 2));
                if ((x >= -5) && (x <= -4)) y = 2;
                if ((x > -4) && (x <= 0)) y = -x / 2;
                if ((x > 0) && (x < Math.PI)) y = Math.Sin(x);
                if (x >= Math.PI) y = x - Math.PI;
                Console.WriteLine($"Y = {y}");
            }
        }
    }
}
