using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace s2_oop_lw_07
{
    public partial class MainWindow : Form
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void секундомерToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.MdiParent = this;
            stopwatch.Show();
        }

        private void timerButton_Click(object sender, EventArgs e)
        {
            TimerWindow timer = new TimerWindow();
            timer.MdiParent = this;
            timer.Show();
        }

        private void closeAllButton_Click(object sender, EventArgs e)
        {
            foreach (Form form in this.MdiChildren)
            {
                form.Close();
            }
        }

        private void cascadeButton_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.Cascade);
        }

        private void horisontalButton_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileHorizontal);
        }

        private void verticalButton_Click(object sender, EventArgs e)
        {
            this.LayoutMdi(MdiLayout.TileVertical);
        }

        private void what_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Собирает как-то мать сына в школу." +
                            "\nКладет ему в рюкзак хлеб, колбасу и гвозди." +
                            "\nСын удивленно спрашивает:" +
                            "\n- Мама, что?" +
                            "\nА мать отвечает:" +
                            "\nКак что? Берешь хлеб, кладешь колбасу и ешь." +
                            "\nА гвозди?" +
                            "\nТак вот же они!", "Внимание, анекдот");
        }
    }
}
