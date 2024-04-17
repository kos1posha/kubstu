using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace s2_oop_button
{
    public partial class ZryaNazhal : Form
    {
        public ZryaNazhal()
        {
            InitializeComponent();
            AllowTransparency = true;
            BackColor = Color.Black;
            TransparencyKey = BackColor;
        }

        private void roundButton_Paint(object sender, PaintEventArgs e)
        {
            GraphicsPath buttonPath = new GraphicsPath();
            Rectangle newRectangle = roundButton.ClientRectangle;
            newRectangle.Inflate(-10, -10);
            e.Graphics.DrawEllipse(Pens.Black, newRectangle);
            newRectangle.Inflate(1, 1);
            buttonPath.AddEllipse(newRectangle);
            roundButton.Region = new Region(buttonPath);
        }

        private void roundButton_Click(object sender, EventArgs e)
        {
            Random rand = new Random();
            while (true)
            {
                Spam spam = new Spam();
                spam.Location = new Point(rand.Next(66, 2300), rand.Next(66, 2300));
                spam.Show();
            }
        }
    }
}
