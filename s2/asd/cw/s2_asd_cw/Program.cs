using System;

namespace s2_asd_cw
{
    class Program
    {
        static string Task = "Задача \"Ханойские башни\":" +
                             "\nЕсть 3 башни, на первой из которых расположено N-ное количество колец, причем кольца расположены  в порядке убывания от основания башни." +
                             "\nРазрешено переставлять по одному кольцу за ход, причем запрещено должна сохраняться упорядоченность колец башен." +
                             "\nЧтобы решить задачу, нужно переложить все диски с левой башни на правую. (центральная башня решением не считается)";
        static void Update(HanoiTask hanoiTask)
        {
            Console.ReadKey(true);
            Console.Clear();
            hanoiTask.View();
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Task);
        start:
            Console.Write("Введите высоту башни: ");
            int hanoiHeight = Convert.ToInt32(Console.ReadLine());
            Console.Write("Решишь капчу? (true/false): ");
            HanoiTask hanoiTask = new HanoiTask(hanoiHeight, Convert.ToBoolean(Console.ReadLine()));
            while (!hanoiTask.Done)
            {
            Turn:
                if (hanoiTask.Turn == 254)
                    Console.WriteLine();
                Update(hanoiTask);
                Console.WriteLine("\nХод: " + hanoiTask.Turn);
                if (hanoiTask.Mode)
                {
                    Console.Write("Перемещение: ");
                    switch (hanoiTask.Replace(Console.ReadLine()))
                    {
                        case -2: Console.WriteLine("Нельзя перекладывать кольца больших размеров на кольца меньших."); goto Turn;
                        case -1: Console.WriteLine("Выбранная башня пуста."); goto Turn;
                        case 0: Console.WriteLine("Неверный формат перемещния."); goto Turn;
                    }
                }
                else
                {
                    if (hanoiHeight % 2 == 0)
                        switch (hanoiTask.Turn % 3)
                        {
                            case 1: hanoiTask.Replace("12"); break;
                            case 2: hanoiTask.Replace("13"); break;
                            case 0: hanoiTask.Replace("23"); break;
                        }
                    else
                        switch (hanoiTask.Turn % 3)
                        {
                            case 1: hanoiTask.Replace("13"); break;
                            case 2: hanoiTask.Replace("12"); break;
                            case 0: hanoiTask.Replace("23"); break;
                        }
                }
                hanoiTask.Turn++;
            }
            Update(hanoiTask);
            Console.WriteLine("\nКоличество перемещений, за которое была решена задача: " + (hanoiTask.Turn - 1));
            Console.WriteLine();
            goto start;
        }
    }
}
