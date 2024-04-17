using System;
using System.Collections.Generic;

namespace s3_evm_lw_08
{
    class Program
    {
        static int stCount = 4; // количество станций
        static int packCount = 8; // количество пакетов каждой станции
        static int time = 0;
        static Random random = new Random();
        static int[] tempFrame = new int[stCount]; // массив кадров которые отправляются в данный момент
        static Queue<int>[] stations = new Queue<int>[stCount]; // массивы для списков кадров каждо станции которые будут отправлены
        static Queue<int> linkChannel = new Queue<int>();

        static void Main(string[] args)
        {
            for (int i = 0; i < stCount; i++) // гененрируем очередь каждой станции
            {
                stations[i] = new Queue<int>(); // 6 подочередей (для каждой станции)
                Genery(stations[i]); // заполняем каждую кадрами
            }
            ZeroAddict(); // дополняем 0 (для равномерного вывода)
            
            Aloha(); // запускаем чистую алоху с новым алгоритмом
        }

        static void Genery(Queue<int> station) // заполние станций кадрами для отправки
        {
            int x = 0; // счётчик сколько пакетов(кадров) добавленно на станцию
            while (x < packCount) // пока не сгенирировалась очередь с нужным количеством кадров
                if (random.Next(0, 100) > 39)
                    station.Enqueue(0); // время отправления кадра = 0 (т.е. его нет)
                else
                {
                    x++; // добавили кадр
                    station.Enqueue(1); // время сгенерировано
                }
        }
        static void ZeroAddict() // метод дополняющий 0-ми очереди
        {
            int packMaxCount = stations[0].Count;
            for (int i = 1; i < stations.Length; i++) // ищем самую длинную очередь
                if (stations[i - 1].Count < stations[i].Count)
                    packMaxCount = stations[i].Count;

            for (int i = 0; i < stations.Length; i++) // дополняем 0 очереди пока их длины не сровняются с самой длинной
                while (stations[i].Count < packMaxCount)
                    stations[i].Enqueue(0);
        }
        static bool Check() //проверка на то, что все очереди проверены от начала и до конца
        {
            foreach (Queue<int> q in stations)
                if (q.Count != 0) 
                    return false; // пока хоть 1 очередь не пуста алоха работает

            return true;
        }
        static void ShowStations() // для вывода результата работы
        {
            for (int i = 0; i < stCount; i++) // Выводим результат
                Console.WriteLine($"Станция {i}: {String.Join(" ", stations[i])}");
        }
        static void Aloha() // чистая алоха
        {
            Console.WriteLine("Распределение сообщений на временной шкале (0-сообщение не отправляется данной станцией):");
            ShowStations(); // выводим станции и очереди с кадрами
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
                    for (int i = 0; i < stCount; i++)
                        stations[i].Dequeue(); // убираем 0 из очередей
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("Нет сообщений для передачи\n");
                    Console.ForegroundColor = ConsoleColor.White;
                }
                else // если сообщения передаются
                {
                    if (came > 1) // если более 1 паркета отправлено в сегмент
                    {
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Столкновение!\n");
                        Console.ForegroundColor = ConsoleColor.White;
                        collisionsCount++; // сяётчик коллизий увеличили
                        for (int i = 0; i < stCount; i++) // генерируем время повторной отправки
                        {
                            int retry = 0;
                            foreach (int pack in stations[i]) // считаем длинну сообщений для каждой станции
                                if (pack == 1) // если пекет есть
                                    retry++;
                                else // иначе выходим из цикла
                                    break;

                            int zeros = random.Next(0, 4);
                            for (int j = 0; j < zeros + i - 1; j++) // вставляем сгенерированное колич. 0
                                stations[i].Enqueue(0);

                            for (int j = 0; j < retry; j++) // вставляем сообщение
                            {
                                stations[i].Dequeue();
                                stations[i].Enqueue(1);
                            }
                            stations[i].Dequeue();
                        }
                    }
                    if (came == 1) // если было отправлено 1 сообщение
                    {
                        int retry = 0;
                        foreach (int i in stations[index]) // считаем его длнну
                        {
                            if (i == 1)
                            {
                                retry++;
                                linkChannel.Enqueue(1);
                            }
                            else
                                break;
                        }
                        Console.WriteLine($"Канал связи {String.Join(" ", linkChannel)}");
                        Console.ForegroundColor = ConsoleColor.Green;
                        Console.WriteLine("Сообщение передано\n");
                        Console.ForegroundColor = ConsoleColor.White;
                        for (int j = 0; j < stCount; j++) // распределяем все сообщения
                        {
                            if (retry > 1) // если длинна сообщения > 1
                            {
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
                                }
                            else // иначе просто удаляем по 1 элементу из очереди
                                stations[j].Dequeue();
                        }
                    }
                }
                ZeroAddict();
                ShowStations(); // вывод очередей
                linkChannel.Clear();
            }
            Console.WriteLine("\nКолличество коллизий - " + collisionsCount);
            Console.WriteLine("Затраченое время - " + time);
        }
    }

}
