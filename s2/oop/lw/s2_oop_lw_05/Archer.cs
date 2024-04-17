using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Archer : Hero, IWarrior
    {
        new internal Bow CurrentWeapon { get; private set; }
        new internal Arrowheads CurrentAccessory { get; private set; }
        public Archer(string name, int gold, List<Item> items) : base(name, 100, gold - 50, 25, items)
        { Slots = 3; SetWeapon((Weapon)Items[0]); SetArmor((Armor)Items[1]); }
        internal override bool CanUse(Item item) =>
            item.Name.Contains("Слот") || item is Bow || item is Arrowheads || item is HeavyArmor || item is LightArmor;
        public string Attack(Enemy enemy)
        {
            double damage = Math.Round(Random.Next(CurrentWeapon.MinDamage, CurrentWeapon.MaxDamage) + Random.NextDouble(), 2);
            bool isCritHit = Random.NextDouble() <= CurrentWeapon.CritChance;
            double totalResistance = 1 - enemy.BaseResistance + CurrentWeapon.IgnoreResistance >= 1 ? 1 : 1 - enemy.BaseResistance + CurrentWeapon.IgnoreResistance;
            if (isCritHit) damage *= CurrentWeapon.CritDamage;
            else damage *= totalResistance;
            enemy.CurrentHealth -= damage;
            return $"{isCritHit}/{damage}";
        }
    }
}
