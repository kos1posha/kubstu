using System;

namespace s2_moi_lw_14_03
{
    class Program
    {
        static void Main(string[] args)
        {
        Start:
            byte[] x = new byte[15];
            byte zeroCount = 0, oneCount = 0;
            Random r = new Random();
            for (int i = 0; i < x.Length; i++)
            {
                x[i] = (byte)r.Next(2);
                Console.Write(x[i]);
                if (x[i] == 0) zeroCount++;
                else oneCount++;
            }
            string ans = oneCount > zeroCount ? "Единиц" : "Нулей";
            Console.WriteLine($"\n{ans} больше");
            Console.ReadKey(true);
            goto Start;
        }
    }
}
