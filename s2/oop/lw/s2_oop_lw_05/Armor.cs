using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Armor : Item
    {
        internal double Resistance { get; }
        public Armor() : base("Слот брони") { }
        public Armor(string name, double weight, int price, string description, double resistance) : base(name, weight, price, description, null)
        {
            Resistance = resistance;
        }
    }
}
