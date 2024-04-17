using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    interface IWarrior
    {
        string Attack(Enemy enemy);
    }

    interface IMerchant
    {
        string Buy(Hero hero, Item item);
        string Sell(Hero hero, Item item);
    }

    interface IDoctor
    {
        string Heal(Hero hero);
    }

    interface IWeapon
    {
        int GetDamage(Hero hero, Creature creature);
    }
}
