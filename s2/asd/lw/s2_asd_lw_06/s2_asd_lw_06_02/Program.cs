using System;
using System.Collections.Generic;

namespace s2_asd_lw_06_02
{
    class Program
    {
        static void Main(string[] args)
        {
            int N;
            BinaryTree binaryTree = new BinaryTree();
            {
            noLink:
                Console.Write("Введите N: ");
                N = Convert.ToInt32(Console.ReadLine());
                Console.Write("Ручной ввод 5 элементов (1) или автозаполнение в интеварле от -99 до 99 (2): ");
                switch (Console.ReadLine())
                {
                    case "1":
                        for (int i = 0; i < 5; i++)
                        {
                            Console.Write($"{i + 1}) ");
                            binaryTree.Add(Convert.ToInt32(Console.ReadLine()));
                        }
                        break;
                    case "2":
                        Random random = new Random();
                        for (int i = 0; i < 5; i++)
                        {
                            binaryTree.Add(random.Next(-99, 100));
                        }
                        break;
                    default:
                        Console.WriteLine("Неуважительно базаришь, кучерявый."); Console.ReadKey(true); Console.Clear();
                        goto noLink;
                }
                Console.ReadKey(true);
                Console.Clear();
            }  // Ввод данных.
            binaryTree.Show(); Console.WriteLine();

            List<int?> result = new List<int?>();
            binaryTree.BinarySearch(N, result);

            foreach (int? item in result) Console.WriteLine(item);
        }
    }
}
