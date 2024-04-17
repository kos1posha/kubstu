using System;
using System.Collections.Generic;

namespace s2_asd_lw_02_03
{
    class Program
    {
        static void Main(string[] args)
        {
            double[] array = new double[15];
            List<double> list = new List<double>();
            for (int i = 0; i < array.Length; i++)
            {
                Random rand = new Random();
                array[i] = rand.Next(10) + Math.Round(rand.NextDouble(), 3);
                Console.Write($"{array[i]} ");
            }
            Console.WriteLine();
            for (int i = 0; i < array.Length; i++)
            {
                list.Add(array[i]);
                Console.Write($"{list[i]} ");
            }
        }
    }
}
