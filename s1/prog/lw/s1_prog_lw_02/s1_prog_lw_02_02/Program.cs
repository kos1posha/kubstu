using System;

namespace s1_prog_lw_02_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("R = ");
            double R = double.Parse(Console.ReadLine());
            Console.Write("x = ");
            double x = Convert.ToDouble(Console.ReadLine());
            Console.Write("y = ");
            double y = Convert.ToDouble(Console.ReadLine());
            if (((x <= R) && (x >= -R)) && ((y <= R) && (y >= -R)))
            {
                if ((x == 0) || (y == 0)) Console.WriteLine("Попадание");
                if ((x > 0) && (y > 0)) Console.WriteLine("Попадание");
                if ((x < 0) && (y < 0)) Console.WriteLine("Попадание");
                if ((x > 0) && (y < 0))
                {
                    if ((Math.Pow(x - R, 2) + Math.Pow(y + R, 2)) >= Math.Pow(R, 2)) Console.WriteLine("Попадание");
                    else Console.WriteLine("Промах");
                }
                if ((x < 0) && (y > 0))
                {
                    if ((Math.Pow(x + R, 2) + Math.Pow(y - R, 2)) >= Math.Pow(R, 2)) Console.WriteLine("Попадание");
                    else Console.WriteLine("Промах");
                }
            }
            else Console.WriteLine("Промах");
        }
    }
}
