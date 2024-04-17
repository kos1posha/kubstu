using System;

namespace s2_asd_lw_06_01
{
    class Program
    {
        public delegate int[] SwitchMethod(int[] array, int index);
        public static int[] ToBeginning(int[] array, int index)
        {
            int table = array[index - 1];
            for (int i = index - 1; i > 0; i--)
            {
                array[i] = array[i - 1];
            }
            array[0] = array[index];
            array[index] = table;
            return array;
        }
        public static int[] Transposition(int[] array, int index)
        {
            for (int i = index; i > 0; i--)
                (array[i], array[i - 1]) = (array[i - 1], array[i]);
            return array;
        }
        public static int[] LineSearch(int[] array, Predicate<int> predicate, SwitchMethod switchMethod)
        {
            int ans = int.MinValue, indAns = 0;
            for (int i = 0; i < array.Length; i++)
            {
                if (predicate(array[i]))
                {
                    if (array[i] > ans)
                    {
                        ans = array[i];
                        indAns = i;
                    }
                }
            }
            return switchMethod(array, indAns);
        }
        static void Main(string[] args)
        {
            int[] arrayTest1 = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int[] arrayTest2 = new int[] { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };

            Console.WriteLine("Transposition:");
            foreach (int item in arrayTest1) Console.Write($"{item} "); Console.Write(" -->  ");
            foreach (int item in Transposition(arrayTest1, 6)) Console.Write($"{item} "); Console.WriteLine();

            Console.WriteLine("ToBeginning:");
            foreach (int item in arrayTest2) Console.Write($"{item} "); Console.Write(" -->  ");
            foreach (int item in ToBeginning(arrayTest2, 3)) Console.Write($"{item} "); Console.WriteLine();

            int[] array1 = new int[] { 103, 2, -10, 11, 91, -121, 99, 6 };
            int[] array2 = new int[] { -14, 23, 176, 22, -363, 0, 7 };

            Console.WriteLine("\nTransposition:");
            foreach (int item in array1) Console.Write($"{item} "); Console.Write(" -->  ");
            foreach (int item in LineSearch(array1, item => item % 11 == 0, Transposition)) Console.Write($"{item} ");

            Console.WriteLine("\nToBeginning:");
            foreach (int item in array1) Console.Write($"{item} "); Console.Write(" -->  ");
            foreach (int item in LineSearch(array2, item => item % 11 == 0, ToBeginning)) Console.Write($"{item} ");

            Console.ReadKey(true);
        }
    }
}
