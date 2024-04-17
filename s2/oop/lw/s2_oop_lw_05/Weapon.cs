using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Weapon : Item
    {
        internal int MinDamage { get; }
        internal int MaxDamage { get; }
        internal double CritChance { get; }
        internal double CritDamage { get; }
        public Weapon() : base("Слот оружия") { }
        public Weapon(string name, double weight, int price, string description, string displayMemberName, int minDamage, int maxDamage, double critChance, double critDamage)
            : base(name, weight, price, description, displayMemberName)
        {
            MinDamage = minDamage;
            MaxDamage = maxDamage;
            CritChance = critChance;
            CritDamage = critDamage;
        }
    }
}
