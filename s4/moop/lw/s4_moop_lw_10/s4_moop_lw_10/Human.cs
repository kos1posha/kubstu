using System;
using System.Collections.Generic;

namespace s4_moop_lw_10
{
    public class Human: Creature, IObservable
    {
        private readonly List<IObserver> _observers;

        public Human()
        {
            _observers = new List<IObserver>();
            _location = Location.Bedroom;
            _action = Action.Sleep;
        }
        
        public bool CanIDo(Action action)
        {
            if (action == Action.Nothing || action == Action.ShakesPlasticBag || action == Action.SaysBadWords || action == Action.SaysPussPussPuss || action == Action.SaysWhoIsGoodBoy)
                return true;
            
            switch (_location)
            {
                case Location.Bedroom:
                    return action == Action.Sleep || action == Action.CleansParrotCell || action == Action.PutOnCarrotFood;
                case Location.Kitchen:
                    return action == Action.Eat || action == Action.PutOnCatFood || action == Action.PutOnDogFood;
                case Location.Bathroom:
                    return action == Action.Shit || action == Action.CleansDogSheet;
                case Location.Balcony:
                    return action == Action.Smoke || action == Action.CleansCatLitterBox;
                case Location.Hall:
                    return action == Action.PlaysOnPiano || action == Action.PlaysOnGuitar;
                default: 
                    return false;
            }
        }

        public bool CanIGo(Location location)
        {
            switch (_location)
            {
                case Location.Bedroom:
                    return location == Location.Balcony || location == Location.Hall;
                case Location.Kitchen:
                case Location.Bathroom:
                    return location == Location.Hall;
                case Location.Balcony:
                    return location == Location.Bedroom;
                case Location.Hall:
                    return location == Location.Bedroom || location == Location.Kitchen || location == Location.Bathroom;
                default:
                    return false;
            }
        }

        public string Update(Enum state)
        {
            switch (state)
            {
                case Location location:
                    if (CanIGo(location))
                    {
                        _location = location;
                        return Notify();
                    }
                    break;

                case Action action:
                    if (CanIDo(action))
                    {
                        _action = action;
                        return Notify();
                    }
                    break;
            }

            return "Ты не можешь это сделать.";
        }

        public string Notify()
        {
            string reaction = string.Empty;
            foreach (IObserver observer in _observers)
                reaction += observer.Reaction(this);
            return reaction;
        }

        public string Subscribe(IObserver observer)
        {
            _observers.Add(observer);
            return "Наблюдает за человеком";
        }
        public string Unsubscribe(IObserver observer)
        {
            _observers.Remove(observer);
            return "Перестал наблюдать за человеком";
        }
    }
}