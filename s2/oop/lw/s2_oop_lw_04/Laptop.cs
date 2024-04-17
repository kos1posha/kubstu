using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_04
{
    class Laptop : Product
    {
        public string Model;
        public string CPU;
        public string RAM;
        public Laptop(string name, double price, string model, string cpu, string ram) : base(name, price)
        {
            Model = model;
            CPU = cpu;
            RAM = ram;
        }
        public override void ShowInfo()
        {
            base.ShowInfo();
            Console.WriteLine($"Модель: {Model}" +
                              $"Процессор: {CPU}" +
                              $"Оперативная память: {RAM}");
        }
    }
}
