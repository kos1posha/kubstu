using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_05
{
    public class Item
    {
        public string Name { get; }
        public double Weight { get; }
        public int Price { get; }
        public string Description { get; }
        public string DisplayMemberName { get; internal set; }
        public Item(string name)
        {
            Name = name;
            DisplayMemberName = name;
            Weight = 0;
            Price = 0;
            Description = "";
        }
        public Item(string name, double weight, int price, string description, string displayMemberName)
        {
            Name = name;
            Weight = weight;
            Price = price;
            Description = description;
            DisplayMemberName = displayMemberName;
        }
    }
}
