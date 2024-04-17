using System;
using System.Collections.Generic;

namespace Array113
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.Write("Введите размер массива: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            int numb = 0, max_numb = 0, max_count = 0;
            int[] A = new int[n];
            List<int> sopen = new List<int>();
            Random R = new Random();
            Console.Write("Исходный массив: ");
            for (int i = 0; i < n; i++)
            {
                A[i] = R.Next(2,11);
                Console.Write($"{A[i]} ");
            }
            Console.WriteLine();
            for (int i = 0; i < n; i++)
            {
                sopen.Clear();
                int counter = 1;
                for (int j = i; j < n - 1; j++)
                {
                    sopen.Add(A[i]);
                    if ((A[j] > 0) && (A[j] % 2 == 0) && (A[j + 1] > 0) && (A[j + 1] % 2 == 0))
                    {
                        counter++;
                        i++;
                        if (j == n - 2) sopen.Add(A[i]);
                    }
                    else { break; }
                }
                if (counter > 1)
                {
                    numb++;
                    Console.Write($"\nСерия [{numb}] - ");
                    for (int z = 0; z < sopen.Count; z++) { Console.Write($"{sopen[z]} "); }
                }
                if (max_count < counter) { max_count = counter; max_numb = numb ; }
            }
            if (numb > 0) { Console.WriteLine($"\n\nМаксимальная серия положительных четных чисел равна {max_count} и соотвествует серии [{max_numb}]"); }
            else { Console.WriteLine("\n\nВ массиве нет ни одной серии положительных четных чисел"); }
        }
    }
}