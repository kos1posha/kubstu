using System;

namespace s2_moi_lw_14_04
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = Convert.ToInt32(Console.ReadLine());
            BigInteger ans = 1;
            while (x > 0)
                ans *= x--;
            Console.WriteLine(ans);
        }
    }
}
