using System;

namespace BizyaevKursach
{
    [Serializable()]
    public class Order
    {
        static int counter = 0;

        public int Number { get; }
        public decimal Cost { get; }
        public decimal Surcharge { get; }
        public string ReceivingAddress { get; }
        public string DeliveryAddress { get; }
        public string SenderFirm { get; }
        public string ReceiverName { get; }
        public string Note { get; set; }
        public decimal Weight { get; }
        public OrderSize Size { get; }
        public OrderStatus Status { get; set; }
        public OrderPaymentMethod PaymentMethod { get; }
        public DateTime FormationTime { get; }
        public DateTime RequestedDeliveryTime { get; }
        public DateTime ActualDeliveryTime { get; set; }

        public Order(decimal cost, string receivingAddress, string deliveryAddress, string senderFirm, string receiverName, decimal weight, OrderPaymentMethod paymentMethod, DateTime formationTime, DateTime requestedDeliveryTime)
        {
            Number = ++counter;
            Cost = cost;
            ReceivingAddress = receivingAddress;
            DeliveryAddress = deliveryAddress;
            SenderFirm = senderFirm;
            ReceiverName = receiverName;
            Note = string.Empty;

            Weight = weight;
            if (weight > 70)
            {
                throw new ArgumentException("Нельзя взять заказ весом больше 60 кг");
            }
            else if (weight > 40)
            {
                Surcharge = 8000 + cost * 0.01m;
                Size = OrderSize.ExtraLarge;
            }
            else if (weight > 20)
            {
                Surcharge = 4000 + cost * 0.01m;
                Size = OrderSize.VeryLarge;
            }
            else if (weight > 10)
            {
                Surcharge = 1600 + cost * 0.01m;
                Size = OrderSize.Large;
            }
            else if (weight > 5)
            {
                Surcharge = 800 + cost * 0.01m;
                Size = OrderSize.Average;
            }
            else if (weight > 2)
            {
                Surcharge = 400 + cost * 0.01m;
                Size = OrderSize.Small;
            }
            else
            {
                Surcharge = 200 + cost * 0.01m;
                Size = OrderSize.VerySmall;
            }

            PaymentMethod = paymentMethod;
            FormationTime = formationTime;
            RequestedDeliveryTime = requestedDeliveryTime;
        }
        public Order(decimal cost, string receivingAddress, string deliveryAddress, string senderFirm, string receiverName, string note, decimal weight, OrderPaymentMethod paymentMethod, DateTime formationTime, DateTime requestedDeliveryTime)
            : this(cost, receivingAddress, deliveryAddress, senderFirm, receiverName, weight, paymentMethod, formationTime, requestedDeliveryTime)
        {
            Note = note;
        }

        public static int GetCount() => counter;
        public string GetSize()
        {
            switch (Size)
            {
                case OrderSize.VerySmall:
                    return "очень маленький";
                case OrderSize.Small:
                    return "маленький";
                case OrderSize.Average:
                    return "средний";
                case OrderSize.Large:
                    return "большой";
                case OrderSize.VeryLarge:
                    return "очень большой";
                case OrderSize.ExtraLarge:
                    return "огромный";
                default:
                    return string.Empty;
            }
        }
        public string GetStatus()
        {
            switch (Status)
            {
                case OrderStatus.Inactive:
                    return "неактивен";
                case OrderStatus.Active:
                    return "активен";
                case OrderStatus.Done:
                    return "доставлен";
                default:
                    return string.Empty;
            }
        }
        public string GetPaymentMethod()
        {
            switch (PaymentMethod)
            {
                case OrderPaymentMethod.Cash:
                    return "наличная оплата";
                case OrderPaymentMethod.Cashless:
                    return "безналичная оплата";
                default:
                    return string.Empty;
            }
        }

        public void Done() => Done(DateTime.Now);
        public void Done(DateTime dateTime)
        {
            Status = OrderStatus.Done;
            ActualDeliveryTime = dateTime;
            // добавить добавление этого заказа в список заказов курьера
        }
    }

    public enum OrderSize
    {
        VerySmall,
        Small,
        Average,
        Large,
        VeryLarge,
        ExtraLarge
    }
    public enum OrderStatus
    {
        Inactive,
        Active,
        Done
    }
    public enum OrderPaymentMethod
    {
        Cash,
        Cashless
    }    
}
