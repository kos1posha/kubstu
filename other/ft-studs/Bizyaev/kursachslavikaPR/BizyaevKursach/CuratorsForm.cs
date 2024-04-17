using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class CuratorsForm : Form
    {
        public CuratorsForm()
        {
            InitializeComponent();

            Show();
        }

        private void CuratorsForm_Load(object sender, EventArgs e)
        {
            UpdateCounts();
        }

        public void UpdateCounts()
        {
            inactiveCountLabel.Text = $"Неактивных: {Program.InactiveOrders.Count}";
            int activeCount = 0;
            foreach (Courier courier in Program.Couriers)
                activeCount += courier.ActiveOrders.Count;
            activeCountLabel.Text = $"Активных: {activeCount}";
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            using (FileStream fileStream = new FileStream("save.dat", FileMode.OpenOrCreate))
            {
                BinaryFormatter binaryFormatter = new BinaryFormatter();
                binaryFormatter.Serialize(fileStream, new Save(Program.InactiveOrders, Program.Couriers, Program.Curators));
            }

            Environment.Exit(0);
        }

        private void createButton_Click(object sender, EventArgs e)
        {
            Order newOrder = NewOrder.Show();
            if (newOrder != null)
            {
                Program.InactiveOrders.Add(newOrder);
                MessageBox.Show("Заказ успешно создан.");
                UpdateCounts();
            }
        }
    }
}
