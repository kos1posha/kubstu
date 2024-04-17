using System;

namespace s4_moop_lw_10
{
    internal static class Program 
    {
        static readonly Enum[] states = { 
            Location.Bedroom,
            Location.Kitchen,
            Location.Bathroom,
            Location.Balcony,
            Location.Hall, 
            Action.Nothing,
            Action.Sleep,
            Action.Shit,
            Action.Eat,
            Action.Smoke,
            Action.ShakesPlasticBag,
            Action.SaysPussPussPuss,
            Action.SaysWhoIsGoodBoy,
            Action.SaysBadWords,
            Action.CleansCatLitterBox,
            Action.CleansDogSheet,
            Action.CleansParrotCell,
            Action.PutOnCatFood,
            Action.PutOnDogFood,
            Action.PutOnCarrotFood,
            Action.PlaysOnPiano,
            Action.PlaysOnGuitar
        };
        
        public static void Main(string[] args)
        {
            Human human = new Human();
            Cat cat = new Cat();
            Dog dog = new Dog();
            Carrot carrot = new Carrot();

            string logs = string.Empty;
            string head =
                "1) Bedroom\n2) Kitchen\n3) Bathroom\n4) Balcony\n5) Hall\n6) Nothing\n7) Sleep\n8) Shit\n9) Eat\n" +
                "10) Smoke\n11) ShakesPlasticBag\n12) SaysPussPussPuss\n13) SaysWhoIsGoodBoy\n14) SaysBadWords\n" +
                "15) CleansCatLitterBox\n16) CleansDogSheet\n17) CleansParrotCell\n18) PutOnCatFood\n19) PutOnDogFood\n" +
                "20) PutOnCarrotFood\n21) PlaysOnPiano\n22) PlaysOnGuitar\n23) Подписать кота\n24) Отписать кота\n" +
                "25) Подписать собаку\n26) Отписать собаку\n27) Подписать попугая\n28) Отписать попугая\n" +
                "Выберите действие:";
            
            while (true)
            {
                Console.Write(head);
                int i = Convert.ToInt32(Console.ReadLine());

                if (i == -1)
                    return;
                if (i < states.Length - 6)
                    logs += human.Update(states[i - 1]);
                else
                {
                    switch (i)
                    {
                        case 23:
                            logs += "Кот подписан.\n";
                            human.Subscribe(cat);
                            break;
                        case 24:
                            logs += "Кот отписан.\n";
                            human.Unsubscribe(cat);
                            break;
                        case 25: 
                            logs += "Собака подписана.\n";
                            human.Subscribe(dog);
                            break;
                        case 26: 
                            logs += "Собака отписана.\n";
                            human.Unsubscribe(dog);
                            break;
                        case 27: 
                            logs += "Попугай подписан.\n";
                            human.Subscribe(carrot);
                            break;
                        case 28: 
                            logs += "Попугай отписан.\n";
                            human.Unsubscribe(carrot);
                            break;
                        default:
                            Console.WriteLine("Мимо, чел...\n");
                            break;
                    }
                }
                
                Console.WriteLine(logs);
                Console.ReadKey(true);
                Console.Clear();
            }
        }
    }
}