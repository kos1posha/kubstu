using System;

namespace s1_prog_lw_04
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите размерность массива: ");
            int n = int.Parse(Console.ReadLine());
            Random rand = new Random();
            int[] mas = new int[n]; int sum1 = 0, sum2 = 0, f0 = 0, l0 = 0;
            for (int i = 0; i < mas.Length; i++)
            {
                mas[i] = rand.Next(-2, 2);
                Console.Write(mas[i] + "  ");
            }
            Console.WriteLine();
            for (int i = 0; i < mas.Length; i++)
            {
                if (i % 2 == 0) sum1 += mas[i];
            }
            f0 = Array.IndexOf(mas, 0);
            l0 = Array.LastIndexOf(mas, 0);
            for (int i = f0; i < l0; i++)
            {
                sum2 += mas[i];
            }
            Console.WriteLine($"Сумма четных элементов: {sum1}\nСумма чисел между первым и последним нулевыми элементами: {sum2}");
        }
    }
}
