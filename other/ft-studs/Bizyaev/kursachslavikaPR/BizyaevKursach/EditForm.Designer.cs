
namespace BizyaevKursach
{
    partial class EditForm
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
            this.cancelButton = new System.Windows.Forms.Button();
            this.saveButton = new System.Windows.Forms.Button();
            this.captionLabel = new System.Windows.Forms.Label();
            this.headPanel = new System.Windows.Forms.Panel();
            this.bodyPanel = new System.Windows.Forms.Panel();
            this.helpTitle = new System.Windows.Forms.Label();
            this.canDeliveryLabel = new System.Windows.Forms.Label();
            this.canDeliveryPanel = new System.Windows.Forms.Panel();
            this.verySmallCheck = new System.Windows.Forms.CheckBox();
            this.smallCheck = new System.Windows.Forms.CheckBox();
            this.largeCheck = new System.Windows.Forms.CheckBox();
            this.averageCheck = new System.Windows.Forms.CheckBox();
            this.veryLargeCheck = new System.Windows.Forms.CheckBox();
            this.extraLargeCheck = new System.Windows.Forms.CheckBox();
            this.infoBox = new System.Windows.Forms.GroupBox();
            this.telephoneEditBox = new System.Windows.Forms.MaskedTextBox();
            this.nameEditBox = new System.Windows.Forms.TextBox();
            this.nameLabel = new System.Windows.Forms.Label();
            this.telephoneNumberLabel = new System.Windows.Forms.Label();
            this.headPanel.SuspendLayout();
            this.bodyPanel.SuspendLayout();
            this.canDeliveryPanel.SuspendLayout();
            this.infoBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // cancelButton
            // 
            this.cancelButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.cancelButton.BackColor = System.Drawing.Color.LightCoral;
            this.cancelButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.cancelButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.cancelButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Firebrick;
            this.cancelButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.cancelButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.cancelButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.cancelButton.Location = new System.Drawing.Point(222, 283);
            this.cancelButton.Name = "cancelButton";
            this.cancelButton.Size = new System.Drawing.Size(122, 33);
            this.cancelButton.TabIndex = 1;
            this.cancelButton.Text = "Отмена";
            this.cancelButton.UseVisualStyleBackColor = false;
            this.cancelButton.Click += new System.EventHandler(this.cancelButton_Click);
            // 
            // saveButton
            // 
            this.saveButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
            this.saveButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(188)))), ((int)(((byte)(201)))), ((int)(((byte)(135)))));
            this.saveButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.saveButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(166)))), ((int)(((byte)(183)))), ((int)(((byte)(96)))));
            this.saveButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.saveButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.saveButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.saveButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.saveButton.Location = new System.Drawing.Point(94, 283);
            this.saveButton.Name = "saveButton";
            this.saveButton.Size = new System.Drawing.Size(122, 33);
            this.saveButton.TabIndex = 2;
            this.saveButton.Text = "Сохранить";
            this.saveButton.UseVisualStyleBackColor = false;
            this.saveButton.Click += new System.EventHandler(this.saveButton_Click);
            // 
            // captionLabel
            // 
            this.captionLabel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.captionLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.captionLabel.Location = new System.Drawing.Point(3, 9);
            this.captionLabel.Name = "captionLabel";
            this.captionLabel.Size = new System.Drawing.Size(349, 22);
            this.captionLabel.TabIndex = 3;
            this.captionLabel.Text = "Изменить";
            // 
            // headPanel
            // 
            this.headPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.headPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.headPanel.Controls.Add(this.captionLabel);
            this.headPanel.Location = new System.Drawing.Point(1, 1);
            this.headPanel.Name = "headPanel";
            this.headPanel.Size = new System.Drawing.Size(355, 36);
            this.headPanel.TabIndex = 4;
            // 
            // bodyPanel
            // 
            this.bodyPanel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bodyPanel.BackColor = System.Drawing.Color.White;
            this.bodyPanel.Controls.Add(this.helpTitle);
            this.bodyPanel.Controls.Add(this.canDeliveryLabel);
            this.bodyPanel.Controls.Add(this.canDeliveryPanel);
            this.bodyPanel.Controls.Add(this.infoBox);
            this.bodyPanel.Controls.Add(this.cancelButton);
            this.bodyPanel.Controls.Add(this.saveButton);
            this.bodyPanel.Location = new System.Drawing.Point(1, 1);
            this.bodyPanel.Name = "bodyPanel";
            this.bodyPanel.Size = new System.Drawing.Size(355, 320);
            this.bodyPanel.TabIndex = 6;
            // 
            // helpTitle
            // 
            this.helpTitle.Font = new System.Drawing.Font("Century Gothic", 9F, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.helpTitle.Location = new System.Drawing.Point(11, 245);
            this.helpTitle.Name = "helpTitle";
            this.helpTitle.Size = new System.Drawing.Size(333, 35);
            this.helpTitle.TabIndex = 28;
            this.helpTitle.Text = "Если вы хотите изменить логин или пароль, \r\nсвяжитель с куратором.";
            this.helpTitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // canDeliveryLabel
            // 
            this.canDeliveryLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.canDeliveryLabel.AutoEllipsis = true;
            this.canDeliveryLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.canDeliveryLabel.ForeColor = System.Drawing.Color.Black;
            this.canDeliveryLabel.Location = new System.Drawing.Point(17, 149);
            this.canDeliveryLabel.Margin = new System.Windows.Forms.Padding(1);
            this.canDeliveryLabel.Name = "canDeliveryLabel";
            this.canDeliveryLabel.Size = new System.Drawing.Size(148, 25);
            this.canDeliveryLabel.TabIndex = 21;
            this.canDeliveryLabel.Text = "Могу доставить: ";
            // 
            // canDeliveryPanel
            // 
            this.canDeliveryPanel.Controls.Add(this.verySmallCheck);
            this.canDeliveryPanel.Controls.Add(this.smallCheck);
            this.canDeliveryPanel.Controls.Add(this.largeCheck);
            this.canDeliveryPanel.Controls.Add(this.averageCheck);
            this.canDeliveryPanel.Controls.Add(this.veryLargeCheck);
            this.canDeliveryPanel.Controls.Add(this.extraLargeCheck);
            this.canDeliveryPanel.Location = new System.Drawing.Point(11, 176);
            this.canDeliveryPanel.Name = "canDeliveryPanel";
            this.canDeliveryPanel.Size = new System.Drawing.Size(333, 68);
            this.canDeliveryPanel.TabIndex = 29;
            // 
            // verySmallCheck
            // 
            this.verySmallCheck.AutoSize = true;
            this.verySmallCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.verySmallCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.verySmallCheck.Location = new System.Drawing.Point(28, 1);
            this.verySmallCheck.Margin = new System.Windows.Forms.Padding(1);
            this.verySmallCheck.Name = "verySmallCheck";
            this.verySmallCheck.Size = new System.Drawing.Size(146, 22);
            this.verySmallCheck.TabIndex = 22;
            this.verySmallCheck.Text = "очень маленький";
            this.verySmallCheck.UseVisualStyleBackColor = true;
            // 
            // smallCheck
            // 
            this.smallCheck.AutoSize = true;
            this.smallCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.smallCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.smallCheck.Location = new System.Drawing.Point(28, 22);
            this.smallCheck.Margin = new System.Windows.Forms.Padding(1);
            this.smallCheck.Name = "smallCheck";
            this.smallCheck.Size = new System.Drawing.Size(105, 22);
            this.smallCheck.TabIndex = 23;
            this.smallCheck.Text = "маленький";
            this.smallCheck.UseVisualStyleBackColor = true;
            // 
            // largeCheck
            // 
            this.largeCheck.AutoSize = true;
            this.largeCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.largeCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.largeCheck.Location = new System.Drawing.Point(176, 1);
            this.largeCheck.Margin = new System.Windows.Forms.Padding(1);
            this.largeCheck.Name = "largeCheck";
            this.largeCheck.Size = new System.Drawing.Size(93, 22);
            this.largeCheck.TabIndex = 25;
            this.largeCheck.Text = "большой";
            this.largeCheck.UseVisualStyleBackColor = true;
            // 
            // averageCheck
            // 
            this.averageCheck.AutoSize = true;
            this.averageCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.averageCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.averageCheck.Location = new System.Drawing.Point(28, 46);
            this.averageCheck.Margin = new System.Windows.Forms.Padding(1);
            this.averageCheck.Name = "averageCheck";
            this.averageCheck.Size = new System.Drawing.Size(90, 22);
            this.averageCheck.TabIndex = 24;
            this.averageCheck.Text = "средний";
            this.averageCheck.UseVisualStyleBackColor = true;
            // 
            // veryLargeCheck
            // 
            this.veryLargeCheck.AutoSize = true;
            this.veryLargeCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.veryLargeCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.veryLargeCheck.Location = new System.Drawing.Point(176, 22);
            this.veryLargeCheck.Margin = new System.Windows.Forms.Padding(1);
            this.veryLargeCheck.Name = "veryLargeCheck";
            this.veryLargeCheck.Size = new System.Drawing.Size(134, 22);
            this.veryLargeCheck.TabIndex = 26;
            this.veryLargeCheck.Text = "очень большой";
            this.veryLargeCheck.UseVisualStyleBackColor = true;
            // 
            // extraLargeCheck
            // 
            this.extraLargeCheck.AutoSize = true;
            this.extraLargeCheck.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.extraLargeCheck.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.extraLargeCheck.Location = new System.Drawing.Point(176, 46);
            this.extraLargeCheck.Margin = new System.Windows.Forms.Padding(1);
            this.extraLargeCheck.Name = "extraLargeCheck";
            this.extraLargeCheck.Size = new System.Drawing.Size(101, 22);
            this.extraLargeCheck.TabIndex = 27;
            this.extraLargeCheck.Text = "огромный";
            this.extraLargeCheck.UseVisualStyleBackColor = true;
            // 
            // infoBox
            // 
            this.infoBox.Controls.Add(this.telephoneEditBox);
            this.infoBox.Controls.Add(this.nameEditBox);
            this.infoBox.Controls.Add(this.telephoneNumberLabel);
            this.infoBox.Controls.Add(this.nameLabel);
            this.infoBox.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.infoBox.Font = new System.Drawing.Font("Century Gothic", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.infoBox.Location = new System.Drawing.Point(11, 42);
            this.infoBox.Name = "infoBox";
            this.infoBox.Size = new System.Drawing.Size(333, 103);
            this.infoBox.TabIndex = 20;
            this.infoBox.TabStop = false;
            this.infoBox.Text = "Персональные данные";
            // 
            // telephoneEditBox
            // 
            this.telephoneEditBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.telephoneEditBox.BeepOnError = true;
            this.telephoneEditBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.telephoneEditBox.Font = new System.Drawing.Font("Century Gothic", 12F);
            this.telephoneEditBox.Location = new System.Drawing.Point(93, 24);
            this.telephoneEditBox.Mask = "8 (999) 000-0000";
            this.telephoneEditBox.Name = "telephoneEditBox";
            this.telephoneEditBox.Size = new System.Drawing.Size(131, 20);
            this.telephoneEditBox.TabIndex = 20;
            // 
            // nameEditBox
            // 
            this.nameEditBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.nameEditBox.BackColor = System.Drawing.Color.White;
            this.nameEditBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.nameEditBox.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.nameEditBox.Location = new System.Drawing.Point(54, 51);
            this.nameEditBox.MaxLength = 48;
            this.nameEditBox.Multiline = true;
            this.nameEditBox.Name = "nameEditBox";
            this.nameEditBox.Size = new System.Drawing.Size(272, 46);
            this.nameEditBox.TabIndex = 21;
            // 
            // nameLabel
            // 
            this.nameLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.nameLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.nameLabel.ForeColor = System.Drawing.Color.Black;
            this.nameLabel.Location = new System.Drawing.Point(6, 51);
            this.nameLabel.Margin = new System.Windows.Forms.Padding(3);
            this.nameLabel.Name = "nameLabel";
            this.nameLabel.Size = new System.Drawing.Size(75, 23);
            this.nameLabel.TabIndex = 16;
            this.nameLabel.Text = "ФИО: ";
            // 
            // telephoneNumberLabel
            // 
            this.telephoneNumberLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.telephoneNumberLabel.AutoEllipsis = true;
            this.telephoneNumberLabel.AutoSize = true;
            this.telephoneNumberLabel.BackColor = System.Drawing.Color.Transparent;
            this.telephoneNumberLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.telephoneNumberLabel.ForeColor = System.Drawing.Color.Black;
            this.telephoneNumberLabel.Location = new System.Drawing.Point(6, 24);
            this.telephoneNumberLabel.Margin = new System.Windows.Forms.Padding(3);
            this.telephoneNumberLabel.Name = "telephoneNumberLabel";
            this.telephoneNumberLabel.Size = new System.Drawing.Size(92, 21);
            this.telephoneNumberLabel.TabIndex = 18;
            this.telephoneNumberLabel.Text = "Телефон: ";
            // 
            // EditForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.ClientSize = new System.Drawing.Size(357, 322);
            this.Controls.Add(this.headPanel);
            this.Controls.Add(this.bodyPanel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "EditForm";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.TopMost = true;
            this.Load += new System.EventHandler(this.EditForm_Load);
            this.headPanel.ResumeLayout(false);
            this.bodyPanel.ResumeLayout(false);
            this.canDeliveryPanel.ResumeLayout(false);
            this.canDeliveryPanel.PerformLayout();
            this.infoBox.ResumeLayout(false);
            this.infoBox.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button cancelButton;
        private System.Windows.Forms.Button saveButton;
        private System.Windows.Forms.Label captionLabel;
        private System.Windows.Forms.Panel headPanel;
        private System.Windows.Forms.Panel bodyPanel;
        private System.Windows.Forms.GroupBox infoBox;
        private System.Windows.Forms.CheckBox verySmallCheck;
        private System.Windows.Forms.Label canDeliveryLabel;
        private System.Windows.Forms.CheckBox extraLargeCheck;
        private System.Windows.Forms.CheckBox veryLargeCheck;
        private System.Windows.Forms.CheckBox largeCheck;
        private System.Windows.Forms.CheckBox averageCheck;
        private System.Windows.Forms.CheckBox smallCheck;
        private System.Windows.Forms.Label helpTitle;
        private System.Windows.Forms.MaskedTextBox telephoneEditBox;
        private System.Windows.Forms.Panel canDeliveryPanel;
        private System.Windows.Forms.TextBox nameEditBox;
        private System.Windows.Forms.Label telephoneNumberLabel;
        private System.Windows.Forms.Label nameLabel;
    }
}