using System;

namespace s2_moi_lw_09_01
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = Convert.ToInt32(Console.ReadLine());
            int z = (x << 5) + (x << 3);
            Console.WriteLine(z);
        }
    }
}