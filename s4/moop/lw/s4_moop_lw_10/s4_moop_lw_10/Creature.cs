namespace s4_moop_lw_10
{
    public abstract class Creature
    {
        protected Location _location;
        protected Action _action;
        
        public Location Location => _location;
        public Action Action => _action;
    }
}