using System;

namespace s2_asd_lw_03_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите количество войнов: ");
            int[] warsLine = new int[Convert.ToInt32(Console.ReadLine())];
            for (int i = 0; i < warsLine.Length; i++) warsLine[i] = i + 1;
            SpiralList<int> warsCircle = new SpiralList<int>(warsLine);
            Node<int> temp = warsCircle.Last;
            for (int i = 1; warsCircle.Count != 2; i++)
            {
                if (i % 3 == 0)
                {
                    if (temp.Next == warsCircle.First) warsCircle.First = temp.Next.Next;
                    if (temp.Next == warsCircle.Last) warsCircle.Last = temp;
                    temp.Next = temp.Next.Next;
                    warsCircle.Count--;
                }
                else temp = temp.Next;
            }
            Console.WriteLine($"Из них живыми остались {warsCircle.First.Data} и {warsCircle.Last.Data}");
        }
    }
}
