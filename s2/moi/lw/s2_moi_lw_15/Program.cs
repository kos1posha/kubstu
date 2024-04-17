using System;

namespace s2_moi_lw_15
{
    class Program
    {
        static void Main(string[] args)
        {
            int m = Convert.ToInt32(Console.ReadLine()), n = Convert.ToInt32(Console.ReadLine()), d;
            while (true)
            {
                if (m > n) m %= n;
                else n %= m;
                if ((m == 0) || (n == 0))
                {
                    d = Math.Max(n, m);
                    break;
                }
            }
            Console.WriteLine(d);
        }
    }
}
