using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Rogue : Hero, IWarrior
    {
        new internal Dagger CurrentWeapon { get; private set; }
        new internal Lubricant CurrentAccessory { get; private set; }
        public Rogue(string name, int gold, List<Item> items) : base(name, 80, gold + 100, 20, items)
        { Slots = 3; SetWeapon((Weapon)Items[0]); SetArmor((Armor)Items[1]); }
        internal override bool CanUse(Item item) =>
            item.Name.Contains("Слот") || item is Dagger || item is Lubricant || item is LightArmor;
        public string Attack(Enemy enemy)
        {
            double damage = Math.Round(Random.Next(CurrentWeapon.MinDamage, CurrentWeapon.MaxDamage) + Random.NextDouble(), 2);
            bool isCritHit = Random.NextDouble() <= CurrentWeapon.CritChance;
            if (isCritHit) enemy.CurrentHealth -= damage * CurrentWeapon.CritDamage;
            else damage *= 1 - enemy.BaseResistance;
            enemy.CurrentHealth -= damage;
            enemy.PoisonStacks += CurrentWeapon.PoisonDamage;
            return $"{isCritHit}/{damage}";
        }
    }
}
