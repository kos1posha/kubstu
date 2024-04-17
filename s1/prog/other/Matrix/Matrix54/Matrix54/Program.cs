using System;
using System.Collections.Generic;

namespace Matrix54
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите ранг квадратной матрицы: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            int[,] A = new int[n, n];
            bool match;
            int i, j;
            List<int> ansClm = new List<int>();
            Random R = new Random();

            for (i = 0; i < n; i++)
            {
                for (j = 0; j < n; j++)
                {
                    A[i, j] = R.Next(2, 5);
                    Console.Write($"{A[i, j]} ");
                }
                Console.WriteLine();
            }

            for (j = 0; j < n; j++)
            {
                match = true;
                for (i = 0; i < n; i++)
                {
                    if (A[i, j] % 2 != 0) { match = false; }
                }
                if (match == true) { ansClm.Add(j); }
                else { ansClm.Add(-1); }

            }

            Console.WriteLine("\nОтвет:");
            for (int k = 0; k < ansClm.Count; k++)
            {
                if (ansClm[k] != -1)
                {
                    for (i = ansClm[k]; ;)
                    {
                        Console.Write($"[{ansClm[k]}] - ");
                        for (j = 0; j < n; j++)
                        {
                            Console.Write($"{A[j, i]}");
                        }
                        Console.WriteLine();
                        break;
                    }
                }
            }
        }
    }
}
