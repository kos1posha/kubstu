using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Hero : Creature
    {
        internal Weapon CurrentWeapon { get; private set; }
        internal Armor CurrentArmor { get; private set; }
        internal Accessory CurrentAccessory { get; private set; }
        internal string Location { get; set; }
        internal int Slots { get; set; }
        public int Gold { get; internal set; }
        public double CurrentWeight
        {
            get { double value = 0; foreach (Item item in Items) value += item.Weight; return value; }
        }
        public double MaxWeight { get; }
        public List<Item> Items { get; } = new List<Item>() { new Weapon(), new Armor(), new Accessory() };
        public Hero(string name, double maxHealth, int gold, double maxWeight, List<Item> items) : base(name, maxHealth)
        {
            Gold = gold;
            MaxWeight = maxWeight;
            Items.AddRange(items);
            Location = "wildlands";
            SetWeapon((Weapon)Items[0]); SetArmor((Armor)Items[1]); SetAccessory((Accessory)Items[2]);
        }

        public string Use(Aid aid)
        {
            if (CurrentHealth == MaxHealth) return "У вас уже полное здоровье.";
            double heal = aid.Heal;
            if (MaxHealth - CurrentHealth < aid.Heal) heal = MaxHealth - CurrentHealth;
            if (IsInjured) heal = aid.Heal * 1.5;
            CurrentHealth += heal;
            Items.Remove(aid);
            return $"Вы использовали аптечку и восстановили {heal} единиц здоровья.";
        }

        internal virtual bool CanUse(Item item) => true;

        public string SetWeapon(Weapon weapon)
        {
            if (CanUse(weapon))
            {
                CurrentWeapon = weapon;
                return $"Вы экипировали новое оружие: {CurrentWeapon.Name.ToLower()}.";
            }
            else return "Вы не умеете пользоваться этим оружием.";
        }

        public string SetArmor(Armor armor)
        {
            if (CanUse(armor))
            {
                CurrentArmor = armor;
                return $"Вы экипировали новую броню: {CurrentArmor.Name.ToLower()}.";
            }
            else return "Эта броня слишком тяжела для вас.";
        }

        public string SetAccessory(Accessory accessory)
        {
            if (CanUse(accessory))
            {
                CurrentAccessory = accessory;
                return $"Вы экипировали новый аксессуар: {CurrentAccessory.Name.ToLower()}.";
            }
            else return "Вы не умеете пользоваться этим аксессуаром.";
        }

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
}
