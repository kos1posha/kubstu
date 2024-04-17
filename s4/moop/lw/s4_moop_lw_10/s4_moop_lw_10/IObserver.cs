namespace s4_moop_lw_10
{
    public interface IObserver // наблюдатель
    {
        string Reaction(IObservable observable);
    }
}