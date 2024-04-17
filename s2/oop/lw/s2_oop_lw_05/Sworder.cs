using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Sworder : Hero, IWarrior
    {
        new internal Sword CurrentWeapon { get; private set; }
        new internal Shield CurrentAccessory { get; private set; }
        public Sworder(string name, int gold, List<Item> items) : base(name, 120, gold, 30, items)

        { Slots = 3; }
        internal override bool CanUse(Item item) =>
            item.Name.Contains("Слот") || item is Sword || item is Shield || item is HeavyArmor;
        public string Attack(Enemy enemy)
        {
            if (enemy.BaseDodge <= Random.NextDouble()) return "-1";
            double damage = Math.Round(Random.Next(CurrentWeapon.MinDamage, CurrentWeapon.MaxDamage) + Random.NextDouble(), 2);
            bool isCritHit = Random.NextDouble() <= CurrentWeapon.CritChance;
            if (isCritHit) damage *= CurrentWeapon.CritDamage * (1 - enemy.BaseResistance);
            else damage *= 1 - enemy.BaseResistance;
            enemy.CurrentHealth -= damage;
            return $"{isCritHit}/{damage}";
        }
    }
}
