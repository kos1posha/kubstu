using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_06_02
{
    class Ingredient
    {
        public string Name;
        public string Effect;
        public int Price;
        public static Dictionary<string, string> Recipes = new Dictionary<string, string>()
        {
            { "МухоморКонфета", "Мгновенная смерть" },
            { "МухоморЦветок", "Лечение отравления" },
            { "МухоморСыр", "Немота" },
            { "МухоморВода", "Сильное отравление" },
            { "КонфетаЦветок", "Лечение кариеса" },
            { "КонфетаСыр", "Просто вкусное зелье" },
            { "КонфетаВода", "Разъедание желудка" },
            { "ЦветокСыр", "Увеличение магического сопротивления" },
            { "ЦветокВода", "Временно увеличивает переносимый вес" },
            { "СырВода", "Уменьшение магического сопротивления" }
        };
        public Ingredient(string name, string effect, int price)
        {
            Name = name;
            Effect = effect;
            Price = price;
        }
        public static Ingredient operator +(Ingredient ing1, Ingredient ing2)
        {
            string effect;
            if (Recipes.ContainsKey(ing1.Name + ing2.Name)) effect = Recipes[ing1.Name + ing2.Name];
            else effect = Recipes[ing2.Name + ing1.Name];
            return new Ingredient("Зелье", effect, (ing1.Price + ing2.Price) * 3);
        }
    }
}
