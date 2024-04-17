using System;
using System.Collections.Generic;

namespace s2_asd_lw_01_03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите любую скобочную структуру: ");
            char[] input = Console.ReadLine().ToCharArray();
            Stack<string> check = new Stack<string>();
            if (input[0] == ')')
            {
                Console.WriteLine("Структура не является правильной");
                Environment.Exit(0);
            }
            for (int i = 0; i < input.Length; i++)
            {
                if (input[i] == '(') check.Push("-");
                if (input[i] == ')') check.Pop();
            }
            if (check.Count == 0) Console.WriteLine("Структура является правильной");
            else Console.WriteLine("Структура не является правильной");
        }
    }
}