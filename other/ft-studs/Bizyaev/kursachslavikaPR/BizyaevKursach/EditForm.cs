using System;
using System.Drawing;
using System.Windows.Forms;

namespace BizyaevKursach
{
    public partial class EditForm : Form
    {
        public EditForm()
        {
            InitializeComponent();
        }

        private void EditForm_Load(object sender, EventArgs e)
        {
            telephoneEditBox.Text = Program.CurrentCourier.TelephoneNumber;
            nameEditBox.Text = Program.CurrentCourier.Name;

            foreach (OrderSize size in Program.CurrentCourier.CanDeliveryList)
                switch (size)
                {
                    case (OrderSize.VerySmall):
                        verySmallCheck.Checked = true;
                        break;
                    case (OrderSize.Small):
                        smallCheck.Checked = true;
                        break;
                    case (OrderSize.Average):
                        averageCheck.Checked = true;
                        break;
                    case (OrderSize.Large):
                        largeCheck.Checked = true;
                        break;
                    case (OrderSize.VeryLarge):
                        veryLargeCheck.Checked = true;
                        break;
                    case (OrderSize.ExtraLarge):
                        extraLargeCheck.Checked = true;
                        break;
                }
        }

        new public static DialogResult Show()
        {
            EditForm editForm = new EditForm();
            return editForm.ShowDialog();
        }

        private void saveButton_Click(object sender, EventArgs e)
        {
            bool correct = true;
            if (nameEditBox.Text.Trim() == "")
            {
                nameLabel.ForeColor = Color.Red;
                correct = false;
            }
            if (!telephoneEditBox.MaskCompleted)
            {
                telephoneNumberLabel.ForeColor = Color.Red;
                correct = false;
            }
            if (!correct) return;

            DialogResult = DialogResult.OK;

            Program.CurrentCourier.TelephoneNumber = telephoneEditBox.Text;
            Program.CurrentCourier.Name = nameEditBox.Text;
            Program.CurrentCourier.CanDeliveryList.Clear();

            if (verySmallCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.VerySmall);
            if (smallCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.Small);
            if (averageCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.Average);
            if (largeCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.Large);
            if (veryLargeCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.VeryLarge);
            if (extraLargeCheck.Checked)
                Program.CurrentCourier.CanDeliveryList.Add(OrderSize.ExtraLarge);

            Dispose();
        }

        private void cancelButton_Click(object sender, EventArgs e)
        {
            DialogResult = DialogResult.Cancel;
            Dispose();
        }
    }
}
