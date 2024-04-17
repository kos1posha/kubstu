using System;

namespace s2_oml_lw_01_04
{
    class Program
    {
        static void Main(string[] args)
        {
            bool a = Convert.ToBoolean(Console.ReadLine());
            bool b = Convert.ToBoolean(Console.ReadLine());
            bool c = Convert.ToBoolean(Console.ReadLine());
            Console.WriteLine($"a = {a}\tb = {b}\tc = {c}\n!(a | b & c) | !b | !c = {!(a | b & c) | !b | !c}");
        }
    }
}
