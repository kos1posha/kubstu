using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Forms;

namespace BizyaevKursach
{
    [Serializable()]
    static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);


            try
            {
                using (FileStream fileStream = new FileStream("save.dat", FileMode.Open))
                {
                    BinaryFormatter binaryFormatter = new BinaryFormatter();
                    Save save = (Save)binaryFormatter.Deserialize(fileStream);
                    InactiveOrders = save.InactiveOrders;
                    Couriers = save.Couriers;
                    Curators = save.Curators;
                    CurrentCourier = null;
                }
            }
            catch
            {
                InactiveOrders = new List<Order>();
                Couriers = new List<Courier>()
                {
                new Courier("login", "password", "Котов Леха Дмитриевич", "9897872543", new DateTime(2018, 5, 27)),
                new Courier("slava", "slava", "Бизяев Вячеслав", "9180739415", new DateTime(2018, 5, 27)),
                new Courier("g2rek", "6390", "Параскевопулос Владимир Ктотытам", "9183577089", new DateTime(2018, 5, 27)),
                new Courier("jinh", "4444", "Бог любит четверку", "4444444444", new DateTime(2018, 5, 27))
                };
                Curators = new List<Curator>()
                {
                    new Curator("log", "pass"),
                    new Curator("root", "12345qwerty")
                };
            }

            Application.Run(new LoginForm());
        }

        public static string GetDate(DateTime dateTime) => $"{dateTime.Day}.{dateTime.Month}.{dateTime.Year}";
        
        public static MainForm MainForm { get; set; }
        public static List<Order> InactiveOrders { get; set; }
        public static List<Curator> Curators { get; set; }
        public static List<Courier> Couriers { get; set; }
        public static Courier CurrentCourier { get; set; }
    }
}
