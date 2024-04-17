using System;
using System.Collections.Generic;
using System.Linq;

namespace s3_evm_lw_05_01
{
    class Program
    {
        static int procCount = 4;
        static int requCount = 40;
        static int[] procs = new int[procCount];
        static int[] time = new int[procCount];
        static Queue<int> requQueue = new Queue<int>();
        static Random random = new Random();

        static void Main(string[] args)
        {
            Console.WriteLine("Алгоритм с общей памятью\n");

            for (int i = 0; i < procCount; i++)
                procs[i] = 0;
            for (int i = 0; i < requCount; i++)
                requQueue.Enqueue(random.Next(1, 10));

            Console.WriteLine($"Длины заявок: {String.Join(" ", requQueue)}");

            while (!ProcessingCheck())
                for (int i = 0; i < procCount; i++)
                {
                    if ((procs[i] == 0) || (--procs[i] == 0))
                    {
                        time[i] = time[i] + 2;
                        if (requQueue.Count() != 0)
                        {
                            procs[i] = requQueue.Dequeue();
                            time[i] = ++time[i] + procs[i];
                            Console.WriteLine($"{requCount - requQueue.Count})  r:{procs[i]}:+3 -> p:{i + 1} -> pt:{time[i]}");
                        }
                    }
                    else
                        procs[i] = procs[i] - 1;
                }

            Console.WriteLine("\nВремя работы:");
            for (int i = 0; i < time.Length; i++)
                Console.WriteLine($"- процессора {i + 1} = {time[i]}");
        }

        static bool ProcessingCheck()
        {
            if (requQueue.Count != 0) 
                return false;

            foreach (int proc in procs)
                if (proc > 0) 
                    return false;

            return true;
        }
    }
}