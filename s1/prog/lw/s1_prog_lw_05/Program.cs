using System;

namespace s1_prog_lw_05
{
    class Program
    {
        private static int[,] WriteMatrixDimension()
        {
            int strg, clmn;
            {
                for (; ; )
                {
                StrgUncorrect:
                    Console.Write("Введите количество строк: ");
                    strg = Convert.ToInt32(Console.ReadLine());
                    if (strg <= 0)
                    {
                        Console.Clear();
                        Console.Write("Количество строк указано некорректно. Нажмите любую клавишу, чтобы повторить ввод.");
                        Console.ReadKey(false);
                        Console.Clear();
                        goto StrgUncorrect;
                    }
                ClmnUncorrect:
                    Console.Write("Введите количество столбцов: ");
                    clmn = Convert.ToInt32(Console.ReadLine());
                    if (clmn <= 0)
                    {
                        Console.Clear();
                        Console.Write("Количество столбцов указано некорректно. Нажмите любую клавишу, чтобы повторить ввод.");
                        Console.ReadKey(false);
                        Console.Clear();
                        Console.WriteLine($"Введите количество строк: {strg}");
                        goto ClmnUncorrect;
                    }
                    Console.Clear();
                    break;
                }
                return new int[strg, clmn];
            }
        }
        public static void RandomFillingMatrix(int[,] matrix)
        {
            Random Random = new Random();
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    matrix[i, j] = Random.Next(-2, 3);
                }
            }
        }
        public static void WriteMatrix(int[,] matrix)
        {
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                for (int j = 0; j < matrix.GetLength(1); j++)
                {
                    var space = matrix[i, j] < 0 ? "" : " ";
                    Console.Write($"{space}{matrix[i, j]} ");
                }
                Console.WriteLine();
            }
        }
        private static int ClmnZeroFinder(int[,] matrix)
        {
            int counter = 0;
            for (int clmn = 0; clmn < matrix.GetLength(1); clmn++)
            {
                for (int strg = 0; strg < matrix.GetLength(0); strg++)
                {
                    if (matrix[strg, clmn] == 0) { counter++; break; }
                }
            }
            return counter;
        }
        private static int StrgMaxSeriesOfIdenticalElementsFinder(int[,] matrix)
        {
            int strgMaxSeries = 0, maxCounter = 0, counter = 0;
            bool once = false;
            for (int strg = 0; strg < matrix.GetLength(0); strg++)
            {
                for (int clmn = 1; clmn < matrix.GetLength(1); clmn++)
                {
                    if (matrix[strg, clmn] == matrix[strg, clmn - 1])
                    {
                        counter++;
                        once = true;
                    }
                    else
                    {
                        counter = 0;
                    }
                    if (maxCounter < counter)
                    {
                        maxCounter = counter;
                        strgMaxSeries = strg + 1;
                    }
                }
                if (maxCounter < counter)
                {
                    maxCounter = counter;
                }
            }
            if (once) { return strgMaxSeries; }
            else { return 0; }
        }

        public static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.DarkBlue;
            int[,] matrix = WriteMatrixDimension();
            RandomFillingMatrix(matrix); Console.WriteLine("Исходная матрица:");
            WriteMatrix(matrix);
            if (ClmnZeroFinder(matrix) == 0) { Console.WriteLine("\nВ матрице нет ни одного столбца с хотя бы одним нулевым элементом."); }
            else { Console.WriteLine($"\nКоличество столбцов с хотя бы одним нулевым элементом: {ClmnZeroFinder(matrix)}"); }
            if (StrgMaxSeriesOfIdenticalElementsFinder(matrix) == 0) { Console.WriteLine("В матрице нет ни одной строки с серией повторяющихся элементов."); }
            else { Console.WriteLine($"\nСтрока с максимальной серией одинаковых элементов: {StrgMaxSeriesOfIdenticalElementsFinder(matrix)}"); }
        }
    }
}
