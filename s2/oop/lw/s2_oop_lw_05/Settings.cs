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
    public partial class Settings : Form
    {
        private Game Game;

        public Settings(Game game)
        {
            InitializeComponent();
            Game = game;
        }

        private void continueButton_Click(object sender, EventArgs e)
        {
            Dispose();
            Game.Enabled = true;
        }

        private void restartButton_Click(object sender, EventArgs e)
        {
            DialogResult result =
                MessageBox.Show("Вы уверены, что хотите начать новую игру? Весь нынешний прогресс будет безвозвратно удален.", "Начать заново?", MessageBoxButtons.YesNo);
            if (result == DialogResult.Yes)
            {
                Registration registration = new Registration();
                registration.Show();
                Dispose();
                Game.Dispose();
            }
        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            // аче
        }

        private void exitButton_Click(object sender, EventArgs e)
        {
            DialogResult result =
                MessageBox.Show("Вы уверены, что хотите выйти из игры? Весь несохранненый прогресс будет безвозвратно удален.", "Выйти из игры?", MessageBoxButtons.YesNo);
            if (result == DialogResult.Yes)
            {
                Environment.Exit(0);
            }
        }
    }
}
