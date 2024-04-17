using System;

namespace s2_oml_lw_01_02
{
    class Program
    {
        static void Main(string[] args)
        {
            bool x = Convert.ToBoolean(Console.ReadLine());
            bool y = Convert.ToBoolean(Console.ReadLine());
            bool z = Convert.ToBoolean(Console.ReadLine());
            Console.WriteLine($"x = {x}\ty = {y}\tz = {z}\n!(!x | y | !z) + (y & z) = {!(!x | y | !z) | (y & z)}");
        }
    }
}
