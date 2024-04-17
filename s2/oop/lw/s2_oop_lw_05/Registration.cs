using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace s2_oop_lw_05
{
    public partial class Registration : Form
    {
        public Registration()
        {
            InitializeComponent();
        }

        private void regExitButton_Click(object sender, EventArgs e)
        {
            Environment.Exit(0);
        }

        private void regStartButton_Click(object sender, EventArgs e)
        {
            if (heroName.Text.Trim() == "")
            {
                MessageBox.Show(this, "Не у всех героев есть предыстория, но у каждого должно быть имя.", "Выберите имя", MessageBoxButtons.OK);
                return;
            }
            if (heroClass.Text == "")
            {
                MessageBox.Show(this, "Стать легендарным крестьянином с копьем вам, увы, не велено судьбой.", "Выберите класс", MessageBoxButtons.OK);
                return;
            }
            Game game = new Game(heroName.Text.Trim(), heroClass.Text);
            game.Show();
            Hide();
        }
    }
}
