using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_01_02
{
    class Phone
    {
        public string Firm;
        public string Model;
        public int Quantity;
        public bool SecondHand;
        public Phone(string firm, string model, int quantity, bool secondHand)
        {
            this.Firm = firm;
            this.Model = model;
            this.Quantity = quantity;
            this.SecondHand = secondHand;
        }
        public void ShowPhone()
        {
            Console.Write("\n[Информация о данном устройстве]" +
                             $"\nФирма-производитель: {Firm}" +
                             $"\nМодель: {Model}" +
                             $"\nКоличество на складе: {Quantity}" +
                             $"\nБ/У: {SecondHand}");
        }
    }
}
