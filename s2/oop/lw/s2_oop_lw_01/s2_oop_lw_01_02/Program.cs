using System;
using System.Collections.Generic;

namespace s2_oop_lw_01_02
{
    class Program
    {
        static List<Phone> DataBase = new List<Phone>()
        {
            new Phone("Smasung", "Smasung A40", 284, true),
            new Phone("Pineaplle", "bPhone XS", 23, false),
            new Phone("Xlomy", "Xlomy Note 10 Pro", 893, true),
            new Phone("Yeskia", "Yeskia C20", 117, false),
            new Phone("Slava", "Slava", 1, false)
        };
        public static void ShowList()
        {
            Console.Clear();
            Console.Write("[Список имеющихся устройств]");
            if (DataBase.Count == 0) Console.WriteLine("\nСписок пуст.");
            for (int i = 0; i < DataBase.Count; i++) Console.Write($"\n{i + 1}) {DataBase[i].Model}");
        }
        public static void ShowInformation()
        {
            bool information = true;
            while (information)
            {
                Console.Write("\n\nХотите посмотреть более подробную информацию по какой-то модели? (true/false): ");
                information = Convert.ToBoolean(Console.ReadLine());
                if (information)
                {
                    Console.Write("Выберите номер утройства: ");
                    int i = Convert.ToInt32(Console.ReadLine());
                    DataBase[i - 1].ShowPhone();
                }
            }
        }
        public static Phone AddNewPhone()
        {
            Console.Clear();
            Console.WriteLine("[Добавление нового устройства]");
            Console.Write("Укажите фирму-производитель: ");
            string firm = Console.ReadLine();
            Console.Write("Укажите модель: ");
            string model = Console.ReadLine();
            Console.Write("Укажите количество на складе: ");
            int quantity = Convert.ToInt32(Console.ReadLine());
            Console.Write("Является ли Б/У? (true/false): ");
            bool secondHand = Convert.ToBoolean(Console.ReadLine());
            return new Phone(firm, model, quantity, secondHand);
        }
        public static void DeletePhone()
        {
            Console.Write("\n\nКакое устройство вы хотите удалить?: ");
            int i = Convert.ToInt32(Console.ReadLine());
            Console.Write("Вы уверены, что хотите удалить данное устройство. Это действие необратимо. (true/false): ");
            if (Convert.ToBoolean(Console.ReadLine())) DataBase.Remove(DataBase[i - 1]);
        }
        public static void EndProgram()
        {
            Console.Write("Вы уверены, что хотите закончить работу программы? При этом все изменения будут удалены, потому что я криворукий. (true/false): ");
            if (Convert.ToBoolean(Console.ReadLine())) Environment.Exit(0);
        }
        static void Main(string[] args)
        {
        Menu:
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.Write("[База данных склада мобильных устройств \"Хлеб, колбаса и гвозди\"]\n1) Просмотр списка имеющихся устройств.\n2) Добавить устройство.\n3) Удалить устройство.\n4) Очистить данные.\n5) Закончить работу программы.\n\nВвод: ");
            byte input = Convert.ToByte(Console.ReadLine());
            switch (input)
            {
                case 1:
                    {
                        ShowList();
                        if (DataBase.Count != 0) ShowInformation();
                        break;
                    }
                case 2:
                    {
                        DataBase.Add(AddNewPhone());
                        break;
                    }
                case 3:
                    {
                        ShowList();
                        if (DataBase.Count != 0) DeletePhone();
                        break;
                    }
                case 4:
                    {
                        Console.Write("\nВы уверены, что хотите удалить все данные? Это действие необратимо. (true/false): ");
                        if (Convert.ToBoolean(Console.ReadLine())) DataBase.Clear();
                        break;
                    }
                case 5:
                    {
                        EndProgram();
                        break;
                    }
            }
            Console.Write("Нажмите на любую кнопку, чтобы вернуться в меню.");
            Console.ReadKey(true);
            goto Menu;
        }
    }
}
