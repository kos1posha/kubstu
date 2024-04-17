using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_07_01
{
    class Car
    {
        public string Numbers { get; private set; }
        public string Brand { get; private set; }
        public string OwnerName { get; private set; }
        public int RepairedCount { get; private set; }
        public DateTime? LastRepairDate { get; private set; }
        public DateTime RepairedDate { get; private set; }
        public Car()
        { }
        public Car(string numbers, string brand, string ownerName, int repairedCount, DateTime? lastRepairDate, DateTime repairedDate)
        {
            Numbers = numbers;
            Brand = brand;
            OwnerName = ownerName;
            RepairedCount = repairedCount;
            LastRepairDate = lastRepairDate;
            RepairedDate = repairedDate;
        }
        public static List<Car> Generator(int N)
        {
            List<Car> carList = new List<Car>();
            Random random = new Random();
            string[] brands = new string[]
            {
                "Жигули", "Мерседес", "Порше", "Газель", "Лада", "Датсун", "Тойота", "БМВ", "Хендай", "Даеву", "Тесла", "Лексус"
            };
            string[] ownerFirstNames = new string[]
            {
                "Стас ", "Гена ", "Слава ", "Руслан ", "Антон ", "Денис ", "Андрей ", "Максим ", "Богдан ", "Сурик ", "Матвей ", "Влад "
            };
            string[] ownerLastNames = new string[]
            {
                "Комаров", "Пикалюк", "Доценко", "Павлов", "Параскевопулос", "Пахин", "Терешков", "Ктохин", "Балабайко", "Стасюк", "Питкин", "Иванов"
            };
            string russian = "АВЕКМНОРСТУХ";
            for (int i = 0; i < N; i++)
            {
                DateTime? lastRepairDate = null;
                int repairCount = random.Next(7);
                if (repairCount != 0) lastRepairDate = new DateTime(random.Next(2012, 2022), random.Next(1, 12), random.Next(1, 29));
                carList.Add(
                    new Car(
                    russian[random.Next(12)] + random.Next(100, 1000).ToString() + russian[random.Next(12)] + russian[random.Next(12)],
                    brands[random.Next(brands.Length)],
                    ownerFirstNames[random.Next(12)] + ownerLastNames[random.Next(12)],
                    random.Next(7),
                    lastRepairDate,
                    new DateTime(2022, random.Next(1, 12), random.Next(1, 29))));
            }
            return carList;
        }
    }
}
