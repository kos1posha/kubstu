using System;

namespace s2_moi_lw_14_02
{
    class Program
    {
        static void Main(string[] args)
        {
            uint x = Convert.ToUInt32(Console.ReadLine());
            uint N1 = x, N2 = 0;
            string strx = x.ToString();
            for (int i = 0; i < strx.Length; i++)
                N2 += (uint)strx[i] - 48;
            for (int i = 0; x > 1; i++)
                N1 -= 9 * (x /= 10);
            Console.WriteLine($"N1 = {N1}\nN2 = {N2}");
        }
    }
}