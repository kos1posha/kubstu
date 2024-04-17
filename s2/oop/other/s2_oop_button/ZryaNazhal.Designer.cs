
namespace s2_oop_button
{
    partial class ZryaNazhal
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.roundButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // roundButton
            // 
            this.roundButton.BackColor = System.Drawing.Color.DarkRed;
            this.roundButton.Cursor = System.Windows.Forms.Cursors.No;
            this.roundButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.roundButton.Font = new System.Drawing.Font("Segoe UI Black", 12F, ((System.Drawing.FontStyle)(((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic) 
                | System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.roundButton.ForeColor = System.Drawing.Color.White;
            this.roundButton.Location = new System.Drawing.Point(4, 4);
            this.roundButton.Margin = new System.Windows.Forms.Padding(0);
            this.roundButton.Name = "roundButton";
            this.roundButton.Size = new System.Drawing.Size(129, 130);
            this.roundButton.TabIndex = 0;
            this.roundButton.Text = "НЕ НАЖИМАЙ";
            this.roundButton.UseVisualStyleBackColor = false;
            this.roundButton.Click += new System.EventHandler(this.roundButton_Click);
            this.roundButton.Paint += new System.Windows.Forms.PaintEventHandler(this.roundButton_Paint);
            // 
            // ZryaNazhal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.Black;
            this.ClientSize = new System.Drawing.Size(137, 139);
            this.Controls.Add(this.roundButton);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "ZryaNazhal";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button roundButton;
    }
}

