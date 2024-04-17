using System;

namespace Matrix11
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите количество строк: ");
            int n = Convert.ToInt32(Console.ReadLine());
            if (n < 3)
            {
                Console.Clear();
                Console.Write("Необходимо минимум 3 строки");
                Console.ReadKey(true);
                Console.Clear();
                Console.Write("Введите количество строк: ");
                n = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Введите количество столбцов: ");
            int m = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            uint[,] A = new uint[n, m];
            ulong productAll = 1;
            uint sumAll = 0, sum3 = 0, productLastButOne = 1;
            Random Random = new Random();
            Console.WriteLine("Исходная матрица: ");
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    A[i, j] = (uint) Random.Next(1, 10);
                    Console.Write($"{A[i, j]} ");
                    sumAll += A[i, j];
                    productAll *= A[i, j];
                    if (i == n - 2) { productLastButOne *= A[i, j]; }
                    if (j == 2) { sum3 += A[i, j]; }
                }
                Console.WriteLine();
            }
            Console.WriteLine($"\nСумма элементов 3-го столбца = {sum3}");
            Console.WriteLine($"Сумма всех элементов матрицы = {sumAll}");
            Console.WriteLine($"Произведение элементов предпоследней строки = {productLastButOne}");
            Console.WriteLine($"Произведение всех элементов матрицы = {productAll}");
        }
    }
}
