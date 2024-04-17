using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Enemy : Creature
    {
        public int Level { get; }
        public int BaseDamage { get; }
        public double BaseResistance { get; }
        public double BaseDodge { get; }
        public int MinGold { get; }
        public int MaxGold { get; }
        public List<Item> Drop { get; }
        public Enemy(string name, double maxHealth, int level, int baseDamage, int baseResistance, int minGold, int maxGold, List<Item> drop) : base(name, maxHealth)
        {
            Level = level;
            BaseDamage = baseDamage;
            BaseResistance = baseResistance;
            MinGold = minGold;
            MaxGold = maxGold;
            Drop = drop;
        }
    }
}
