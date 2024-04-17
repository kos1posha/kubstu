using System;
using System.Collections.Generic;
using System.Linq;

namespace s3_evm_lw_04
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] times = new int[20];
            int[] procArray = new int[4];

            Queue<int> timesQueue = new Queue<int>();
            Random rand = new Random();

            for (int i = 0; i < times.Length; i++)
                times[i] = rand.Next(1, 15);

            Array.Sort(times);
            Array.Reverse(times);
            Console.WriteLine($"Процессы ({times.Sum()}): {String.Join(" ", times)}\n" +
                              $"Оптимальное расписание - {Convert.ToInt32(Math.Ceiling((double)times.Sum() / procArray.Length))}\n");

            for (int i = 0; i < times.Length; i++)
                timesQueue.Enqueue(times[i]);

            Console.WriteLine("Алгоритм Макноттона");

            McNaughtonsAlgorithm(times, procArray.Length);

            Console.WriteLine("\nАлгоритм LPT");

            LPTAlgorithm(procArray, timesQueue);
        }

        static void McNaughtonsAlgorithm(int[] times, int procQuantity)
        {
            int optimal = Convert.ToInt32(Math.Ceiling((double)times.Sum() / procQuantity));

            int current = optimal;
            int currentProcTSum = 0;
            string result = string.Empty;

            for (int i = 0; i < times.Length; i++)
            {
                if (procQuantity > 0 && current <= 0)
                {
                    int change = current;
                    current += optimal;

                    Console.WriteLine($"Очередь задач на процессоре {procQuantity}({currentProcTSum}): {result}");

                    currentProcTSum = -change;
                    if (change != 0)
                        result = $"{i - 1}({-change}) ";
                    procQuantity--;
                }

                current -= times[i];

                if (current > 0)
                {
                    result += $"{i + 1}({times[i]}) ";
                    currentProcTSum += times[i];
                }
                else
                {
                    result += $"{i + 1}({times[i] + current}) ";
                    currentProcTSum += times[i] + current;
                }
            }

            Console.WriteLine($"Очередь задач на процессоре {procQuantity}({currentProcTSum}): {result}");
            Console.WriteLine($"Задержка процессора - {current}");
        }

        static void LPTAlgorithm(int[] procArray, Queue<int> timesQ)
        {
            int n = 1;
            string[] res = new string[procArray.Length];

            do
            {
                for (int i = 0; i < procArray.Length; i++, n++)
                {
                    int temp = timesQ.Dequeue();
                    int min = Array.IndexOf(procArray, procArray.Min());

                    procArray[min] += temp;
                    res[min] += $"{n}({temp}) ";
                }
            }
            while (timesQ.Count > 0);

            for (int i = 0; i < procArray.Length; i++)
                Console.WriteLine($"Очередь на процессоре {i + 1}({procArray[i]}): {res[i]}");

            Array.Sort(procArray);

            int lessTime = 0;
            for (int i = 0; i < procArray.Length; i++)
                lessTime += procArray[3] - procArray[i];

            Console.WriteLine($"Простой процессора - {lessTime}");
        }

    }
}
