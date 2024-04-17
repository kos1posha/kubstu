using System;

namespace BizyaevKursach
{
    [Serializable()]
    public class Curator : User
    {
        public Curator(string login, string password)
            :base(login, password)
        {

        }
    }
}
