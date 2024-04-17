using System;
using System.Collections.Generic;

namespace s2_oop_lw_03
{
    class Product
    {
        public static List<Product> Cart = new List<Product>();
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
        public void AddToCart(Product product)
        {
            Cart.Add(product);
        }

        public double TotalPrice()
        {
            double totalPrice = 0;
            for (int i = 0; i < Cart.Count; i++)
                totalPrice += Cart[i].Price;
            return totalPrice;
        }
        public virtual void ShowInfo(Product product)
        {
            Console.WriteLine($"Идентификатор: {Id}\n" +
                              $"Название: {Name}\n" +
                              $"Цена: {Price}\n");
        }
    }
}

