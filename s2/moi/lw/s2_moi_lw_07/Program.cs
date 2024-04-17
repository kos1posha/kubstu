using System;

namespace s2_moi_lw_07
{
    class Program
    {
        static void Main(string[] args)
        {
            bool[] X = new bool[4], Y = new bool[4], G = new bool[4], P = new bool[4], c = new bool[5], s = new bool[4];
            Console.Write("Введите первое число: ");
            byte x = Convert.ToByte(Console.ReadLine(), 2);
            Console.Write("Введите второе число: ");
            byte y = Convert.ToByte(Console.ReadLine(), 2);
            Console.WriteLine();
            c[0] = false;
            for (int i = 0; i < 5; i++)
            {
                if (i < 4)
                {
                    byte mask = 0b0001;
                    X[i] = Convert.ToBoolean((x & (mask << i)) >> i);
                    Y[i] = Convert.ToBoolean((y & (mask << i)) >> i);
                    G[i] = X[i] & Y[i];
                    P[i] = X[i] ^ Y[i];
                    Console.Write("| {0,5} | {1,5} | {2,5} | {3,5} ", X[i], Y[i], G[i], P[i]);
                }
                if (i > 0)
                {
                    c[i] = G[i - 1] | P[i - 1] & c[i - 1];
                }
                if (i < 4)
                {
                    s[i] = P[i] ^ c[i];
                    Console.WriteLine("| {0,5} | {1,5} | ", c[i], s[i]);
                }
            }
            Console.Write($"\nCF = {c[4]}\nOF = {c[3] ^ c[4]}\nSF = {s[3]}\nZF = {!(s[3] | s[2] | s[1] | s[0])}\nPF = {!(s[3] ^ s[2] ^ s[1] ^ s[0])}");
        }
    }
}
