using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_04
{
    class Clothes : Product
    {
        public string Material;
        public string Color;
        public string Size;
        public Clothes(string name, double price, string material, string color, string size) : base(name, price)
        {
            Material = material;
            Color = color;
            Size = size;
        }
        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine($"Материал: {Material}" +
                              $"Цвет: {Color}" +
                              $"Размер: {Size}");
        }
    }
}
