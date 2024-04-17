using System;

namespace Matrix75
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

            int[,] A = new int[n, m];
            int maxElementIndex = 0, minElementIndex = 0, maxElement = 0, minElement = 1000;
            Random Random = new Random();
            Console.WriteLine("Исходная матрциа: ");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    A[i, j] = Random.Next(100, 1000);
                    if (maxElement < A[i, j])
                    {
                        maxElement = A[i, j];
                        maxElementIndex = i;
                    }
                    if (minElement > A[i, j])
                    {
                        minElement = A[i, j];
                        minElementIndex = i;
                    }
                }
            }
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    Console.Write($"{A[i, j]} ");
                }
                if (i == minElementIndex) { Console.Write(" - "); }
                if (i == maxElementIndex) { Console.Write(" + "); }
                Console.WriteLine();
            }
            Console.WriteLine($"\nМинимальный элемент равен {minElement} и находится на строке {minElementIndex + 1}\nМаксимальный элемент равен {maxElement} и находится на строке {maxElementIndex + 1}");
            if (maxElementIndex == minElementIndex) { Console.WriteLine("Так как максимальный и минимальный элементы матрицы находятся на одной строке, перестановка ничего не изменит"); Environment.Exit(0); }
            Console.WriteLine("\nКонечная матрица: ");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    if (i == minElementIndex) { Console.Write($"{A[maxElementIndex, j]} "); continue; }
                    if (i == maxElementIndex) { Console.Write($"{A[minElementIndex, j]} "); continue; }
                    Console.Write($"{A[i, j]} ");
                }
                if (i == minElementIndex) { Console.Write(" + "); }
                if (i == maxElementIndex) { Console.Write(" - "); }
                Console.WriteLine();
            }
        }
    }
}