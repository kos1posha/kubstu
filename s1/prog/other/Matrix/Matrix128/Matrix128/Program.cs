using System;

namespace Matrix128
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,,] matrix = new int[3, 9, 4];
            int[] counter = new int[3] { 0, 0, 0 };
            int max = 0;
            Random Random = new Random();
            Console.WriteLine("Исходные матрицы:");
            for (int k = 0; k < 3; k++)
            {
                Console.WriteLine($"+---+[{k + 1}]+---+");
                for (int i = 0, c = 0; i < 9; c = 0, i++)
                {
                    for (int j = 0; j < 4; j++)
                    {
                        matrix[k, i, j] = Random.Next(2);
                        Console.Write($"{matrix[k, i, j]}   ");
                        if (matrix[k, i, j] == 0) c++;
                    }
                    if (c == 4) { Console.Write(" + "); counter[k]++; }
                    Console.WriteLine();
                }
                Console.WriteLine("+---+---+---+\n");
            }
            Console.WriteLine("\n");
            max = Math.Max(counter[0], counter[1]); max = Math.Max(max, counter[2]);
            if (max == 0) { Console.WriteLine("Ни в одной матрице нет нулевой строки"); Environment.Exit(0); }
            Console.WriteLine("Ответ");
            for (int k = 0; k < 3; k++)
            {
                if (counter[k] == max)
                {
                    Console.WriteLine($"+---+[{k + 1}]+---+");
                    for (int i = 0; i < 9; i++)
                    {
                        for (int j = 0; j < 4; j++)
                        {
                            Console.Write($"{matrix[k, i, j]}   ");
                        }
                        Console.WriteLine();
                    }
                }
                else continue;
                Console.WriteLine("+---+---+---+\n");
            }
        }
    }
}
