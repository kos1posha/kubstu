using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Arrowheads : Accessory
    {
        internal double Damage { get; }
        public Arrowheads(string name, double weight, int price, string description, double damage) : base(name, weight, price, description)
        {
            Damage = damage;
            DisplayMemberName = String.Format("{0} [🏹{3} 🅖{2} ⚖{1}]", Name, Weight, Price, Damage);
        }
    }
}
