using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Lubricant : Accessory
    {
        internal double PoisonDamage { get; }
        public Lubricant(string name, double weight, int price, string description, double poisonDamage) : base(name, weight, price, description)
        {
            PoisonDamage = poisonDamage;
            DisplayMemberName = String.Format("{0} [💧{3} 🅖{2} ⚖{1}]", Name, Weight, Price, PoisonDamage);
        }
    }
}
