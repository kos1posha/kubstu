
namespace BizyaevKursach
{
    partial class OrderPanel
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
            this.paymentMethodLabel = new System.Windows.Forms.Label();
            this.receiverNameLabel = new System.Windows.Forms.Label();
            this.senderFirmLabel = new System.Windows.Forms.Label();
            this.sizeLabel = new System.Windows.Forms.Label();
            this.weightLabel = new System.Windows.Forms.Label();
            this.firstButton = new System.Windows.Forms.Button();
            this.numberLabel = new System.Windows.Forms.Label();
            this.headPanel = new System.Windows.Forms.Panel();
            this.actualDeliveryTimeLabel = new System.Windows.Forms.Label();
            this.timeLabel = new System.Windows.Forms.Label();
            this.infoButton = new System.Windows.Forms.Button();
            this.deliveryAddressLabel = new System.Windows.Forms.Label();
            this.secondButton = new System.Windows.Forms.Button();
            this.bodyPanel = new System.Windows.Forms.Panel();
            this.receivingAddressLabel = new System.Windows.Forms.Label();
            this.headPanel.SuspendLayout();
            this.bodyPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // paymentMethodLabel
            // 
            this.paymentMethodLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.paymentMethodLabel.AutoEllipsis = true;
            this.paymentMethodLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.paymentMethodLabel.ForeColor = System.Drawing.Color.Black;
            this.paymentMethodLabel.Location = new System.Drawing.Point(4, 143);
            this.paymentMethodLabel.Name = "paymentMethodLabel";
            this.paymentMethodLabel.Size = new System.Drawing.Size(391, 21);
            this.paymentMethodLabel.TabIndex = 18;
            this.paymentMethodLabel.Text = "Способ оплаты: ";
            // 
            // receiverNameLabel
            // 
            this.receiverNameLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.receiverNameLabel.AutoEllipsis = true;
            this.receiverNameLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.receiverNameLabel.ForeColor = System.Drawing.Color.Black;
            this.receiverNameLabel.Location = new System.Drawing.Point(4, 122);
            this.receiverNameLabel.Name = "receiverNameLabel";
            this.receiverNameLabel.Size = new System.Drawing.Size(388, 21);
            this.receiverNameLabel.TabIndex = 16;
            this.receiverNameLabel.Text = "Имя получателя: \r\n";
            // 
            // senderFirmLabel
            // 
            this.senderFirmLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.senderFirmLabel.AutoEllipsis = true;
            this.senderFirmLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.senderFirmLabel.ForeColor = System.Drawing.Color.Black;
            this.senderFirmLabel.Location = new System.Drawing.Point(3, 21);
            this.senderFirmLabel.Name = "senderFirmLabel";
            this.senderFirmLabel.Size = new System.Drawing.Size(388, 21);
            this.senderFirmLabel.TabIndex = 14;
            this.senderFirmLabel.Text = "Фирма-отправитель: ";
            // 
            // sizeLabel
            // 
            this.sizeLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.sizeLabel.AutoEllipsis = true;
            this.sizeLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.sizeLabel.ForeColor = System.Drawing.Color.Black;
            this.sizeLabel.Location = new System.Drawing.Point(111, 0);
            this.sizeLabel.Name = "sizeLabel";
            this.sizeLabel.Size = new System.Drawing.Size(280, 18);
            this.sizeLabel.TabIndex = 13;
            this.sizeLabel.Text = "Размер: ";
            // 
            // weightLabel
            // 
            this.weightLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.weightLabel.AutoEllipsis = true;
            this.weightLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.weightLabel.ForeColor = System.Drawing.Color.Black;
            this.weightLabel.Location = new System.Drawing.Point(3, 0);
            this.weightLabel.Name = "weightLabel";
            this.weightLabel.Size = new System.Drawing.Size(102, 21);
            this.weightLabel.TabIndex = 12;
            this.weightLabel.Text = "Вес: __.__ кг";
            // 
            // firstButton
            // 
            this.firstButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.firstButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(188)))), ((int)(((byte)(201)))), ((int)(((byte)(135)))));
            this.firstButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.firstButton.DialogResult = System.Windows.Forms.DialogResult.Yes;
            this.firstButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.firstButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(166)))), ((int)(((byte)(183)))), ((int)(((byte)(96)))));
            this.firstButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.firstButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.firstButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.firstButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.firstButton.Location = new System.Drawing.Point(143, 165);
            this.firstButton.Name = "firstButton";
            this.firstButton.Size = new System.Drawing.Size(123, 33);
            this.firstButton.TabIndex = 11;
            this.firstButton.TabStop = false;
            this.firstButton.UseVisualStyleBackColor = false;
            // 
            // numberLabel
            // 
            this.numberLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.numberLabel.Font = new System.Drawing.Font("Century Gothic", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.numberLabel.ForeColor = System.Drawing.Color.Black;
            this.numberLabel.Location = new System.Drawing.Point(3, 7);
            this.numberLabel.Name = "numberLabel";
            this.numberLabel.Size = new System.Drawing.Size(336, 23);
            this.numberLabel.TabIndex = 10;
            this.numberLabel.Text = "Заказ номер __________";
            // 
            // headPanel
            // 
            this.headPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.headPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.headPanel.Controls.Add(this.actualDeliveryTimeLabel);
            this.headPanel.Controls.Add(this.timeLabel);
            this.headPanel.Controls.Add(this.infoButton);
            this.headPanel.Controls.Add(this.numberLabel);
            this.headPanel.Location = new System.Drawing.Point(1, 1);
            this.headPanel.Name = "headPanel";
            this.headPanel.Size = new System.Drawing.Size(401, 75);
            this.headPanel.TabIndex = 19;
            // 
            // actualDeliveryTimeLabel
            // 
            this.actualDeliveryTimeLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.actualDeliveryTimeLabel.Font = new System.Drawing.Font("Century Gothic", 12.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.actualDeliveryTimeLabel.ForeColor = System.Drawing.Color.Black;
            this.actualDeliveryTimeLabel.Location = new System.Drawing.Point(3, 50);
            this.actualDeliveryTimeLabel.Name = "actualDeliveryTimeLabel";
            this.actualDeliveryTimeLabel.Size = new System.Drawing.Size(336, 23);
            this.actualDeliveryTimeLabel.TabIndex = 18;
            this.actualDeliveryTimeLabel.Text = "доставлен __.__.____";
            // 
            // timeLabel
            // 
            this.timeLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.timeLabel.Font = new System.Drawing.Font("Century Gothic", 12.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.timeLabel.ForeColor = System.Drawing.Color.Black;
            this.timeLabel.Location = new System.Drawing.Point(3, 30);
            this.timeLabel.Name = "timeLabel";
            this.timeLabel.Size = new System.Drawing.Size(336, 23);
            this.timeLabel.TabIndex = 11;
            this.timeLabel.Text = "от __.__.____ до __.__.____";
            // 
            // infoButton
            // 
            this.infoButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.infoButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(188)))), ((int)(((byte)(201)))), ((int)(((byte)(135)))));
            this.infoButton.BackgroundImage = global::BizyaevKursach.Properties.Resources.orders_addit_icon_color_inv;
            this.infoButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.infoButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.infoButton.FlatAppearance.BorderSize = 0;
            this.infoButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(166)))), ((int)(((byte)(183)))), ((int)(((byte)(96)))));
            this.infoButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.infoButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.infoButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.infoButton.ForeColor = System.Drawing.Color.Black;
            this.infoButton.Location = new System.Drawing.Point(352, 7);
            this.infoButton.Name = "infoButton";
            this.infoButton.Size = new System.Drawing.Size(40, 40);
            this.infoButton.TabIndex = 17;
            this.infoButton.TabStop = false;
            this.infoButton.UseVisualStyleBackColor = false;
            this.infoButton.Click += new System.EventHandler(this.infoButton_Click);
            this.infoButton.Paint += new System.Windows.Forms.PaintEventHandler(this.infoButton_Paint);
            // 
            // deliveryAddressLabel
            // 
            this.deliveryAddressLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.deliveryAddressLabel.AutoEllipsis = true;
            this.deliveryAddressLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.deliveryAddressLabel.ForeColor = System.Drawing.Color.Black;
            this.deliveryAddressLabel.Location = new System.Drawing.Point(3, 82);
            this.deliveryAddressLabel.Name = "deliveryAddressLabel";
            this.deliveryAddressLabel.Size = new System.Drawing.Size(391, 40);
            this.deliveryAddressLabel.TabIndex = 20;
            this.deliveryAddressLabel.Text = "Адрес доставки:";
            // 
            // secondButton
            // 
            this.secondButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.secondButton.BackColor = System.Drawing.Color.LightCoral;
            this.secondButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.secondButton.DialogResult = System.Windows.Forms.DialogResult.No;
            this.secondButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.secondButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.secondButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Firebrick;
            this.secondButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.secondButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.secondButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.secondButton.Location = new System.Drawing.Point(271, 165);
            this.secondButton.Name = "secondButton";
            this.secondButton.Size = new System.Drawing.Size(123, 33);
            this.secondButton.TabIndex = 21;
            this.secondButton.TabStop = false;
            this.secondButton.UseVisualStyleBackColor = false;
            // 
            // bodyPanel
            // 
            this.bodyPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bodyPanel.BackColor = System.Drawing.SystemColors.InactiveCaption;
            this.bodyPanel.Controls.Add(this.firstButton);
            this.bodyPanel.Controls.Add(this.secondButton);
            this.bodyPanel.Controls.Add(this.weightLabel);
            this.bodyPanel.Controls.Add(this.sizeLabel);
            this.bodyPanel.Controls.Add(this.senderFirmLabel);
            this.bodyPanel.Controls.Add(this.receivingAddressLabel);
            this.bodyPanel.Controls.Add(this.deliveryAddressLabel);
            this.bodyPanel.Controls.Add(this.receiverNameLabel);
            this.bodyPanel.Controls.Add(this.paymentMethodLabel);
            this.bodyPanel.Location = new System.Drawing.Point(1, 76);
            this.bodyPanel.Name = "bodyPanel";
            this.bodyPanel.Size = new System.Drawing.Size(401, 203);
            this.bodyPanel.TabIndex = 22;
            // 
            // receivingAddressLabel
            // 
            this.receivingAddressLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.receivingAddressLabel.AutoEllipsis = true;
            this.receivingAddressLabel.Font = new System.Drawing.Font("Century Gothic", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.receivingAddressLabel.ForeColor = System.Drawing.Color.Black;
            this.receivingAddressLabel.Location = new System.Drawing.Point(3, 42);
            this.receivingAddressLabel.Name = "receivingAddressLabel";
            this.receivingAddressLabel.Size = new System.Drawing.Size(391, 40);
            this.receivingAddressLabel.TabIndex = 15;
            this.receivingAddressLabel.Text = "Адрес получения посылки:";
            // 
            // OrderPanel
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.Controls.Add(this.bodyPanel);
            this.Controls.Add(this.headPanel);
            this.Name = "OrderPanel";
            this.Size = new System.Drawing.Size(403, 280);
            this.Load += new System.EventHandler(this.OrderPanel_Load);
            this.headPanel.ResumeLayout(false);
            this.bodyPanel.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label paymentMethodLabel;
        private System.Windows.Forms.Label receiverNameLabel;
        private System.Windows.Forms.Label senderFirmLabel;
        private System.Windows.Forms.Label sizeLabel;
        private System.Windows.Forms.Label weightLabel;
        private System.Windows.Forms.Button firstButton;
        private System.Windows.Forms.Label numberLabel;
        private System.Windows.Forms.Panel headPanel;
        private System.Windows.Forms.Label timeLabel;
        private System.Windows.Forms.Label deliveryAddressLabel;
        private System.Windows.Forms.Button secondButton;
        private System.Windows.Forms.Button infoButton;
        private System.Windows.Forms.Panel bodyPanel;
        private System.Windows.Forms.Label actualDeliveryTimeLabel;
        private System.Windows.Forms.Label receivingAddressLabel;
    }
}
