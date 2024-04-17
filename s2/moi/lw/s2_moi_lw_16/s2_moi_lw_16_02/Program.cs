using System;

namespace s2_moi_lw_16_02
{
    class Program
    {
        static void Main(string[] args)
        {
            ulong a = Convert.ToUInt64(Console.ReadLine());
            ulong b = Convert.ToUInt64(Console.ReadLine());
            int counter = a >= 2 ? 1 : 0;
            if (a % 2 == 0) a++;
            for (; a <= b; a += 2)
            {
                bool primary = true;
                for (ulong i = 2; i <= Math.Sqrt(a); i += 1)
                {
                    if (a % i == 0)
                    {
                        primary = false;
                        break;
                    }
                }
                if (primary == true) counter++;
            }
            Console.WriteLine(counter);
        }
    }
}
