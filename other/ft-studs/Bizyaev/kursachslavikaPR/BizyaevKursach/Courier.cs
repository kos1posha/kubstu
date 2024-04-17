using System;
using System.Collections.Generic;
using System.Drawing;

namespace BizyaevKursach
{
    [Serializable()]
    public class Courier : User
    {
        int _counter = 1000;

        public string Id { get; set; }
        public string Name { get; set; }
        public string TelephoneNumber { get; set; }
        public List<Order> HiddenOrders { get; set; }
        public List<Order> ActiveOrders { get; set; }
        public List<Order> OrdersHistory { get; set; }
        public List<OrderSize> CanDeliveryList { get; set; }
        public DateTime RegistrationDate { get; set; }
        public Image Photo { get; set; }

        public Courier(string login, string password, string name, string telephoneNumber, DateTime registrationDate)
            :base(login, password)
        {
            Id = (++_counter).ToString();
            Name = name;
            TelephoneNumber = telephoneNumber;
            HiddenOrders = new List<Order>();
            ActiveOrders = new List<Order>();
            OrdersHistory = new List<Order>();
            CanDeliveryList = new List<OrderSize>();
            RegistrationDate = registrationDate;
        }

        public bool CanDelivery(Order order)
        {
            if (CanDeliveryList.Contains(order.Size))
                return true;
            return false;
        }

        public string GetCanDeliveryString()
        {
            if (CanDeliveryList.Count == 6)
                return "все могу :)";
            if (CanDeliveryList.Count == 0)
                    return "ничего не могу :(";

            string value = string.Empty;

            foreach (OrderSize size in CanDeliveryList)
                switch (size)
                {
                    case OrderSize.VerySmall:
                        value += "очень маленький, ";
                        break;
                    case OrderSize.Small:
                        value += "маленький, ";
                        break;
                    case OrderSize.Average:
                        value += "средний, ";
                        break;
                    case OrderSize.Large:
                        value += "большой, ";
                        break;
                    case OrderSize.VeryLarge:
                        value += "очень большой, ";
                        break;
                    case OrderSize.ExtraLarge:
                        value += "огромный, ";
                        break;
                }

            return value.Remove(value.Length - 2, 1) + "заказ" + (CanDeliveryList.Count > 1 ? "ы" : "");
        }
    }
}
