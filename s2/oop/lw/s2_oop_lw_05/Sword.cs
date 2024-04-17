using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Sword : Weapon
    {
        public Sword(string name, double weight, int price, string description, int minDamage, int maxDamage, double critChance, double critDamage)
            : base(name, weight, price, description, null, minDamage, maxDamage, critChance, critDamage)
        {
            DisplayMemberName = String.Format("{0} [⚔{3}-{4} 💢{5}% 💥{6}% 🅖{2} ⚖{1}]", Name, Weight, Price, MinDamage, MaxDamage, CritChance * 100, CritDamage * 100);
        }
    }
}
