using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class LightArmor : Armor
    {
        internal double Dodge { get; }
        public LightArmor(string name, double weight, int price, string description, double resistance) : base(name, weight, price, description, resistance)
        {
            DisplayMemberName = String.Format("{0} [🛡{3} 🅖{2} ⚖{1}]", Name, Weight, Price, Resistance * 100);
        }
    }
}
