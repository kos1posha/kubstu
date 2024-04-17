using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BizyaevKursach
{
    [Serializable()]
    class Save
    {
        public List<Order> InactiveOrders { get; set; }
        public List<Courier> Couriers { get; set; }
        public List<Curator> Curators { get; set; }

        public Save(List<Order> inactiveOrders, List<Courier> couriers, List<Curator> curators)
        {
            InactiveOrders = inactiveOrders;
            Couriers = couriers;
            Curators = curators;
        }
    }
}
