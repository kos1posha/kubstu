using System;
using System.Drawing;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();

            Show();
        }
        private void MainForm_Load(object sender, EventArgs e)
        {
            generalTabControl.SelectedIndex = 1;

            activeOrdersCount.Text = activeOrdersList.Controls.Count.ToString();
            inactiveOrdersCount.Text = inactiveOrdersList.Controls.Count.ToString();

            idLabel.Text = $"ID: {Program.CurrentCourier.Id}";
            telephoneNumberLabel.Text = $"Телефон: {Program.CurrentCourier.TelephoneNumber}";
            nameLabel.Text = $"ФИО: {Program.CurrentCourier.Name}";
            registrationDateLabel.Text = $"Дата регистрации: {Program.GetDate(Program.CurrentCourier.RegistrationDate)}";
            doneOrdersCountLabel.Text = $"Доставил заказов:  {doneOrdersList.Controls.Count}";
            canDeliveryLabel.Text = $"Могу доставить: {Program.CurrentCourier.GetCanDeliveryString()}";

            foreach (Order order in Program.InactiveOrders)
                AddOrder(order);
            foreach (Order order in Program.CurrentCourier.ActiveOrders)
                AddOrder(order);
            foreach (Order order in Program.CurrentCourier.OrdersHistory)
                AddOrder(order);
        }

        public void AddOrder(Order order)
        {
            if (!Program.CurrentCourier.CanDelivery(order))
                return;
            if (Program.CurrentCourier.HiddenOrders.Contains(order))
                return;

            TableLayoutPanel control = null;
            switch (order.Status)
            {
                case OrderStatus.Inactive:
                    control = inactiveOrdersList;
                    break;
                case OrderStatus.Active:
                    control = activeOrdersList;
                    break;
                case OrderStatus.Done:
                    control = doneOrdersList;
                    break;
            }

            control.Controls.Add(new OrderPanel(order));
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
        private void editInfoButton_Click(object sender, EventArgs e)
        {
            if (EditForm.Show() == DialogResult.OK)
                MainForm_Load(sender, e);
        }
        private void hiddenOrdersListButton_Click(object sender, EventArgs e)
        {
            OrdersList ordersList = new OrdersList(generalTabControl.TabPages[1]);
            ordersList.Parent.Controls.SetChildIndex(ordersList, 0);
        }

        private void ordersList_ControlAdded(object sender, ControlEventArgs e)
        {
            Control control = (Control)sender;

            doneOrdersCountLabel.Text = "Доставил заказов: " + doneOrdersList.Controls.Count.ToString();
            activeOrdersCount.Text = activeOrdersList.Controls.Count.ToString();
            inactiveOrdersCount.Text = inactiveOrdersList.Controls.Count.ToString();
            control.Size = new Size(control.Size.Width, control.Size.Height + 265);
        }
        private void ordersList_ControlRemoved(object sender, ControlEventArgs e)
        {
            Control control = (Control)sender;

            activeOrdersCount.Text = activeOrdersList.Controls.Count.ToString();
            inactiveOrdersCount.Text = inactiveOrdersList.Controls.Count.ToString();
            control.Size = new Size(control.Width, control.Height - 265);
        }
        private void ordersPage_Scroll(object sender, ScrollEventArgs e)
        {
            Control control = (Control)sender;
            control.Refresh();
        }

        private void ordersCount_Paint(object sender, PaintEventArgs e)
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
        private void ordersCount_TextChanged(object sender, EventArgs e)
        {
            Label control = (Label)sender;
            if (control.Text == "0")
                control.Visible = false;
            else
                control.Visible = true;
        }
        private void courierPhoto_DoubleClick(object sender, EventArgs e)
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.Filter = "Файл \"JPG\" (*.jpg)|*.jpg|Файл \"PNG\" (*.png)|*.png";
                openFileDialog.ShowDialog();
                if (openFileDialog.FileName != string.Empty)
                    if (MessageBox.Show("Сохранить фотографию?", MessageBoxButtons.OKCancel) == DialogResult.OK)
                        courierPhoto.Image = Program.CurrentCourier.Photo = Image.FromFile(openFileDialog.FileName);
            }
        }
        private void exit_MouseEnter(object sender, EventArgs e)
        {
            exit.ForeColor = Color.Red;
        }
        private void exit_MouseLeave(object sender, EventArgs e)
        {
            exit.ForeColor = Color.Black;
        }
    }
}