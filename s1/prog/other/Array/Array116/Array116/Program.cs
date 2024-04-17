using System;
using System.Collections.Generic;

namespace Array116
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Размер массива: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            bool ans = false;
            int[] A = new int[n];
            List<int> sum = new List<int>();
 
            Random R = new Random();
            Console.Write("Исходный массив: ");
            for (int i = 0; i < n; i++)
            {
                A[i] = R.Next(-5, 6);
                Console.Write($"{A[i]} ");
            }
            Console.WriteLine();
            for (int i = 0; i < n - 2; i++)
            {
                int niceNumb = 0; 
                if ((A[i] < 0) && (Math.Abs(A[i]) % 2 == 1)) { niceNumb++; }
                if ((A[i + 1] < 0) && (Math.Abs(A[i + 1]) % 2 == 1)) { niceNumb++; }
                if ((A[i + 2] < 0) && (Math.Abs(A[i + 2]) % 2 == 1)) { niceNumb++; }
                if (niceNumb == 2) 
                { 
                    ans = true; 
                    sum.Add(A[i] + A[i + 1] + A[i + 2]); 
                    Console.WriteLine($"{A[i]} {A[i + 1]} {A[i + 2]} | {A[i] + A[i + 1] + A[i + 2]}"); 
                }
            }
            if (ans)
            {
                sum.Sort(); sum.Reverse();
                Console.Write("\nМаксимальная сумма по условию: " + sum[0]);
            }
            else 
            { 
                Console.WriteLine("\nВ массиве нет трех стоящих рядом чисел, подходящих по условию"); 
            }
            Console.WriteLine();
        }
    }
}