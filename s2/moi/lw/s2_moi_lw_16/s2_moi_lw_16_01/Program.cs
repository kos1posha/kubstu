using System;

namespace s2_moi_lw_16_01
{
    class Program
    {
        static void Main(string[] args)
        {
            ulong x = Convert.ToUInt64(Console.ReadLine());
            bool primary = true;
            for (ulong i = 2; i <= Math.Sqrt(x); i += 1)
            {
                if (x % i == 0)
                {
                    primary = false;
                    break;
                }
            }
            Console.WriteLine(primary);
        }
    }
}
