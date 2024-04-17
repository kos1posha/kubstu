using System;
using System.Collections.Generic;

namespace Array137
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("Введите размер массива: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            int[] A = new int[n];
            Random R = new Random();
            List<int> sort_A = new List<int>();
            int first_even_numb = 0;
            bool start_sort = false;
            Console.Write("Исходный массив: ");
            for (int i = 0; i < n; i++)
            {
                A[i] = R.Next(-5, 6);
                Console.Write($"{A[i]} ");
            }
            Console.WriteLine("\n");
            for (int i = 0; i < n; i++)
            {
                if (start_sort == true) { sort_A.Add(A[i]); }
                if ((A[i] != 0) && (Math.Abs(A[i]) % 2 == 0) && (start_sort == false)) 
                { 
                    start_sort = true; 
                    first_even_numb = i; 
                    Console.WriteLine($"Первое четное число - это {A[i]} под индексом {i}"); 
                }
            }
            if (start_sort)
            {
                sort_A.Sort();
                Console.WriteLine();
                Console.Write("Конечный массив: ");
                for (int i = 0; i < first_even_numb; i++) { Console.Write($"{A[i]} "); }
                Console.Write($"{A[first_even_numb]} | ");
                for (int i = 0; i < sort_A.Count; i++) { Console.Write($"{sort_A[i]} "); }
                Console.WriteLine();
            }
            else { Console.WriteLine("В массиве нет нечетных чисел"); }
        }
    }
}
