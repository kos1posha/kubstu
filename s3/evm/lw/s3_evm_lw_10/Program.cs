using System;

namespace s3_evm_lw_10
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 1000, i, k, j;
            int[,] A = new int[6, 6] 
            {
                { 0, 1, 5, 2, x, x},
                { 1, 0, x, 1, 3, x},
                { 5, x, 0, 4, 2, 3},
                { 2, 1, 4, 0, x, 6},
                { x, 3, 2, x, 0, 1},
                { x, x, 3, 6, 1, 0}
            };
            int[,] B = new int[6, 6];

            Console.WriteLine("Исходная матрица:");
            Console.WriteLine(" * [1]  [2]  [3]  [4]  [5]  [6]");
            for (i = 0; i < 6; i++)
            {
                Console.Write($"[{i + 1}]");
                for (j = 0; j < 6; j++)
                    Console.Write($" {(A[i, j] != 1000 ? A[i,j].ToString() : "x")}   ");
                Console.WriteLine();
            }

            for (k = 0; k < 6; k++)
                for (i = 0; i < 6; i++)
                    for (j = 0; j < 6; j++)
                        if (A[i, j] > A[i, k] + A[k, j])
                        {
                            A[i, j] = A[i, k] + A[k, j];
                            B[i, j] = k + 1;
                        }


            Console.WriteLine("\nМатрица минимальных расстояний:");
            Console.WriteLine(" * [1]  [2]  [3]  [4]  [5]  [6]");
            for (i = 0; i < 6; i++)
            {
                Console.Write($"[{i + 1}]");
                for (j = 0; j < 6; j++)
                    Console.Write($" {A[i, j]}   ");
                Console.WriteLine();
            }

            //Console.WriteLine("\nМатрица маршрутов:");
            //for (i = 0; i < 6; i++)
            //{
            //    Console.Write(i + 1 + ":\t");
            //    for (j = 0; j < 6; j++)
            //        if (B[i, j] != 0)
            //            Console.Write($"{i + 1} -> {B[i, j]} -> {j + 1}\t");
            //    Console.WriteLine();
            //}
        }
    }
}
