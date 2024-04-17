using System;

namespace s2_oop_lw_06_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Ingredient Mushroom = new Ingredient("Мухомор", "Отравление", 5);
            Ingredient Candy = new Ingredient("Конфета", "Кариес", 40);
            Ingredient Plant = new Ingredient("Цветок", "Восстановление здоровья", 25);
            Ingredient Cheese = new Ingredient("Сыр", "Восстановление маны", 50);
            Ingredient Water = new Ingredient("Вода", "Восстановление выносливости", 20);
            Ingredient Potion = Cheese + Candy;
            Console.WriteLine($"{Potion.Effect}\n{Potion.Price}");
        }
    }
}
