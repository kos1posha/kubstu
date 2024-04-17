using System;

namespace BizyaevKursach
{
    [Serializable()]
    public class User
    {
        string _login;
        string _password;

        public User(string login, string password)
        {
            _login = login;
            _password = password;
        }

        public bool Verification(string login, string password)
            => login == _login && password == _password;
    }
}
