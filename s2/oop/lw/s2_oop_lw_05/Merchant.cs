using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    class Merchant : Creature, IMerchant
    {
        public List<Item> Assortment;
        public Merchant(string name, List<Item> assortment) : base(name, 1)
        {
            Assortment = assortment;
        }
        public string Buy(Hero hero, Item item)
        {
            hero.Items.Remove(item);
            hero.Gold += (int)(0.5 * item.Price);
            return $"Вы продали {item.Name} за {0.5 * item.Price} золотых.";
        }
        public string Sell(Hero hero, Item item)
        {
            if (hero.CurrentWeight + item.Weight > hero.MaxWeight)
                return "У вас недостаточно места в инветаре.";
            if (hero.Gold - item.Price < 0)
                return "У вас недостаточно денег.";
            hero.Items.Add(item);
            hero.Gold -= item.Price;
            return $"Вы купили {item.Name} за  {item.Price} золотых.";
        }
    }
}
