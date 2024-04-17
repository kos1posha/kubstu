using System;

namespace s2_oml_lw_01_03
{
    class Program
    {
        static void Main(string[] args)
        {
            bool a = Convert.ToBoolean(Console.ReadLine());
            bool b = Convert.ToBoolean(Console.ReadLine());
            bool c = Convert.ToBoolean(Console.ReadLine());
            Console.WriteLine($"a = {a}\tb = {b}\tc = {c}\n(!a & b & c) | (!(a & b) & c) | !(a & b) = {(!a & b & c) | (!(a & b) & c) | !(a & b)}");
        }
    }
}
