using System;
using System.Collections.Generic;

namespace s2_asd_lw_07_01
{
    class Program
    {
        public static void InclusionSort(List<int> array)
        {
            for (int i = 1; i < array.Count; i++)
            {
                int value = array[i];
                int j = i;
                for (; j > 0 && array[j - 1] > value; j--)
                    array[j] = array[j - 1];
                array[j] = value;
            }
        }
        public static void InclusionSortByRC(List<Car> array)
        {
            for (int i = 1; i < array.Count; i++)
            {
                Car value = array[i];
                int j = i;
                for (; j > 0 && array[j - 1].RepairedCount > value.RepairedCount; j--)
                    array[j] = array[j - 1];
                array[j] = value;
            }
        }
        static void Main(string[] args)
        {
            Console.Write("Введите количество машин: ");
            int N = Convert.ToInt32(Console.ReadLine());
            Console.Clear();
            List<Car> carList = Car.Generator(N);
            int i = 1;
            Console.WriteLine("Все тачки:");
            foreach (Car car in carList)
            {
                Console.WriteLine($"{i++}) {car.Brand} {car.Numbers} RC:{car.RepairedCount}");
            }
            Console.WriteLine("\nСамые блатные тачки:");
            // отберем жигули
            List<Car> zhiguliList = new List<Car>();
            i = 1;
            foreach (Car car in carList)
            {
                if (car.Brand == "Жигули")
                {
                    zhiguliList.Add(car);
                    Console.WriteLine($"{i++}) {car.Brand} {car.Numbers} RC:{car.RepairedCount}");
                }
            }
            InclusionSortByRC(zhiguliList);
            Console.WriteLine("\nСамые блатные тачки, отсортированные методом прямого включения по количеству предыдущих ремонтов:");
            i = 1;
            foreach (Car zhiguli in zhiguliList)
            {
                Console.WriteLine($"{i++}) {zhiguli.Brand} {zhiguli.Numbers} RC:{zhiguli.RepairedCount}");
            }
        }
    }
}