using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_03
{
    class Clothes : Product
    {
        public string Material;
        public string Color;
        public string Size;
        public bool Print;
        public Clothes(string name, double price, string material, string color, string size, bool print) : base(name, price)
        {
            Material = material;
            Color = color;
            Size = size;
            Print = print;
        }
        public override void ShowInfo(Product product)
        {
            base.ShowInfo(product);
            Console.WriteLine($"Материал: {Material}" +
                              $"Цвет: {Color}" +
                              $"Размер: {Size}" +
                              $"Принт: {Print}");
        }
    }
}
