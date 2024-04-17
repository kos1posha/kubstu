using System;
using System.Globalization;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class NewOrder : Form
    {
        public Order Order { get; set; }  

        public NewOrder()
        {
            InitializeComponent();
        }

        private void NewOrder_Load(object sender, EventArgs e)
        {
            numberLabel.Text = $"Заказ номер {Order.GetCount() + 1}";
            timeLabel.Text = $"от {Program.GetDate(DateTime.Now)}";
        }

        public decimal GetWeight()
        {
            return (Convert.ToInt32(weightTextBox.Text.Substring(0, 2)) + Convert.ToDecimal(weightTextBox.Text.Substring(2, 2)) / 10m);
        }
        public OrderPaymentMethod GetPaymentMethod()
        {
            if (paymentMethodComboBox.SelectedIndex == 0)
                return OrderPaymentMethod.Cash;
            else
                return OrderPaymentMethod.Cashless;
        }

        new public static Order Show()
        {
            NewOrder newOrder = new NewOrder();
            newOrder.ShowDialog();
            if (newOrder.Order != null)
                return newOrder.Order;
            return null;
        }

        private void cancelButton_Click(object sender, EventArgs e)
        {
            Dispose();
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            timeLabel.Text = $"от {Program.GetDate(DateTime.Now)}";
        }

        private void createButton_Click(object sender, EventArgs e)
        {
            try
            {
                Order = new Order(Convert.ToDecimal(costTextBox.Text), receivingAddressTextBox.Text, deliveryAddressTextBox.Text, senderFirmTextBox.Text, receiverNameTextBox.Text, GetWeight(), GetPaymentMethod(), DateTime.Now, DateTime.ParseExact(deliveryTimeTextBox.Text.Substring(3), "dd,MM,yyyy", CultureInfo.InvariantCulture)); //DateTime dt=DateTime.ParseExact("24/01/2013", "ddMMyyyy", CultureInfo.InvariantCulture);
            }
            catch
            {
                MessageBox.Show("Ошибка", "Некорректные даннные");
            }
        }
    }
}
