using System;

namespace s1_prog_lw_07_02
{
    class Program
    {
        public static int TheProductOfOddElements(int arg)
        {
            if (arg == 1) return 1;
            if (arg % 2 == 1) return arg * TheProductOfOddElements(arg - 1);
            else return TheProductOfOddElements(arg - 1);
        }
        public static int SumOfAllArrayElements(int n, int[] array)
        {
            if (n == 0) return array[0];
            else return SumOfAllArrayElements(n - 1, array) + array[n];
        }
        static void Main(string[] args)
        {
        Restart:
            Console.WriteLine("Выберите задание: \n  1) Рекурсия: Сумма четных элементов от 1 до N\n  2) Рекурсия: Сумма всех элементов массива");
            switch (Console.ReadLine())
            {
                case "1":
                    Console.Clear();
                    Console.Write("Введите аргумент: ");
                    int arg = Convert.ToInt32(Console.ReadLine());
                    Console.WriteLine($"Результат работы рекурсии: {TheProductOfOddElements(arg)}");
                    int product = 1;
                    for (int i = 1; i <= arg; i++)
                    {
                        if (i % 2 == 1)
                        {
                            product *= i;
                        }
                    }
                    Console.WriteLine($"Результат работы цикла: {product}");
                    break;
                case "2":
                    Console.Clear();
                    Console.Write("Введите размер массива: ");
                    int n = Convert.ToInt32(Console.ReadLine());
                    int[] array = new int[n];
                    Random R = new Random();
                    int sum = 0;
                    Console.WriteLine("Исходный массив:");
                    for (int i = 0; i < n; array[i] = R.Next(-256, 257), sum += array[i], Console.Write($"{array[i]} "), i++) { };
                    Console.WriteLine($"\nСумма элементов массива подсчитанная циклом: {sum}");
                    Console.WriteLine($"Сумма элементов массива подсчитанная рекурсией: {SumOfAllArrayElements(n - 1, array)}");
                    break;
                default:
                    Console.WriteLine("Ошибка ввода. Нажмите любую клавишу, чтобы повторить ввод.");
                    Console.ReadKey(true);
                    Console.Clear();
                    goto Restart;
            }
        }
    }
}