using System;
using System.Collections.Generic;
using System.Text;

namespace s2_oop_lw_06_01
{
    class Order
    {
        public string Name;
        public int ProductPrice;
        public int DeliveryPrice;
        public int Weight;
        public Order(string name, int productPrice, int deliveryPrice, int weight)
        {
            Name = name;
            ProductPrice = productPrice;
            DeliveryPrice = deliveryPrice;
            Weight = weight;
        }
        public static bool operator >(Order arg1, Order arg2) => arg1.Weight > arg2.Weight;
        public static bool operator <(Order arg1, Order arg2) => arg1.Weight < arg2.Weight;
        public static bool operator >=(Order arg1, Order arg2) => arg1.Weight >= arg2.Weight;
        public static bool operator <=(Order arg1, Order arg2) => arg1.Weight <= arg2.Weight;
        public static Order operator +(Order arg1, Order arg2) => new Order($"{arg1.Name}, {arg2.Name}", arg1.ProductPrice + arg2.ProductPrice, Math.Max(arg1.DeliveryPrice, arg2.DeliveryPrice), arg1.Weight + arg2.Weight);
        public static implicit operator double(Order arg) => arg.ProductPrice + arg.DeliveryPrice;
    }
}
