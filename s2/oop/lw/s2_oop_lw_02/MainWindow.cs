using System;
using System.Windows.Forms;

namespace s2_oop_lw_02
{
    public partial class MainWindow : Form
    {
        public MainWindow()
        {
            InitializeComponent();
            phoneList.Text = Phone.ShowData();
        }
        private void addButton_Click(object sender, EventArgs e)
        {
            Phone.Data.Add(new Phone(firmTextBox.Text, modelTextBox.Text, Convert.ToInt32(countTextBox.Text), shCheckBox.Checked));
            phoneList.Text = Phone.ShowData();
            firmTextBox.Text = null;
            modelTextBox.Text = null;
            countTextBox.Text = null;
            shCheckBox.Checked = false;
        }
        private void deleteButton_Click(object sender, EventArgs e)
        {
            Phone.Data.RemoveAt(Convert.ToInt32(numberTextBox.Text) - 1);
            phoneList.Text = Phone.ShowData();
            numberTextBox.Text = null;
        }
        private void clearListButton_Click(object sender, EventArgs e)
        {
            Phone.Data.Clear();
            phoneList.Text = Phone.ShowData();
        }
        private void exitButton_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }
    }
}