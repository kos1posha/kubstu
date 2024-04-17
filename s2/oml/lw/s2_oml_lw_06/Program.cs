using System;

namespace s2_oml_lw_06
{
    class Program
    {
        static bool ToBool(string a)
        {
            switch (a)
            {
                case "0": return false;
                case "1": return true;
                default: return Convert.ToBoolean(a);
            }
        }
        static byte ToBit(bool a)
        {
            if (a == true) return 1;
            else return 0;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("На вход сумматора подаются разряды слагаемых a2, a1, b2, b1" +
                              "На экран выводятся разряды суммы c2, c1 и выходной перенос p3");
            Console.Write("a2 = ");
            bool a2 = ToBool(Console.ReadLine());
            Console.Write("a1 = ");
            bool a1 = ToBool(Console.ReadLine());
            Console.Write("b2 = ");
            bool b2 = ToBool(Console.ReadLine());
            Console.Write("b1 = ");
            bool b1 = ToBool(Console.ReadLine());
            bool c1 = a1 ^ b1;
            bool p2 = a1 & b1;
            bool c2 = p2 ^ a2 ^ b2;
            //bool p3 = (a2 & b2) | (p2 & a2) | (p2 & b2);
            bool p3 = (a2 & b2) ^ (p2 & a2) ^ (p2 & b2);
            Console.Clear();
            Console.Write($"a2 = {ToBit(a2)}\ta1 = {ToBit(a1)}\tb2 = {ToBit(b2)}\tb1 = {ToBit(b1)}\n" +
                          $"p3 = {ToBit(p3)}\tc2 = {ToBit(c2)}\tc1 = {ToBit(c1)}\n" +
                          $"{ToBit(a2)}{ToBit(a1)} + {ToBit(b2)}{ToBit(b1)} = {ToBit(p3)}{ToBit(c2)}{ToBit(c1)}");
        }
    }
}
