using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_04
{
    abstract class Product
    {
        private static int Count = 1;
        public int Id;
        public string Name;
        public double Price;
        public Product(string name, double price)
        {
            Id = Count++;
            Name = name;
            Price = price;
        }
        public virtual void ShowInfo()
        {
            Console.WriteLine($"Идентификатор: {Id}\n" +
                              $"Название: {Name}\n" +
                              $"Цена: {Price}\n");
        }
    }
}
