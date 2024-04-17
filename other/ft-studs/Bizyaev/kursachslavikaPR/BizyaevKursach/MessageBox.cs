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
    public partial class MessageBox : Form
    {
        public MessageBox(string caption, string message, MessageBoxButtons messageBoxButtons)
        {
            InitializeComponent();

            captionLabel.Text = caption;
            messageLabel.Text = message;
            Size = new Size(337, 106 + (message.Length / 44 * 20));
            bodyPanel.Size = new Size(Size.Width - 2, Size.Height - 2);

            switch (messageBoxButtons)
            {
                case MessageBoxButtons.OK:
                    cancelButton.Hide();
                    okButton.Location = cancelButton.Location;
                    break;
            }
        }

        public static DialogResult Show(string message) => Show("", message, MessageBoxButtons.OK);
        public static DialogResult Show(string caption, string message) => Show(caption, message, MessageBoxButtons.OK);
        public static DialogResult Show(string message, MessageBoxButtons messageType) => Show("", message, messageType);
        public static DialogResult Show(string caption, string message, MessageBoxButtons messageBoxButtons)
        {
            MessageBox messageBox = new MessageBox(caption, message, messageBoxButtons);
            messageBox.ShowDialog();
            return messageBox.DialogResult;
        }
            
        private void okButton_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.OK;
            Dispose();
        }
        private void cancelButton_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.Cancel;
            Dispose();
        }
    }
}
