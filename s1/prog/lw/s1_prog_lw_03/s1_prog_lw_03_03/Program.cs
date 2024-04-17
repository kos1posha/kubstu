using System;

namespace s1_prog_lw_03_03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("x = ");
            double x = double.Parse(Console.ReadLine()),
                   E = 1,
                   n = 0,
                   exp = 0,
                   fact = 1;
            for (; Math.Abs(E) > 0.0000000001; n++)
            {
                if (n != 0) fact *= n;
                E = Math.Pow(x, n) / fact;
                exp += E;
            }
            Console.WriteLine(Math.Exp(x));
            Console.WriteLine("Exp = " + exp);
        }
    }
}
