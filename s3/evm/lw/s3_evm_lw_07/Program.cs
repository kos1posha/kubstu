using System;
using System.Collections.Generic;

namespace s3_evm_lw_07
{
    class Program
    {
        static int stCount = 4;
        static int packCount = 8;
        static int collisionsCount = 0;
        static int time = 0;
        static int[] tempFrame = new int[stCount];
        static Queue<int>[] stations = new Queue<int>[stCount];

        static void Main(string[] args)
        {
            for (int i = 0; i < stCount; i++)
            {
                stations[i] = new Queue<int>();
                Genery(i);
            }
            ZeroAddict();

            Aloha();
        }
        static void Genery(int stInd)
        {
            for (int i = 0; i < packCount; i++)
            {
                while (new Random().Next(0, 100) > 39)
                    stations[stInd].Enqueue(0);
                stations[stInd].Enqueue(1);
            }
        }
        static void ZeroAddict()
        {
            int packMaxCount = stations[0].Count;
            for (int i = 1; i < stations.Length; i++)
                if (packMaxCount < stations[i].Count)
                    packMaxCount = stations[i].Count;

            for (int i = 0; i < stations.Length; i++)
                while (stations[i].Count != packMaxCount)
                    stations[i].Enqueue(0);
        }
        static bool Check()
        {
            foreach (Queue<int> q in stations)
                if (q.Count != 0)
                    return false;

            return true;
        }
        static void ShowStations()
        {
            for (int i = 0; i < stCount; i++)
                Console.WriteLine($"Станция {i + 1}: {String.Join(" ", stations[i])}");
        }
        static void Aloha()
        {
            Console.WriteLine("Чистая алоха");
            Console.WriteLine("Распределение сообщений на временной шкале (0-сообщение не отправляется данной станцией):");
            ShowStations();
            while (!Check())
            {
                int came = 0;
                for (int i = 0; i < stCount; i++)
                {
                    tempFrame[i] = stations[i].Dequeue();
                    if (tempFrame[i] != 0)
                        came++;
                }
                time++;
                if (came > 1)
                {
                    collisionsCount++;
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("Столкновение!\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    for (int j = 0; j < tempFrame.Length; j++)
                        if (tempFrame[j] != 0)
                        {
                            for (int k = 0, retry = new Random().Next(0, 4); k < retry; k++)
                                stations[j].Enqueue(0);

                            stations[j].Enqueue(tempFrame[j]);
                            ZeroAddict();
                        }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("Сообщение передано или сообщения не передавались вовсе\n");
                    Console.ForegroundColor = ConsoleColor.White;
                }
                ShowStations();
            }
            Console.WriteLine("\nКолличество коллизий - " + collisionsCount);
            Console.WriteLine("Потраченое время - " + time);
        }

        static void AlohaPlus()
        {
            Console.WriteLine("Синхронная алоха");
            Console.WriteLine("Распределение сообщений на временной шкале (0-сообщение не отправляется данной станцией):");
            ShowStations();
            Random random = new Random();
            int collisionsCount = 0;
            while (!Check()) // пока хоть 1 станция отправлет сообщения
            {
                int came = 0; // количество подходящих под сигмент пакетов
                int index = 0; // индекс передаваемого сообщения
                int zeroCount = 0; // количество 0
                for (int i = 0; i < stCount; i++) // принимаем первые сообщения
                {
                    tempFrame[i] = stations[i].Peek(); // берем пакет кадров с каждой станции
                    if (tempFrame[i] == 1) // если пакет кадров = размеру сегмента 
                    {
                        index = i; // запомнаем индекс
                        came++; // считаем количество таких пакетов
                    }
                    else // если никакие кадры не отправляются вообще
                        zeroCount++; // если все 0
                }
                time++;
                if (zeroCount == stCount) // если сообщения не передаются
                {
                    Console.ForegroundColor = ConsoleColor.Magenta;
                    Console.WriteLine("Сообщения не отправляются\n");
                    Console.ForegroundColor = ConsoleColor.White;
                    for (int i = 0; i < stCount; i++)
                        stations[i].Dequeue(); // убираем 0 из очередей
                }
                else // если сообщения передаются
                {
                    if (came > 1) // если более 1 паркета отправлено в сегмент 
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Столкновение!\n");
                        Console.ForegroundColor = ConsoleColor.White;
                        collisionsCount++; // счётчик столкновений увеличили
                        for (int i = 0; i < stCount; i++) // генерируем время повторной отправки
                        {
                            int retry = 0;
                            foreach (int pack in stations[i]) // считаем длинну сообщений для каждой станции
                                if (pack == 1) // если пакет есть 
                                    retry++;
                                else // иначе выходим из цикла
                                    break;
                            for (int j = 0; j < random.Next(0, 4) + i - 1; j++) // вставляем сгенерированное колич. 0
                                stations[i].Enqueue(0);
                            for (int j = 0; j < retry; j++) // вставляем сообщение
                            {
                                stations[i].Dequeue();
                                stations[i].Enqueue(1);
                            }
                        }
                    }

                    if (came == 1) // если было отправлено 1 сообщение 
                    {
                        int retry = 0;
                        foreach (int pack in stations[index]) // считаем его длнну
                            if (pack == 1)
                                retry++;
                            else
                                break;

                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("Сообщение передано\n");
                        Console.ForegroundColor = ConsoleColor.White;

                        for (int j = 0; j < stCount; j++) // распределяем все сообщения
                            if (retry > 1) // если длинна сообщения > 1
                                if (j != index) // кроме отправляемого сообщения все переносятся в конец очереди
                                {
                                    int zeros = random.Next(0, 4);
                                    for (int i = 0; i < zeros; i++) // вставляем 0
                                        stations[j].Enqueue(0);

                                    for (int i = 0; i < retry; i++) // вставляем сообщение
                                        stations[j].Enqueue(stations[j].Dequeue());
                                }
                                else // отправляемое сообщение удаляем из очереди
                                    for (int i = 0; i < retry; i++)
                                        stations[j].Dequeue();
                            else // иначе просто удаляем по 1 элементу из очереди
                                stations[j].Dequeue();
                    }
                }
                ZeroAddict();
                ShowStations();
            }
            Console.WriteLine("\nКолличество коллизий - " + collisionsCount);
            Console.WriteLine("Потраченое время - " + time);
        }
    }
}
