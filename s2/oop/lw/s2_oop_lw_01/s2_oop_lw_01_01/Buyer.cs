using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_01_01
{
    public class Buyer
    {
        private int Id;
        static int Count = 1;
        public string Name;
        private int age;
        public int Age { get { return age; } set { if (value > 18) age = value; } }
        public string Sex;
        public string Login;
        private string Password;
        public Buyer()
        {
            Id = Count++;
            Name = "Н/Д";
            Age = 18;
            Sex = "Н/Д";
            Login = $"id{this.Id}";
            Password = null;
        }
        public Buyer(string name, int age, string sex, string login, string password)
        {
            Id = Count++;
            Name = name;
            Age = age;
            Sex = sex;
            Login = login;
            Password = password;
        }
        public static void Show(Buyer buyer)
        {
            Console.WriteLine("[Информация о клиенте]\nИдентификатор в системе: {buyer.Id}\nИмя: {buyer.Name}\nВозраст: {buyer.Age}\nПол: {buyer.Sex}\nЛогин: {buyer.Login}\nПароль: {buyer.Password}");
        }
    }
}