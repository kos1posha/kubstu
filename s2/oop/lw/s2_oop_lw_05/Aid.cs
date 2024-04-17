using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Aid : Item
    {
        internal int Heal { get; }
        public Aid(int heal) : base("Аптечка", Math.Round((heal * 0.05), 2), 0, "Эта штука хиллит", null)
        {
            Heal = heal;
            DisplayMemberName = String.Format("{0} [➕{3} 🅖{2} ⚖{1}]", Name, Weight, Price, Heal);
        }
    }
}
