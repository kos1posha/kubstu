
namespace BizyaevKursach
{
    partial class NewOrder
    {
        /// <summary> 
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary> 
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором компонентов

        /// <summary> 
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.paymentMethodLabel = new System.Windows.Forms.Label();
            this.receiverNameLabel = new System.Windows.Forms.Label();
            this.senderFirmLabel = new System.Windows.Forms.Label();
            this.weightLabel = new System.Windows.Forms.Label();
            this.createButton = new System.Windows.Forms.Button();
            this.headPanel = new System.Windows.Forms.Panel();
            this.deliveryTimeTextBox = new System.Windows.Forms.MaskedTextBox();
            this.timeLabel = new System.Windows.Forms.Label();
            this.numberLabel = new System.Windows.Forms.Label();
            this.deliveryAddressLabel = new System.Windows.Forms.Label();
            this.cancelButton = new System.Windows.Forms.Button();
            this.bodyPanel = new System.Windows.Forms.Panel();
            this.costTextBox = new System.Windows.Forms.MaskedTextBox();
            this.priceCostLabel = new System.Windows.Forms.Label();
            this.paymentMethodComboBox = new System.Windows.Forms.ComboBox();
            this.receiverNameTextBox = new System.Windows.Forms.TextBox();
            this.deliveryAddressTextBox = new System.Windows.Forms.TextBox();
            this.receivingAddressTextBox = new System.Windows.Forms.TextBox();
            this.senderFirmTextBox = new System.Windows.Forms.TextBox();
            this.weightTextBox = new System.Windows.Forms.MaskedTextBox();
            this.receivingAddressLabel = new System.Windows.Forms.Label();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.headPanel.SuspendLayout();
            this.bodyPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // paymentMethodLabel
            // 
            this.paymentMethodLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.paymentMethodLabel.AutoEllipsis = true;
            this.paymentMethodLabel.AutoSize = true;
            this.paymentMethodLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.paymentMethodLabel.ForeColor = System.Drawing.Color.Black;
            this.paymentMethodLabel.Location = new System.Drawing.Point(3, 194);
            this.paymentMethodLabel.Name = "paymentMethodLabel";
            this.paymentMethodLabel.Size = new System.Drawing.Size(138, 18);
            this.paymentMethodLabel.TabIndex = 18;
            this.paymentMethodLabel.Text = "Способ оплаты: ";
            // 
            // receiverNameLabel
            // 
            this.receiverNameLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.receiverNameLabel.AutoEllipsis = true;
            this.receiverNameLabel.AutoSize = true;
            this.receiverNameLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.receiverNameLabel.ForeColor = System.Drawing.Color.Black;
            this.receiverNameLabel.Location = new System.Drawing.Point(3, 172);
            this.receiverNameLabel.Name = "receiverNameLabel";
            this.receiverNameLabel.Size = new System.Drawing.Size(138, 18);
            this.receiverNameLabel.TabIndex = 16;
            this.receiverNameLabel.Text = "Имя получателя: \r\n";
            // 
            // senderFirmLabel
            // 
            this.senderFirmLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.senderFirmLabel.AutoEllipsis = true;
            this.senderFirmLabel.AutoSize = true;
            this.senderFirmLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.senderFirmLabel.ForeColor = System.Drawing.Color.Black;
            this.senderFirmLabel.Location = new System.Drawing.Point(3, 21);
            this.senderFirmLabel.Name = "senderFirmLabel";
            this.senderFirmLabel.Size = new System.Drawing.Size(172, 18);
            this.senderFirmLabel.TabIndex = 14;
            this.senderFirmLabel.Text = "Фирма-отправитель: ";
            // 
            // weightLabel
            // 
            this.weightLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.weightLabel.AutoEllipsis = true;
            this.weightLabel.AutoSize = true;
            this.weightLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.weightLabel.ForeColor = System.Drawing.Color.Black;
            this.weightLabel.Location = new System.Drawing.Point(3, 0);
            this.weightLabel.Name = "weightLabel";
            this.weightLabel.Size = new System.Drawing.Size(41, 18);
            this.weightLabel.TabIndex = 12;
            this.weightLabel.Text = "Вес:";
            // 
            // createButton
            // 
            this.createButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.createButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(188)))), ((int)(((byte)(201)))), ((int)(((byte)(135)))));
            this.createButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.createButton.DialogResult = System.Windows.Forms.DialogResult.Yes;
            this.createButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.createButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(166)))), ((int)(((byte)(183)))), ((int)(((byte)(96)))));
            this.createButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.createButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.createButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.createButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.createButton.Location = new System.Drawing.Point(159, 248);
            this.createButton.Name = "createButton";
            this.createButton.Size = new System.Drawing.Size(107, 33);
            this.createButton.TabIndex = 11;
            this.createButton.TabStop = false;
            this.createButton.Text = "Создать";
            this.createButton.UseVisualStyleBackColor = false;
            this.createButton.Click += new System.EventHandler(this.createButton_Click);
            // 
            // headPanel
            // 
            this.headPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.headPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.headPanel.Controls.Add(this.deliveryTimeTextBox);
            this.headPanel.Controls.Add(this.timeLabel);
            this.headPanel.Controls.Add(this.numberLabel);
            this.headPanel.Location = new System.Drawing.Point(1, 1);
            this.headPanel.Name = "headPanel";
            this.headPanel.Size = new System.Drawing.Size(385, 57);
            this.headPanel.TabIndex = 19;
            // 
            // deliveryTimeTextBox
            // 
            this.deliveryTimeTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.deliveryTimeTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.deliveryTimeTextBox.Font = new System.Drawing.Font("Century Gothic", 12.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))));
            this.deliveryTimeTextBox.Location = new System.Drawing.Point(118, 30);
            this.deliveryTimeTextBox.Mask = "до 00.00.0000";
            this.deliveryTimeTextBox.Name = "deliveryTimeTextBox";
            this.deliveryTimeTextBox.Size = new System.Drawing.Size(256, 21);
            this.deliveryTimeTextBox.TabIndex = 23;
            // 
            // timeLabel
            // 
            this.timeLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.timeLabel.AutoSize = true;
            this.timeLabel.Font = new System.Drawing.Font("Century Gothic", 12.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.timeLabel.ForeColor = System.Drawing.Color.Black;
            this.timeLabel.Location = new System.Drawing.Point(3, 30);
            this.timeLabel.Name = "timeLabel";
            this.timeLabel.Size = new System.Drawing.Size(117, 21);
            this.timeLabel.TabIndex = 11;
            this.timeLabel.Text = "от __.__.____";
            // 
            // numberLabel
            // 
            this.numberLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.numberLabel.Font = new System.Drawing.Font("Century Gothic", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.numberLabel.ForeColor = System.Drawing.Color.Black;
            this.numberLabel.Location = new System.Drawing.Point(3, 7);
            this.numberLabel.Name = "numberLabel";
            this.numberLabel.Size = new System.Drawing.Size(320, 23);
            this.numberLabel.TabIndex = 10;
            this.numberLabel.Text = "Заказ номер __________";
            // 
            // deliveryAddressLabel
            // 
            this.deliveryAddressLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.deliveryAddressLabel.AutoEllipsis = true;
            this.deliveryAddressLabel.AutoSize = true;
            this.deliveryAddressLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.deliveryAddressLabel.ForeColor = System.Drawing.Color.Black;
            this.deliveryAddressLabel.Location = new System.Drawing.Point(4, 107);
            this.deliveryAddressLabel.Name = "deliveryAddressLabel";
            this.deliveryAddressLabel.Size = new System.Drawing.Size(140, 18);
            this.deliveryAddressLabel.TabIndex = 20;
            this.deliveryAddressLabel.Text = "Адрес доставки:";
            // 
            // cancelButton
            // 
            this.cancelButton.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.cancelButton.BackColor = System.Drawing.Color.LightCoral;
            this.cancelButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.cancelButton.DialogResult = System.Windows.Forms.DialogResult.No;
            this.cancelButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.cancelButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.cancelButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Firebrick;
            this.cancelButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.cancelButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.cancelButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.cancelButton.Location = new System.Drawing.Point(272, 248);
            this.cancelButton.Name = "cancelButton";
            this.cancelButton.Size = new System.Drawing.Size(107, 33);
            this.cancelButton.TabIndex = 21;
            this.cancelButton.TabStop = false;
            this.cancelButton.Text = "Отменить";
            this.cancelButton.UseVisualStyleBackColor = false;
            this.cancelButton.Click += new System.EventHandler(this.cancelButton_Click);
            // 
            // bodyPanel
            // 
            this.bodyPanel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.bodyPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.bodyPanel.Controls.Add(this.costTextBox);
            this.bodyPanel.Controls.Add(this.priceCostLabel);
            this.bodyPanel.Controls.Add(this.paymentMethodComboBox);
            this.bodyPanel.Controls.Add(this.receiverNameTextBox);
            this.bodyPanel.Controls.Add(this.deliveryAddressTextBox);
            this.bodyPanel.Controls.Add(this.receivingAddressTextBox);
            this.bodyPanel.Controls.Add(this.senderFirmTextBox);
            this.bodyPanel.Controls.Add(this.weightTextBox);
            this.bodyPanel.Controls.Add(this.createButton);
            this.bodyPanel.Controls.Add(this.cancelButton);
            this.bodyPanel.Controls.Add(this.weightLabel);
            this.bodyPanel.Controls.Add(this.senderFirmLabel);
            this.bodyPanel.Controls.Add(this.receivingAddressLabel);
            this.bodyPanel.Controls.Add(this.deliveryAddressLabel);
            this.bodyPanel.Controls.Add(this.receiverNameLabel);
            this.bodyPanel.Controls.Add(this.paymentMethodLabel);
            this.bodyPanel.Location = new System.Drawing.Point(1, 58);
            this.bodyPanel.Name = "bodyPanel";
            this.bodyPanel.Size = new System.Drawing.Size(385, 337);
            this.bodyPanel.TabIndex = 22;
            // 
            // costTextBox
            // 
            this.costTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.costTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.costTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.costTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.costTextBox.Location = new System.Drawing.Point(108, 223);
            this.costTextBox.Mask = "00000";
            this.costTextBox.Name = "costTextBox";
            this.costTextBox.Size = new System.Drawing.Size(271, 19);
            this.costTextBox.TabIndex = 30;
            this.costTextBox.ValidatingType = typeof(int);
            // 
            // priceCostLabel
            // 
            this.priceCostLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.priceCostLabel.AutoEllipsis = true;
            this.priceCostLabel.AutoSize = true;
            this.priceCostLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.priceCostLabel.ForeColor = System.Drawing.Color.Black;
            this.priceCostLabel.Location = new System.Drawing.Point(4, 223);
            this.priceCostLabel.Name = "priceCostLabel";
            this.priceCostLabel.Size = new System.Drawing.Size(108, 18);
            this.priceCostLabel.TabIndex = 29;
            this.priceCostLabel.Text = "Цена заказа:";
            // 
            // paymentMethodComboBox
            // 
            this.paymentMethodComboBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.paymentMethodComboBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.paymentMethodComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.paymentMethodComboBox.FormattingEnabled = true;
            this.paymentMethodComboBox.Items.AddRange(new object[] {
            "наличная оплата",
            "безналичная оплата"});
            this.paymentMethodComboBox.Location = new System.Drawing.Point(136, 193);
            this.paymentMethodComboBox.Name = "paymentMethodComboBox";
            this.paymentMethodComboBox.Size = new System.Drawing.Size(243, 21);
            this.paymentMethodComboBox.TabIndex = 28;
            // 
            // receiverNameTextBox
            // 
            this.receiverNameTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.receiverNameTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.receiverNameTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.receiverNameTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.receiverNameTextBox.Location = new System.Drawing.Point(136, 172);
            this.receiverNameTextBox.Name = "receiverNameTextBox";
            this.receiverNameTextBox.Size = new System.Drawing.Size(246, 19);
            this.receiverNameTextBox.TabIndex = 27;
            // 
            // deliveryAddressTextBox
            // 
            this.deliveryAddressTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.deliveryAddressTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.deliveryAddressTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.deliveryAddressTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.deliveryAddressTextBox.Location = new System.Drawing.Point(3, 128);
            this.deliveryAddressTextBox.Multiline = true;
            this.deliveryAddressTextBox.Name = "deliveryAddressTextBox";
            this.deliveryAddressTextBox.Size = new System.Drawing.Size(376, 41);
            this.deliveryAddressTextBox.TabIndex = 26;
            // 
            // receivingAddressTextBox
            // 
            this.receivingAddressTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.receivingAddressTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.receivingAddressTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.receivingAddressTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.receivingAddressTextBox.Location = new System.Drawing.Point(6, 63);
            this.receivingAddressTextBox.Multiline = true;
            this.receivingAddressTextBox.Name = "receivingAddressTextBox";
            this.receivingAddressTextBox.Size = new System.Drawing.Size(376, 41);
            this.receivingAddressTextBox.TabIndex = 25;
            // 
            // senderFirmTextBox
            // 
            this.senderFirmTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.senderFirmTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.senderFirmTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.senderFirmTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.senderFirmTextBox.Location = new System.Drawing.Point(173, 21);
            this.senderFirmTextBox.Name = "senderFirmTextBox";
            this.senderFirmTextBox.Size = new System.Drawing.Size(209, 19);
            this.senderFirmTextBox.TabIndex = 24;
            // 
            // weightTextBox
            // 
            this.weightTextBox.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.weightTextBox.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.weightTextBox.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.weightTextBox.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold);
            this.weightTextBox.Location = new System.Drawing.Point(50, 0);
            this.weightTextBox.Mask = "00.00 кг";
            this.weightTextBox.Name = "weightTextBox";
            this.weightTextBox.Size = new System.Drawing.Size(62, 19);
            this.weightTextBox.TabIndex = 22;
            // 
            // receivingAddressLabel
            // 
            this.receivingAddressLabel.Anchor = System.Windows.Forms.AnchorStyles.Top;
            this.receivingAddressLabel.AutoEllipsis = true;
            this.receivingAddressLabel.AutoSize = true;
            this.receivingAddressLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.receivingAddressLabel.ForeColor = System.Drawing.Color.Black;
            this.receivingAddressLabel.Location = new System.Drawing.Point(3, 42);
            this.receivingAddressLabel.Name = "receivingAddressLabel";
            this.receivingAddressLabel.Size = new System.Drawing.Size(217, 18);
            this.receivingAddressLabel.TabIndex = 15;
            this.receivingAddressLabel.Text = "Адрес получения посылки:";
            // 
            // timer
            // 
            this.timer.Interval = 1000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // NewOrder
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.ClientSize = new System.Drawing.Size(387, 348);
            this.Controls.Add(this.bodyPanel);
            this.Controls.Add(this.headPanel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "NewOrder";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.Load += new System.EventHandler(this.NewOrder_Load);
            this.headPanel.ResumeLayout(false);
            this.headPanel.PerformLayout();
            this.bodyPanel.ResumeLayout(false);
            this.bodyPanel.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label paymentMethodLabel;
        private System.Windows.Forms.Label receiverNameLabel;
        private System.Windows.Forms.Label senderFirmLabel;
        private System.Windows.Forms.Label weightLabel;
        private System.Windows.Forms.Button createButton;
        private System.Windows.Forms.Panel headPanel;
        private System.Windows.Forms.Label deliveryAddressLabel;
        private System.Windows.Forms.Button cancelButton;
        private System.Windows.Forms.Panel bodyPanel;
        private System.Windows.Forms.Label receivingAddressLabel;
        private System.Windows.Forms.MaskedTextBox deliveryTimeTextBox;
        private System.Windows.Forms.Label timeLabel;
        private System.Windows.Forms.Label numberLabel;
        private System.Windows.Forms.MaskedTextBox weightTextBox;
        private System.Windows.Forms.ComboBox paymentMethodComboBox;
        private System.Windows.Forms.TextBox receiverNameTextBox;
        private System.Windows.Forms.TextBox deliveryAddressTextBox;
        private System.Windows.Forms.TextBox receivingAddressTextBox;
        private System.Windows.Forms.TextBox senderFirmTextBox;
        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.Label priceCostLabel;
        private System.Windows.Forms.MaskedTextBox costTextBox;
    }
}