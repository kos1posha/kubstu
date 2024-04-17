using System;

namespace s2_oml_lw_01_01
{
    class Program
    {
        static void Main(string[] args)
        {
            bool x = Convert.ToBoolean(Console.ReadLine());
            bool y = Convert.ToBoolean(Console.ReadLine());
            Console.WriteLine($"x = {x}\ty = {y}\n(!x & y) | (x & !y) = {(!x & y) | (x & !y)}");
        }
    }
}
