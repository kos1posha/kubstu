using System;

namespace s2_asd_lw_05
{
    class Program
    {
        public static void LineSearchMod(int[] array, Predicate<int> predicate)
        {
            Console.WriteLine();
            foreach (int item in array) if (predicate(item)) Console.Write($"{item} ");
        }
        static void Main(string[] args)
        {
            Console.Write("Введите размерность: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] array1 = new int[n], array2 = new int[n];
            Random random = new Random();

            for (int i = 0; i < n; i++)
            {
                array1[i] = i + 1;
                array2[i] = random.Next(1, 16);
            }

            Console.WriteLine("\narray1:");
            foreach (int item in array1) Console.Write($"{item} ");
            LineSearchMod(array1, item => item % 3 == 0);

            Console.WriteLine();

            Console.WriteLine("\narray2:");
            foreach (int item in array2) Console.Write($"{item} ");
            LineSearchMod(array2, item => item % 3 == 0);
        }
    }
}
