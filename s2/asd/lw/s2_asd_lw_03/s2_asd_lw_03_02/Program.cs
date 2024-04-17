using System;

namespace s2_asd_lw_03_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Student[] input = new Student[5]
            {
                new Student("Don", "G-10", new int[5] { 4, 4, 3, 2, 4 }),
                new Student("Emily", "G-17", new int[5] { 5, 4, 4, 5, 5 }),
                new Student("Bob", "G-12B", new int[5] { 5, 5, 5, 5, 5 }),
                new Student("Cock", "G-10", new int[5] { 5, 4, 4, 5, 3 }),
                new Student("Abby", "G-17", new int[5] { 2, 2, 4, 3, 3 })
            };

            Array.Sort(input);
            bool nobody = true;
            for (int i = 0; i < input.Length; i++)
            {
                for (int j = 0; j < 5; j++)
                {
                    if (input[i].Grades[j] == 2)
                    {
                        Console.WriteLine(input[i].Name);
                        nobody = false;
                        break;
                    }
                }
            }
            if (nobody) Console.WriteLine("No one have two");
        }
    }
}
