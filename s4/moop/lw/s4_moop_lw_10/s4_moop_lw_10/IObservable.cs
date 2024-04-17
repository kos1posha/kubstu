using System;

namespace s4_moop_lw_10
{
    public interface IObservable // наблюдаемый
    {
        string Update(Enum state);
        string Notify();
        
        string Subscribe(IObserver observer);
        string Unsubscribe(IObserver observer);
    }
}