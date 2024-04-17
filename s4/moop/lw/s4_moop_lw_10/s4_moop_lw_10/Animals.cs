using System;

namespace s4_moop_lw_10
{
    public class Cat : Creature, IObserver
    {
        public Cat()
        {
            _location = Location.Hall;
            _action = Action.Sleep;
        }
        
        public string Reaction(IObservable observable)
        {
            Human human = observable as Human ?? throw new InvalidCastException();
            Action action = human.Action;
            Location location = human.Location;
            switch (action)
            {
                case Action.Nothing: _action = Action.Nothing; return "1 Чувствует единение со своим человеком от факта совместного ничегонеделания.\n";
                case Action.Sleep: _action = Action.SaysBadWords; _location = Location.Balcony; return "1 Пользуется случаем, чтобы обматерить уличных котов.\n";
                case Action.Shit: _action = Action.Nothing; _location = Location.Hall; return "1 Тихо слушает.\n";
                case Action.Eat: _action = Action.Nothing; _location = Location.Kitchen; return "1 Тихо смотрит.\n";
                case Action.Smoke: _action = Action.Nothing; _location = Location.Balcony; return "1 Пришел думать с человеком о смысле жизни.\n";
                case Action.ShakesPlasticBag: _action = Action.Sleep; return "1 Знает, что это уловка, так что не реагирует.\n";
                case Action.SaysPussPussPuss: _action = Action.Nothing; _location = location; return "1 - Мяу-мяу.\n";
                case Action.SaysWhoIsGoodBoy: _action = Action.Sleep; return "1 - Это к блохастому.\n";
                case Action.SaysBadWords: _action = Action.Sleep; return "1 ...\n";
                case Action.CleansCatLitterBox: _action = Action.Shit; _location = Location.Bathroom; return "1 - Делай свою работу, человек.\n";
                case Action.CleansDogSheet: _action = Action.Nothing; return "1 - Гадость.\n";
                case Action.CleansParrotCell: _action = Action.Nothing; _location = location; return "1 - Однажды ты забудешь закрыть клетку, и я съем попугая\n";
                case Action.PutOnCatFood: _action = Action.Eat; _location = Location.Kitchen; return "1 Делает единственную не ненавистную ему вещь.\n";
                case Action.PutOnDogFood: _action = Action.Nothing; return "1 - Гадость.\n";
                case Action.PutOnCarrotFood: _action = Action.Nothing; _location = Location.Bedroom; return "1 - И зачем кормить корм?\n";
                case Action.PlaysOnPiano: _action = Action.Sleep; _location = Location.Hall; return "1 Умиротворение.\n";
                case Action.PlaysOnGuitar: _action = Action.Sleep; _location = Location.Hall; return "1 Умиротворение.\n";
                default: return string.Empty;
            }
        }
    }

    public class Dog : Creature, IObserver
    {
        public Dog()
        {
            _location = Location.Kitchen;
            _action = Action.Eat;
        }
        
        public string Reaction(IObservable observable)
        {
            Human human = observable as Human ?? throw new InvalidCastException();
            Action action = human.Action;
            Location location = human.Location;
            switch (action)
            {
                case Action.Nothing: _action = Action.Nothing; return $"2 Скучает.\n";
                case Action.Sleep: _action = Action.Nothing; _location = Location.Balcony; return $"2 - А гулять когда?\n";
                case Action.Shit: _action = Action.Nothing; _location = Location.Hall; return $"2 Смотрит в окно.\n";
                case Action.Eat: _action = Action.Eat; _location = Location.Kitchen; return $"2 Подъедает кинутую ей еду.\n";
                case Action.Smoke: _action = Action.Sleep; return $"2 Снится, что он собака-пожарный.\n";
                case Action.ShakesPlasticBag: _action = Action.Nothing; _location = location; return $"2 - Звук еды? Где звук еды? \n";
                case Action.SaysPussPussPuss: _action = Action.Sleep; return $"2 ...\n";
                case Action.SaysWhoIsGoodBoy: _action = Action.Nothing; _location = location; return $"2 - Я хороший мальчик!!! Я! Я!\n";
                case Action.SaysBadWords: _action = Action.Nothing; _location = location; return $"2 - Что случилось? Почему человек злой?\n";
                case Action.CleansCatLitterBox: _action = Action.Sleep; return $"2 ...\n";
                case Action.CleansDogSheet: _action = Action.Shit; return $"2 Испражняется.\n";
                case Action.CleansParrotCell: _action = Action.Sleep; return $"2 ...\n";
                case Action.PutOnCatFood: _action = Action.Nothing; _location = Location.Kitchen; return $"2 - А мне? Я тоже хочу.\n";
                case Action.PutOnDogFood: _action = Action.Eat; _location = Location.Kitchen; return $"2 ОАОАОАОАОАОАОАОАОАОАОАОАОАОА\n";
                case Action.PutOnCarrotFood: _action = Action.Sleep; return $"2 ...\n";
                case Action.PlaysOnPiano: _action = Action.Nothing; _location = Location.Hall; return $"2 Любит человека.\n";
                case Action.PlaysOnGuitar: _action = Action.Nothing; _location = Location.Hall; return $"2 Любит человека.\n";
                default: return string.Empty;
            }
        }
    }

    public class Carrot : Creature, IObserver
    {
        public Carrot()
        {
            _location = Location.Bedroom;
            _action = Action.Nothing;
        }
        
        public string Reaction(IObservable observable)
        {
            Human human = observable as Human ?? throw new InvalidCastException();
            Action action = human.Action;
            Location location = human.Location;
            switch (action)
            {
                case Action.Nothing: _action = Action.SaysBadWords; return $"3 ...\n";
                case Action.Sleep: _action = Action.SaysBadWords; return $"3 - Ругается на спящего человека.\n";
                case Action.Shit: _action = Action.SaysBadWords; return $"3 ...\n";
                case Action.Eat: _action = Action.SaysBadWords; return $"3 - Подавись\n";
                case Action.Smoke: _action = Action.Nothing; return $"3 Делает вид, что задыхается.\n";
                case Action.ShakesPlasticBag: _action = Action.SaysBadWords; return $"3 - Шумный. Шумный. Шумный.\n";
                case Action.SaysPussPussPuss: _action = Action.SaysBadWords; return $"3 - Усатый глупый.\n";
                case Action.SaysWhoIsGoodBoy: _action = Action.SaysBadWords; return $"3 - Хвостатый глупый.\n";
                case Action.SaysBadWords: _action = Action.SaysBadWords; return $"3 - **** ******, **** твою ****.\n";
                case Action.CleansCatLitterBox: _action = Action.Sleep; return $"3 ...\n";
                case Action.CleansDogSheet: _action = Action.Sleep; return $"3 \n";
                case Action.CleansParrotCell: _action = Action.Nothing; return $"3 Чувствует превосходство над человеком.\n";
                case Action.PutOnCatFood: _action = Action.SaysBadWords; return $"3 - Подавись.\n";
                case Action.PutOnDogFood: _action = Action.SaysBadWords; return $"3 - Подавись.\n";
                case Action.PutOnCarrotFood: _action = Action.Eat; return $"3 - Ну и стрепня.\n";
                case Action.PlaysOnPiano: _action = Action.SaysBadWords; return $"3 Поет матерные песни.\n";
                case Action.PlaysOnGuitar: _action = Action.SaysBadWords; return $"3 Поет матерные песни.\n";
                default: return string.Empty;
            }
        }
    }
}
