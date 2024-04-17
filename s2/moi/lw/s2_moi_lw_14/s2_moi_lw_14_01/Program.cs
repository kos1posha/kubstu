using System;

namespace s2_moi_lw_14_01
{
    class Program
    {
        static void Main(string[] args)
        {
            uint x = Convert.ToUInt32(Console.ReadLine()) * 2;
            Console.WriteLine(Convert.ToString(x >> 1, 2));
            uint N1 = x, N2 = 0;
            for (int i = 1; i <= 31; i++)
            {
                N1 -= x >> 1;
                N2 += (x >>= 1) & 1;
            }
            Console.WriteLine($"N1 = {N1}\nN2 = {N2}");
        }
    }
}
