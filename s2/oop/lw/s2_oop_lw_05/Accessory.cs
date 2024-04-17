using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Accessory : Item
    {
        public Accessory() : base("Слот аксессуара") { }
        public Accessory(string name, double weight, int price, string description) : base(name, weight, price, description, null) { }
    }
}
