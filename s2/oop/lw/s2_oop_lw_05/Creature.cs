using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Creature
    {
        protected Random Random = new Random();
        public string Name { get; }
        public double CurrentHealth { get; internal set; }
        public double MaxHealth { get; }
        internal double PoisonStacks { get; set; } = 0;
        protected bool IsInjured => CurrentHealth <= MaxHealth * 0.2;
        public Creature(string name, double maxHealth)
        {
            Name = name;
            CurrentHealth = maxHealth;
            MaxHealth = maxHealth;
        }
    }
}
