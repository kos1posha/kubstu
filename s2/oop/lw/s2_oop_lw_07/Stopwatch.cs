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
    public partial class Stopwatch : Form
    {
        int seconds;
        int minutes;
        int hours;
        public Stopwatch()
        {
            InitializeComponent();
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            seconds++;
            if (seconds == 60)
            {
                minutes++;
                seconds = 0;
            }
            if (minutes == 60)
            {
                hours++;
                minutes = 0;
            }
            secondesLabel.Text = Convert.ToString(seconds);
            minutesLabel.Text = Convert.ToString(minutes);
            hoursLabel.Text = Convert.ToString(hours);
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            seconds = Convert.ToInt32(secondesLabel.Text);
            minutes = Convert.ToInt32(minutesLabel.Text);
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
    }
}
