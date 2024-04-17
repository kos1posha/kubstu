
namespace s2_oop_lw_02
{
    partial class MainWindow
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
            this.phoneListLabel = new System.Windows.Forms.Label();
            this.addGroupBox = new System.Windows.Forms.GroupBox();
            this.countTextBox = new System.Windows.Forms.TextBox();
            this.modelTextBox = new System.Windows.Forms.TextBox();
            this.addButton = new System.Windows.Forms.Button();
            this.firmTextBox = new System.Windows.Forms.TextBox();
            this.shCheckBox = new System.Windows.Forms.CheckBox();
            this.countLabel = new System.Windows.Forms.Label();
            this.firmLabel = new System.Windows.Forms.Label();
            this.modelLabel = new System.Windows.Forms.Label();
            this.phoneList = new System.Windows.Forms.TextBox();
            this.deleteGroupBox = new System.Windows.Forms.GroupBox();
            this.numberLabel = new System.Windows.Forms.Label();
            this.numberTextBox = new System.Windows.Forms.TextBox();
            this.deleteButton = new System.Windows.Forms.Button();
            this.exitButton = new System.Windows.Forms.Button();
            this.clearListButton = new System.Windows.Forms.Button();
            this.addGroupBox.SuspendLayout();
            this.deleteGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // phoneListLabel
            // 
            this.phoneListLabel.AutoSize = true;
            this.phoneListLabel.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.phoneListLabel.Location = new System.Drawing.Point(276, 10);
            this.phoneListLabel.Name = "phoneListLabel";
            this.phoneListLabel.Size = new System.Drawing.Size(218, 20);
            this.phoneListLabel.TabIndex = 1;
            this.phoneListLabel.Text = "Список имеющихся устройств";
            // 
            // addGroupBox
            // 
            this.addGroupBox.Controls.Add(this.countTextBox);
            this.addGroupBox.Controls.Add(this.modelTextBox);
            this.addGroupBox.Controls.Add(this.addButton);
            this.addGroupBox.Controls.Add(this.firmTextBox);
            this.addGroupBox.Controls.Add(this.shCheckBox);
            this.addGroupBox.Controls.Add(this.countLabel);
            this.addGroupBox.Controls.Add(this.firmLabel);
            this.addGroupBox.Controls.Add(this.modelLabel);
            this.addGroupBox.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.addGroupBox.Location = new System.Drawing.Point(10, 10);
            this.addGroupBox.Name = "addGroupBox";
            this.addGroupBox.Size = new System.Drawing.Size(261, 133);
            this.addGroupBox.TabIndex = 3;
            this.addGroupBox.TabStop = false;
            this.addGroupBox.Text = "Добавить устройство";
            // 
            // countTextBox
            // 
            this.countTextBox.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.countTextBox.Location = new System.Drawing.Point(103, 77);
            this.countTextBox.Name = "countTextBox";
            this.countTextBox.Size = new System.Drawing.Size(152, 23);
            this.countTextBox.TabIndex = 7;
            // 
            // modelTextBox
            // 
            this.modelTextBox.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.modelTextBox.Location = new System.Drawing.Point(103, 51);
            this.modelTextBox.Name = "modelTextBox";
            this.modelTextBox.Size = new System.Drawing.Size(152, 23);
            this.modelTextBox.TabIndex = 6;
            // 
            // addButton
            // 
            this.addButton.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.addButton.Location = new System.Drawing.Point(103, 102);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(153, 26);
            this.addButton.TabIndex = 3;
            this.addButton.Text = "Добавить\r\n";
            this.addButton.UseVisualStyleBackColor = true;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // firmTextBox
            // 
            this.firmTextBox.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.firmTextBox.Location = new System.Drawing.Point(103, 27);
            this.firmTextBox.Name = "firmTextBox";
            this.firmTextBox.Size = new System.Drawing.Size(152, 22);
            this.firmTextBox.TabIndex = 5;
            // 
            // shCheckBox
            // 
            this.shCheckBox.AutoSize = true;
            this.shCheckBox.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.shCheckBox.Location = new System.Drawing.Point(14, 104);
            this.shCheckBox.Name = "shCheckBox";
            this.shCheckBox.Size = new System.Drawing.Size(49, 23);
            this.shCheckBox.TabIndex = 1;
            this.shCheckBox.Text = "Б/У";
            this.shCheckBox.UseVisualStyleBackColor = true;
            // 
            // countLabel
            // 
            this.countLabel.AutoSize = true;
            this.countLabel.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.countLabel.Location = new System.Drawing.Point(5, 80);
            this.countLabel.Name = "countLabel";
            this.countLabel.Size = new System.Drawing.Size(72, 15);
            this.countLabel.TabIndex = 4;
            this.countLabel.Text = "Количество";
            // 
            // firmLabel
            // 
            this.firmLabel.AutoSize = true;
            this.firmLabel.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.firmLabel.Location = new System.Drawing.Point(5, 29);
            this.firmLabel.Name = "firmLabel";
            this.firmLabel.Size = new System.Drawing.Size(92, 15);
            this.firmLabel.TabIndex = 3;
            this.firmLabel.Text = "Производитель";
            // 
            // modelLabel
            // 
            this.modelLabel.AutoSize = true;
            this.modelLabel.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.modelLabel.Location = new System.Drawing.Point(5, 54);
            this.modelLabel.Name = "modelLabel";
            this.modelLabel.Size = new System.Drawing.Size(50, 15);
            this.modelLabel.TabIndex = 2;
            this.modelLabel.Text = "Модель";
            // 
            // phoneList
            // 
            this.phoneList.Location = new System.Drawing.Point(276, 30);
            this.phoneList.Multiline = true;
            this.phoneList.Name = "phoneList";
            this.phoneList.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.phoneList.Size = new System.Drawing.Size(234, 158);
            this.phoneList.TabIndex = 4;
            // 
            // deleteGroupBox
            // 
            this.deleteGroupBox.Controls.Add(this.numberLabel);
            this.deleteGroupBox.Controls.Add(this.numberTextBox);
            this.deleteGroupBox.Controls.Add(this.deleteButton);
            this.deleteGroupBox.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.deleteGroupBox.Location = new System.Drawing.Point(10, 146);
            this.deleteGroupBox.Name = "deleteGroupBox";
            this.deleteGroupBox.Size = new System.Drawing.Size(261, 82);
            this.deleteGroupBox.TabIndex = 8;
            this.deleteGroupBox.TabStop = false;
            this.deleteGroupBox.Text = "Удалить устройство";
            // 
            // numberLabel
            // 
            this.numberLabel.AutoSize = true;
            this.numberLabel.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.numberLabel.Location = new System.Drawing.Point(5, 23);
            this.numberLabel.Name = "numberLabel";
            this.numberLabel.Size = new System.Drawing.Size(95, 15);
            this.numberLabel.TabIndex = 7;
            this.numberLabel.Text = "Номер в списке";
            // 
            // numberTextBox
            // 
            this.numberTextBox.Font = new System.Drawing.Font("Segoe UI", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.numberTextBox.Location = new System.Drawing.Point(102, 21);
            this.numberTextBox.Name = "numberTextBox";
            this.numberTextBox.Size = new System.Drawing.Size(153, 23);
            this.numberTextBox.TabIndex = 6;
            // 
            // deleteButton
            // 
            this.deleteButton.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.deleteButton.Location = new System.Drawing.Point(102, 51);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(153, 26);
            this.deleteButton.TabIndex = 4;
            this.deleteButton.Text = "Удалить\r\n\r\n";
            this.deleteButton.UseVisualStyleBackColor = true;
            this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // exitButton
            // 
            this.exitButton.Location = new System.Drawing.Point(399, 197);
            this.exitButton.Name = "exitButton";
            this.exitButton.Size = new System.Drawing.Size(111, 26);
            this.exitButton.TabIndex = 9;
            this.exitButton.Text = "Завершить работу";
            this.exitButton.UseVisualStyleBackColor = true;
            this.exitButton.Click += new System.EventHandler(this.exitButton_Click);
            // 
            // clearListButton
            // 
            this.clearListButton.Location = new System.Drawing.Point(276, 198);
            this.clearListButton.Name = "clearListButton";
            this.clearListButton.Size = new System.Drawing.Size(111, 26);
            this.clearListButton.TabIndex = 10;
            this.clearListButton.Text = "Очистить список";
            this.clearListButton.UseVisualStyleBackColor = true;
            this.clearListButton.Click += new System.EventHandler(this.clearListButton_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(519, 234);
            this.ControlBox = false;
            this.Controls.Add(this.clearListButton);
            this.Controls.Add(this.exitButton);
            this.Controls.Add(this.deleteGroupBox);
            this.Controls.Add(this.phoneList);
            this.Controls.Add(this.addGroupBox);
            this.Controls.Add(this.phoneListLabel);
            this.Name = "MainWindow";
            this.Text = "Хлеб, колбаса и гвозди";
            this.addGroupBox.ResumeLayout(false);
            this.addGroupBox.PerformLayout();
            this.deleteGroupBox.ResumeLayout(false);
            this.deleteGroupBox.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label phoneListLabel;
        private System.Windows.Forms.GroupBox addGroupBox;
        private System.Windows.Forms.TextBox phoneList;
        private System.Windows.Forms.Label modelLabel;
        private System.Windows.Forms.CheckBox shCheckBox;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Label firmLabel;
        private System.Windows.Forms.Label countLabel;
        private System.Windows.Forms.TextBox countTextBox;
        private System.Windows.Forms.TextBox modelTextBox;
        private System.Windows.Forms.TextBox firmTextBox;
        private System.Windows.Forms.GroupBox deleteGroupBox;
        private System.Windows.Forms.Button deleteButton;
        private System.Windows.Forms.Label numberLabel;
        private System.Windows.Forms.TextBox numberTextBox;
        private System.Windows.Forms.Button exitButton;
        private System.Windows.Forms.Button clearListButton;
    }
}

