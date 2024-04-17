using System;

namespace Array21
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("Введите размер массива: ");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            double[] A = new double[n];
            Random Random = new Random();
            int counterEven = 0, counterOdd = 0, counterPozitive = 0, counterNegative = 0;

            Console.Write("Исходный массив: ");
            for (int i = 0; i < n; i++)
            {
                A[i] = Convert.ToDouble($"{Random.Next(-10, 11) + Random.NextDouble():F2}");
                Console.Write($"{A[i]} ");
            }
            for (int i = 0; i < n; i++)
            {
                //Console.Write($"{A[i]}");
                int lengthAi = Convert.ToString(Math.Abs(A[i])).Length;
                double evenDivider = Convert.ToDouble("0," + new string(' ', lengthAi - 3).Replace(" ", "0") + "2");
                double evenChecker = Convert.ToDouble("0," + new string(' ', lengthAi - 3).Replace(" ", "0") + "1");
                double evenRemainder = Convert.ToDouble($"{Math.Abs(A[i]) % evenDivider:E}");
                //Console.Write($"|{evenDivider}|{evenChecker}|{evenRemainder}|{evenRemainder != evenChecker}\n");
                if (evenRemainder != evenChecker) { counterEven++; }
                else { counterOdd++; }
            }
            Console.WriteLine($"\n[1]Количество четный чисел: {counterEven}\n[1]Количество нечетных чисел: {counterOdd}");
            for (int i = 0; i < n; i++)
            {     
                if (A[i] != 0)
                {
                    if (A[i] > 0) { counterPozitive++; }
                    else { counterNegative++; }
                }
            }
            Console.Write($"\nКоличество положительный чисел: {counterPozitive}\nКоличество отрицательный чисел: {counterNegative}");
            Console.WriteLine();
        }
    }
}
