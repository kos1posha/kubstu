using System;
using System.IO;

namespace s1_prog_lw_08
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                StreamReader input = new StreamReader("input.txt");
                Console.WriteLine();
                double alfa = Convert.ToDouble(input.ReadLine()) * Math.PI / 180;
                //double alfa = 90 * Math.PI / 180;
                double z1 = ((Math.Sin(alfa) + Math.Sin(5 * alfa) - Math.Sin(3 * alfa)) / (Math.Cos(2 * alfa) + 1 - Math.Pow(Math.Sin(alfa), 2)));
                double z2 = 2 * Math.Cos(2 * alfa);
                StreamWriter output = new StreamWriter("output.txt");
                output.WriteLine($"z1 = {z1}\nz2 = {z2}");
                output.Close();
                //Console.WriteLine($"z1 = {z1} \nz2 = {z2}");
            }
            catch (Exception exception)
            {
                Console.WriteLine($"Ошибка: {exception}");
            }
        }
    }
}
