using System;

namespace s2_asd_lw_01_02
{
    class Program
    {
        static void Main(string[] args)
        {
            AltStack altStack = new AltStack();
            AltStack mid = new AltStack();
            AltStack answer = new AltStack();
            Console.WriteLine("Вводите элементы стека (введите -1, чтобы прекратить ввод):");
            while (true)
            {
                int input = Convert.ToInt32(Console.ReadLine());
                if (input == -1) break;
                altStack.Push(input);
            }
            answer.Push(altStack.Pop());
            while (altStack.Count > 1) mid.Push(altStack.Pop());
            while (mid.Count > 0) answer.Push(mid.Pop());
            answer.Push(altStack.Pop());
            Console.WriteLine("Ответ: ");
            answer.Show();
        }
    }
}
