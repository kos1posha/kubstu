using System;
using System.Collections.Generic;

namespace s3_evm_lw_03
{
    class Program
    {
        static void Main(string[] args)
        {
            int KL = 3;
            int L = 7;
            int R = 60;
            int C = 30;

            Queue<int> A = new Queue<int>();
            Random rnd = new Random();

            int ticks = 0;
            int smallTimes = 0;
            int smallWorks = 0;
            int otlWorks = 0;
            int processedSmallWorks = 0;
            decimal middleTimeOfMinimumWorks = 0;

            for (int i = 0; i < C; i++)
            {
                if (rnd.Next(100) < R)
                    A.Enqueue(L);
                else
                {
                    int work = rnd.Next(1, 5);
                    A.Enqueue(work);
                    if (work <= KL) smallWorks++;
                }
            }

            Console.WriteLine($"Поток команд: {String.Join(" ", A)}");

            while (A.Count != 0)
            {
                int nextWork = A.Dequeue();
                if (nextWork > KL)
                {
                    nextWork -= KL;
                    A.Enqueue(nextWork);
                    otlWorks++;
                }
                else
                {
                    if (processedSmallWorks < smallWorks)
                    {
                        processedSmallWorks++;
                        smallTimes += ticks;
                    }
                }
                ticks++;
            }

            if (smallWorks > 0)
                middleTimeOfMinimumWorks = (decimal)smallTimes / smallWorks;

            Console.WriteLine($"\nТиков: {ticks}" +
                              $"\nСреднее время выполнения маленьких работ: {middleTimeOfMinimumWorks:F4}" +
                              $"\nОткладываний: {otlWorks}");
        }
    }
}
