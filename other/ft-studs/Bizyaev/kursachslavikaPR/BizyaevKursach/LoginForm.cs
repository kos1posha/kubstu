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
    public partial class LoginForm : Form
    {
        public LoginForm()
        {
            InitializeComponent();
        }

        private void loginButton_Click(object sender, EventArgs e)
        {
            bool verification = false;

            foreach (User user in Program.Curators)
                if (user.Verification(loginTextBox.Text, passwordTextBox.Text))
                {
                    CuratorsForm curatorsForm = new CuratorsForm();
                    verification = true;
                    Hide();
                }
            foreach (User user in Program.Couriers)
                if (user.Verification(loginTextBox.Text, passwordTextBox.Text))
                {
                    Program.CurrentCourier = (Courier)user;
                    Program.MainForm = new MainForm();
                    verification = true;
                    Hide();
                }

            if (!verification)
                MessageBox.Show("Ошибка", "Пользователь не найден");
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }
    }
}
