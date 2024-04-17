using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class OrderPanel : UserControl
    {
        public Order Order;

        public OrderPanel(Order order)
        {
            InitializeComponent();

            Order = order;
        }
        private void OrderPanel_Load(object sender, EventArgs e)
        {
            if (Order.Note == string.Empty)
                infoButton.Visible = false;
            numberLabel.Text = $"Заказ номер {Order.Number}";
            timeLabel.Text = $"от {Program.GetDate(Order.FormationTime)} до {Program.GetDate(Order.RequestedDeliveryTime)}";
            actualDeliveryTimeLabel.Text = $"доставлен {Program.GetDate(Order.ActualDeliveryTime)}";
            weightLabel.Text = $"Вес: {Order.Weight} кг";
            sizeLabel.Text = $"Размер: {Order.GetSize()}";
            senderFirmLabel.Text = $"Фирма-отправитель: {Order.SenderFirm}";
            receivingAddressLabel.Text = $"Адрес получения посылки: {Order.ReceivingAddress}";
            deliveryAddressLabel.Text = $"Адрес доставки: {Order.DeliveryAddress}";
            receiverNameLabel.Text = $"Имя получателя: {Order.ReceiverName}";
            paymentMethodLabel.Text = $"Способ оплаты: {Order.GetPaymentMethod()}";

            if (Program.CurrentCourier.HiddenOrders.Contains(Order))
            {
                Size = new Size(Width, Height - 25);
                firstButton.Text = "Убрать";
                firstButton.Location = new Point(271, 165);
                firstButton.Click += new EventHandler(unhideButton_Click);
                return;
            }
            switch (Order.Status)
            {
                case OrderStatus.Inactive:
                    Size = new Size(Width, Height - 25);
                    firstButton.Text = "Принять";
                    secondButton.Text = "Скрыть";
                    firstButton.Click += new EventHandler(activeButton_Click);
                    secondButton.Click += new EventHandler(hideButton_Click);
                    break;
                case OrderStatus.Active:
                    Size = new Size(Width, Height - 25);
                    firstButton.Text = "Доставлено";
                    secondButton.Text = "Отменить";
                    firstButton.Click += new EventHandler(doneButton_Click);
                    secondButton.Click += new EventHandler(cancelButton_Click);
                    break;
                case OrderStatus.Done:
                    Size = new Size(Width, Height - 40);
                    bodyPanel.Size = new Size(bodyPanel.Width, bodyPanel.Height - 40);
                    bodyPanel.Location = new Point(bodyPanel.Location.X, bodyPanel.Location.Y + 40);
                    break;
            }
        }

        private void infoButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Подбробная информация  о заказе", Order.Note, MessageBoxButtons.OK);
        }
        private void activeButton_Click(object sender, EventArgs e)
        {
            Order.Status = OrderStatus.Active;
            Program.CurrentCourier.ActiveOrders.Add(Order);
            Program.MainForm.AddOrder(Order);
            Parent.Controls.Remove(this);
            Dispose();
        }
        private void hideButton_Click(object sender, EventArgs e)
        {
            Program.CurrentCourier.HiddenOrders.Add(Order);
            Parent.Controls.Remove(this);
            Dispose();
        }
        private void cancelButton_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Вы уверены?", "Отмененный заказ будет скрыт и получит статус неактивного. Вы сможете найти его в списке скрытых заказов.", MessageBoxButtons.OKCancel);
            if (result == DialogResult.Cancel)
                return;

            Program.CurrentCourier.HiddenOrders.Add(Order);
            Order.Status = OrderStatus.Inactive;
            Parent.Controls.Remove(this);
            Dispose();
        }
        private void doneButton_Click(object sender, EventArgs e)
        {
            Order.Status = OrderStatus.Done;
            Order.ActualDeliveryTime = DateTime.Now;
            Program.CurrentCourier.OrdersHistory.Add(Order);
            Program.MainForm.AddOrder(Order);
            Parent.Controls.Remove(this);
            Dispose();
        }
        private void unhideButton_Click(object sender, EventArgs e)
        {
            Program.CurrentCourier.HiddenOrders.Remove(Order);
            Program.MainForm.AddOrder(Order);
            Parent.Controls.Remove(this);
            Dispose();
        }

        private void infoButton_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            Control control = (Control)sender;
            int radius = control.Width + 1;
            using (System.Drawing.Drawing2D.GraphicsPath path = new System.Drawing.Drawing2D.GraphicsPath())
            {
                path.AddLine(radius, 0, control.Width - radius, 0);
                path.AddArc(control.Width - radius, -1, radius, radius, 270, 90);
                path.AddLine(control.Width, radius, control.Width, control.Height - radius);
                path.AddArc(control.Width - radius, control.Height - radius, radius, radius, -1, 90);
                path.AddLine(control.Width - radius, control.Height, radius, control.Height);
                path.AddArc(-1, control.Height - radius, radius, radius, 90, 90);
                path.AddLine(0, control.Height - radius, 0, radius);
                path.AddArc(-1, -1, radius, radius, 180, 90);
                control.Region = new Region(path);
            }
        }
    }
}
