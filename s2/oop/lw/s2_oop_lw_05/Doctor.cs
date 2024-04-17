using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    class Doctor : Merchant, IDoctor
    {
        public int HealCost;
        public Doctor(string name, List<Item> assortment, int healCost) : base(name, assortment)
        {
            HealCost = healCost;
        }
        public string Heal(Hero hero)
        {
            if (hero.Gold - HealCost < 0)
                return "У вас недостаточно денег.";
            hero.Gold -= HealCost;
            hero.CurrentHealth = hero.MaxHealth;
            return $"Клирик восстановил ваше здоровье за {HealCost} золотых.";
        }
    }
}
