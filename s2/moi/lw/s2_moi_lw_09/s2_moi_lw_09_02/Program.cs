ausing System;

namespace s2_moi_lw_09_02
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = Convert.ToInt32(Console.ReadLine());
            int z = x >> 4;
            int p = x & 15;
            Console.WriteLine($"{z} | {p}");
        }
    }
}
