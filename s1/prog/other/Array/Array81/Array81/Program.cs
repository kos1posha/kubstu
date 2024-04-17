using System;
using System.Collections.Generic;

namespace Array81
{
    class Program
    {
        static void Main(string[] args)
        {
            int max = 0;
            Console.Write("Размер массива = ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();
            int[] A = new int[n];
            List<int> even_numbers = new List<int>();
            Random R = new Random();
            Console.Write("Исходный массив:");
            for (int i = 0; i < n; i++)
            {
                A[i] = R.Next(2, 21);
                Console.Write($"{A[i]} ");
                if (A[i] % 2 == 0) even_numbers.Add(A[i]);
            }
            Console.Write("\n\nМассив четных чисел:");
            for (int i = 0; i < even_numbers.Count; i++)
            {
                Console.Write($"{even_numbers[i]} ");
            }
            max = even_numbers[0];
            for (int i = 1; i < even_numbers.Count; i++)
            {   
                max = Math.Max(max, even_numbers[i]);
            }
            Console.Write($"\n\nМаксимальное четное число: {max}");
            Console.Write("\n\nКонечный массив:");
            for (int i = 0; i < n; i++)
            {
                if (A[i] < max)
                {
                    if (A[i] % 2 == 0) { A[i] = 0; }
                    else { A[i] = 1; }
                }
                Console.Write($"{A[i]} ");
            }
            Console.WriteLine();
        }
    }
}