
namespace BizyaevKursach
{
    partial class OrdersList
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
            this.closeButton = new System.Windows.Forms.Button();
            this.captionLabel = new System.Windows.Forms.Label();
            this.headPanel = new System.Windows.Forms.Panel();
            this.currentOrdersList = new System.Windows.Forms.TableLayoutPanel();
            this.bodyPanel = new System.Windows.Forms.Panel();
            this.headPanel.SuspendLayout();
            this.bodyPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // closeButton
            // 
            this.closeButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
            this.closeButton.BackColor = System.Drawing.Color.LightCoral;
            this.closeButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.closeButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.IndianRed;
            this.closeButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Firebrick;
            this.closeButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.closeButton.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.closeButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(230)))), ((int)(((byte)(184)))));
            this.closeButton.Location = new System.Drawing.Point(304, 1);
            this.closeButton.Name = "closeButton";
            this.closeButton.Size = new System.Drawing.Size(122, 33);
            this.closeButton.TabIndex = 1;
            this.closeButton.Text = "Закрыть";
            this.closeButton.UseVisualStyleBackColor = false;
            this.closeButton.Click += new System.EventHandler(this.closeButton_Click);
            // 
            // captionLabel
            // 
            this.captionLabel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.captionLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.captionLabel.Location = new System.Drawing.Point(3, 9);
            this.captionLabel.Name = "captionLabel";
            this.captionLabel.Size = new System.Drawing.Size(423, 22);
            this.captionLabel.TabIndex = 3;
            this.captionLabel.Text = "Скрытые заказы";
            // 
            // headPanel
            // 
            this.headPanel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.headPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(142)))), ((int)(((byte)(159)))), ((int)(((byte)(72)))));
            this.headPanel.Controls.Add(this.closeButton);
            this.headPanel.Controls.Add(this.captionLabel);
            this.headPanel.Location = new System.Drawing.Point(1, 1);
            this.headPanel.Name = "headPanel";
            this.headPanel.Size = new System.Drawing.Size(429, 36);
            this.headPanel.TabIndex = 4;
            // 
            // currentOrdersList
            // 
            this.currentOrdersList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.currentOrdersList.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Outset;
            this.currentOrdersList.ColumnCount = 1;
            this.currentOrdersList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.currentOrdersList.Dock = System.Windows.Forms.DockStyle.Top;
            this.currentOrdersList.Location = new System.Drawing.Point(0, 0);
            this.currentOrdersList.Margin = new System.Windows.Forms.Padding(0);
            this.currentOrdersList.Name = "currentOrdersList";
            this.currentOrdersList.RowCount = 1;
            this.currentOrdersList.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.currentOrdersList.Size = new System.Drawing.Size(429, 0);
            this.currentOrdersList.TabIndex = 4;
            this.currentOrdersList.ControlAdded += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlAdded);
            this.currentOrdersList.ControlRemoved += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlRemoved);
            // 
            // bodyPanel
            // 
            this.bodyPanel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.bodyPanel.AutoScroll = true;
            this.bodyPanel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.bodyPanel.Controls.Add(this.currentOrdersList);
            this.bodyPanel.Location = new System.Drawing.Point(1, 37);
            this.bodyPanel.Name = "bodyPanel";
            this.bodyPanel.Size = new System.Drawing.Size(429, 312);
            this.bodyPanel.TabIndex = 6;
            // 
            // OrdersList
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.Controls.Add(this.headPanel);
            this.Controls.Add(this.bodyPanel);
            this.Name = "OrdersList";
            this.Size = new System.Drawing.Size(431, 350);
            this.VisibleChanged += new System.EventHandler(this.closeButton_Click);
            this.headPanel.ResumeLayout(false);
            this.bodyPanel.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button closeButton;
        private System.Windows.Forms.Label captionLabel;
        private System.Windows.Forms.Panel headPanel;
        private System.Windows.Forms.TableLayoutPanel currentOrdersList;
        private System.Windows.Forms.Panel bodyPanel;
    }
}
