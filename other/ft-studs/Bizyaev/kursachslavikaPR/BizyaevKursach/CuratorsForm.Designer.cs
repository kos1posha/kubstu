
namespace BizyaevKursach
{
    partial class CuratorsForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.exitButton = new System.Windows.Forms.Button();
            this.createButton = new System.Windows.Forms.Button();
            this.headPanel = new System.Windows.Forms.Panel();
            this.bodyPanel = new System.Windows.Forms.Panel();
            this.activeCountLabel = new System.Windows.Forms.Label();
            this.inactiveCountLabel = new System.Windows.Forms.Label();
            this.receivingAddressLabel = new System.Windows.Forms.Label();
            this.headPanel.SuspendLayout();
            this.bodyPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // exitButton
            // 
            this.exitButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.exitButton.BackColor = System.Drawing.Color.LightCoral;
            this.exitButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.exitButton.FlatAppearance.BorderSize = 0;
            this.exitButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.exitButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Firebrick;
            this.exitButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.exitButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.exitButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.exitButton.Location = new System.Drawing.Point(225, 0);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(32, 36);
            this.exitButton.TabIndex = 1;
            this.exitButton.Text = "X";
            this.exitButton.UseVisualStyleBackColor = false;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // createButton
            // 
            this.createButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.createButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(188)))), ((int)(((byte)(201)))), ((int)(((byte)(135)))));
            this.createButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.createButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(166)))), ((int)(((byte)(183)))), ((int)(((byte)(96)))));
            this.createButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.createButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.createButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.createButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.createButton.Location = new System.Drawing.Point(14, 86);
            this.createButton.Name = "createButton";
            this.createButton.Size = new System.Drawing.Size(228, 33);
            this.createButton.TabIndex = 2;
            this.createButton.Text = "Создать заказ";
            this.createButton.UseVisualStyleBackColor = false;
            this.createButton.Click += new System.EventHandler(this.createButton_Click);
            // 
            // headPanel
            // 
            this.headPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.headPanel.BackColor = System.Drawing.Color.DarkGray;
            this.headPanel.Controls.Add(this.exitButton);
            this.headPanel.Location = new System.Drawing.Point(1, 1);
            this.headPanel.Name = "headPanel";
            this.headPanel.Size = new System.Drawing.Size(257, 36);
            this.headPanel.TabIndex = 4;
            // 
            // bodyPanel
            // 
            this.bodyPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bodyPanel.BackColor = System.Drawing.Color.White;
            this.bodyPanel.Controls.Add(this.activeCountLabel);
            this.bodyPanel.Controls.Add(this.inactiveCountLabel);
            this.bodyPanel.Controls.Add(this.receivingAddressLabel);
            this.bodyPanel.Controls.Add(this.createButton);
            this.bodyPanel.Location = new System.Drawing.Point(1, 37);
            this.bodyPanel.Name = "bodyPanel";
            this.bodyPanel.Size = new System.Drawing.Size(257, 128);
            this.bodyPanel.TabIndex = 6;
            // 
            // activeCountLabel
            // 
            this.activeCountLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.activeCountLabel.AutoEllipsis = true;
            this.activeCountLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.activeCountLabel.ForeColor = System.Drawing.Color.Black;
            this.activeCountLabel.Location = new System.Drawing.Point(10, 56);
            this.activeCountLabel.Name = "activeCountLabel";
            this.activeCountLabel.Size = new System.Drawing.Size(236, 27);
            this.activeCountLabel.TabIndex = 21;
            this.activeCountLabel.Text = "Активных:";
            // 
            // inactiveCountLabel
            // 
            this.inactiveCountLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.inactiveCountLabel.AutoEllipsis = true;
            this.inactiveCountLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.inactiveCountLabel.ForeColor = System.Drawing.Color.Black;
            this.inactiveCountLabel.Location = new System.Drawing.Point(10, 29);
            this.inactiveCountLabel.Name = "inactiveCountLabel";
            this.inactiveCountLabel.Size = new System.Drawing.Size(236, 27);
            this.inactiveCountLabel.TabIndex = 20;
            this.inactiveCountLabel.Text = "Неактивных:";
            // 
            // receivingAddressLabel
            // 
            this.receivingAddressLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.receivingAddressLabel.AutoEllipsis = true;
            this.receivingAddressLabel.Font = new System.Drawing.Font("Century Gothic", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.receivingAddressLabel.ForeColor = System.Drawing.Color.Black;
            this.receivingAddressLabel.Location = new System.Drawing.Point(10, 2);
            this.receivingAddressLabel.Name = "receivingAddressLabel";
            this.receivingAddressLabel.Size = new System.Drawing.Size(236, 27);
            this.receivingAddressLabel.TabIndex = 16;
            this.receivingAddressLabel.Text = "Заказы";
            // 
            // CuratorsForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.ClientSize = new System.Drawing.Size(259, 166);
            this.Controls.Add(this.headPanel);
            this.Controls.Add(this.bodyPanel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "CuratorsForm";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.TopMost = true;
            this.Load += new System.EventHandler(this.CuratorsForm_Load);
            this.headPanel.ResumeLayout(false);
            this.bodyPanel.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button exitButton;
        private System.Windows.Forms.Button createButton;
        private System.Windows.Forms.Panel headPanel;
        private System.Windows.Forms.Panel bodyPanel;
        private System.Windows.Forms.Label receivingAddressLabel;
        private System.Windows.Forms.Label activeCountLabel;
        private System.Windows.Forms.Label inactiveCountLabel;
    }
}