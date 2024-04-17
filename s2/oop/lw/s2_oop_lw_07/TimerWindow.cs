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
    public partial class TimerWindow : Form
    {
        int seconds;
        int minutes;
        int hours;

        public TimerWindow()
        {
            InitializeComponent();
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            seconds = Convert.ToInt32(secondesLabel.Text);
            if (seconds >= 60)
            {
                secondesLabel.Text = "59";
                seconds = 59;
            }
            minutes = Convert.ToInt32(minutesLabel.Text);
            if (minutes >= 60)
            {
                minutesLabel.Text = "59";
                minutes = 59;
            }
            hours = Convert.ToInt32(hoursLabel.Text);
            timer.Start();
        }

        private void stopButton_Click(object sender, EventArgs e)
        {
            timer.Stop();
            secondesLabel.Text = "0";
            minutesLabel.Text = "0";
            hoursLabel.Text = "0";
        }

        private void pauseButton_Click(object sender, EventArgs e)
        {
            timer.Stop();
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            seconds--;
            if (seconds == -1)
            {
                minutes--;
                seconds = 59;
            }
            if (minutes == -1)
            {
                hours--;
                minutes = 59;
            }
            if (hours == -1)
            {
                timer.Stop();
                MessageBox.Show("Время вышло!");
            }
            else
            {
                secondesLabel.Text = Convert.ToString(seconds);
                minutesLabel.Text = Convert.ToString(minutes);
                hoursLabel.Text = Convert.ToString(hours);
            }
        }
        private void hoursLabel_KeyPress(object sender, KeyPressEventArgs e)
        {
            char number = e.KeyChar;
            if (!Char.IsDigit(number))
            {
                e.Handled = true;
            }
        }
        private void minutesLabel_KeyPress(object sender, KeyPressEventArgs e)
        {
            char number = e.KeyChar;
            if (!Char.IsDigit(number))
            {
                e.Handled = true;
            }
        }
        private void secondesLabel_KeyPress(object sender, KeyPressEventArgs e)
        {
            char number = e.KeyChar;
            if (!Char.IsDigit(number))
            {
                e.Handled = true;
            }
        }
    }
}
