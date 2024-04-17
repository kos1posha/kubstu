using System;

namespace s1_prog_lw_01
{
    class Program
    {
        static void Main(string[] args)
        {
            double alfa = double.Parse(Console.ReadLine());
            double z1 = (Math.Sin(alfa) + Math.Sin(5 * alfa) - Math.Sin(3 * alfa)) / (Math.Cos(2 * alfa) + 1 - Math.Pow(Math.Sin(alfa), 2));
            double z2 = 2 * Math.Cos(2 * alfa);
            Console.WriteLine($"z1 = {z1} \nz2 = {z2} ");
        }
    }
}
