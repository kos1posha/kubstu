using System;
using System.Drawing;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class OrdersList : UserControl
    {
        public OrdersList(Control parent)
        {
            Parent = parent;

            InitializeComponent();

            foreach (Order order in Program.CurrentCourier.HiddenOrders)
                AddOrder(order);
        }
        public void AddOrder(Order order)
        {
            currentOrdersList.Controls.Add(new OrderPanel(order));
        }

        private void closeButton_Click(object sender, EventArgs e)
        {
            Parent.Controls.SetChildIndex(this, Parent.Controls.Count - 1);
        }

        private void ordersList_ControlAdded(object sender, ControlEventArgs e)
        {
            Control control = (Control)sender;
            control.Size = new Size(control.Size.Width, control.Size.Height + 265);
        }
        private void ordersList_ControlRemoved(object sender, ControlEventArgs e)
        {
            Control control = (Control)sender;
            control.Size = new Size(control.Size.Width, control.Size.Height - 265);
        }
    }
}
