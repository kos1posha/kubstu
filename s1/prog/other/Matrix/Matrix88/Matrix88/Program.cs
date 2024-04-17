using System;

namespace Matrix88
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите количество строк: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Write("Введите количество столбцов: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            int[,] spiral = new int[n, m];
            int str = m, clm = n;

            for (int i, j, deep = 0, output = 1; output <= 10; str--, clm--, deep++)
            {
                for (i = deep, j = deep; j < clm; spiral[i, j] = output, j++) {}
                for (i = deep + 1, j = clm - 1; i < str; spiral[i, j] = output, i++) {}
                for (i = str - 1, j = clm - 2; j >= deep; spiral[i, j] = output, j--) {}
                for (i = str - 2, j = deep; i > deep; spiral[i, j] = output, i--) {}
                output++;
            }
            for (int i = 0; i < n; Console.WriteLine(), i++) 
            { 
                for (int j = 0; j < m; Console.Write("{0,4} ", spiral[i, j]), j++) {} 
            }
        }
    }
}