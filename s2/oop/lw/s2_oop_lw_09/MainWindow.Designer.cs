
namespace s2_oop_lw_09
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
            this.firstFormTextBox = new System.Windows.Forms.TextBox();
            this.firstFormLabel = new System.Windows.Forms.Label();
            this.secondFormLabel = new System.Windows.Forms.Label();
            this.thirdFormLabel = new System.Windows.Forms.Label();
            this.addButton = new System.Windows.Forms.Button();
            this.deleteButton = new System.Windows.Forms.Button();
            this.secondFormTextBox = new System.Windows.Forms.TextBox();
            this.thirdFormTextBox = new System.Windows.Forms.TextBox();
            this.resultListGridView = new System.Windows.Forms.DataGridView();
            this.dataGridViewTextBoxColumn4 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn5 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn6 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.enterListLabel = new System.Windows.Forms.Label();
            this.resultListLabel = new System.Windows.Forms.Label();
            this.resultButton = new System.Windows.Forms.Button();
            this.enterListGridView = new System.Windows.Forms.DataGridView();
            this.dataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.mainGroupBox = new System.Windows.Forms.GroupBox();
            this.taskLabel = new System.Windows.Forms.Label();
            this.clearEnterListButton = new System.Windows.Forms.Button();
            this.clearResultListButton = new System.Windows.Forms.Button();
            this.saveMenuStrip = new System.Windows.Forms.MenuStrip();
            this.serializationToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.serializationSaveButton = new System.Windows.Forms.ToolStripMenuItem();
            this.serializationLoadButton = new System.Windows.Forms.ToolStripMenuItem();
            this.commonToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.commonSaveButton = new System.Windows.Forms.ToolStripMenuItem();
            this.commonLoadButton = new System.Windows.Forms.ToolStripMenuItem();
            ((System.ComponentModel.ISupportInitialize)(this.resultListGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.enterListGridView)).BeginInit();
            this.mainGroupBox.SuspendLayout();
            this.saveMenuStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // firstFormTextBox
            // 
            this.firstFormTextBox.Location = new System.Drawing.Point(37, 27);
            this.firstFormTextBox.Name = "firstFormTextBox";
            this.firstFormTextBox.Size = new System.Drawing.Size(256, 20);
            this.firstFormTextBox.TabIndex = 1;
            // 
            // firstFormLabel
            // 
            this.firstFormLabel.AutoSize = true;
            this.firstFormLabel.Font = new System.Drawing.Font("Times New Roman", 12F);
            this.firstFormLabel.Location = new System.Drawing.Point(14, 27);
            this.firstFormLabel.Name = "firstFormLabel";
            this.firstFormLabel.Size = new System.Drawing.Size(21, 19);
            this.firstFormLabel.TabIndex = 2;
            this.firstFormLabel.Text = "I :";
            // 
            // secondFormLabel
            // 
            this.secondFormLabel.AutoSize = true;
            this.secondFormLabel.Font = new System.Drawing.Font("Times New Roman", 12F);
            this.secondFormLabel.Location = new System.Drawing.Point(9, 56);
            this.secondFormLabel.Name = "secondFormLabel";
            this.secondFormLabel.Size = new System.Drawing.Size(26, 19);
            this.secondFormLabel.TabIndex = 3;
            this.secondFormLabel.Text = "II :";
            // 
            // thirdFormLabel
            // 
            this.thirdFormLabel.AutoSize = true;
            this.thirdFormLabel.Font = new System.Drawing.Font("Times New Roman", 12F);
            this.thirdFormLabel.Location = new System.Drawing.Point(5, 86);
            this.thirdFormLabel.Name = "thirdFormLabel";
            this.thirdFormLabel.Size = new System.Drawing.Size(31, 19);
            this.thirdFormLabel.TabIndex = 4;
            this.thirdFormLabel.Text = "III :";
            // 
            // addButton
            // 
            this.addButton.BackColor = System.Drawing.SystemColors.Control;
            this.addButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.addButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.addButton.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.addButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(192)))), ((int)(((byte)(0)))));
            this.addButton.Location = new System.Drawing.Point(321, 23);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(89, 24);
            this.addButton.TabIndex = 7;
            this.addButton.Text = "Добавить";
            this.addButton.UseVisualStyleBackColor = false;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // deleteButton
            // 
            this.deleteButton.BackColor = System.Drawing.SystemColors.Control;
            this.deleteButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.deleteButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.deleteButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            this.deleteButton.Location = new System.Drawing.Point(321, 82);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(89, 24);
            this.deleteButton.TabIndex = 8;
            this.deleteButton.Text = "Удалить";
            this.deleteButton.UseVisualStyleBackColor = false;
            this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // secondFormTextBox
            // 
            this.secondFormTextBox.Location = new System.Drawing.Point(37, 56);
            this.secondFormTextBox.Name = "secondFormTextBox";
            this.secondFormTextBox.Size = new System.Drawing.Size(256, 20);
            this.secondFormTextBox.TabIndex = 9;
            // 
            // thirdFormTextBox
            // 
            this.thirdFormTextBox.Location = new System.Drawing.Point(37, 86);
            this.thirdFormTextBox.Name = "thirdFormTextBox";
            this.thirdFormTextBox.Size = new System.Drawing.Size(256, 20);
            this.thirdFormTextBox.TabIndex = 10;
            // 
            // resultListGridView
            // 
            this.resultListGridView.AllowUserToAddRows = false;
            this.resultListGridView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.resultListGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.resultListGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dataGridViewTextBoxColumn4,
            this.dataGridViewTextBoxColumn5,
            this.dataGridViewTextBoxColumn6});
            this.resultListGridView.GridColor = System.Drawing.SystemColors.Control;
            this.resultListGridView.Location = new System.Drawing.Point(228, 206);
            this.resultListGridView.Name = "resultListGridView";
            this.resultListGridView.RowHeadersWidth = 24;
            this.resultListGridView.RowTemplate.Height = 25;
            this.resultListGridView.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.resultListGridView.Size = new System.Drawing.Size(206, 211);
            this.resultListGridView.TabIndex = 12;
            // 
            // dataGridViewTextBoxColumn4
            // 
            this.dataGridViewTextBoxColumn4.HeaderText = "Первая форма";
            this.dataGridViewTextBoxColumn4.Name = "dataGridViewTextBoxColumn4";
            // 
            // dataGridViewTextBoxColumn5
            // 
            this.dataGridViewTextBoxColumn5.HeaderText = "Вторая форма";
            this.dataGridViewTextBoxColumn5.Name = "dataGridViewTextBoxColumn5";
            // 
            // dataGridViewTextBoxColumn6
            // 
            this.dataGridViewTextBoxColumn6.HeaderText = "Третья форма";
            this.dataGridViewTextBoxColumn6.Name = "dataGridViewTextBoxColumn6";
            // 
            // enterListLabel
            // 
            this.enterListLabel.AutoSize = true;
            this.enterListLabel.Font = new System.Drawing.Font("Times New Roman", 12.75F);
            this.enterListLabel.Location = new System.Drawing.Point(11, 187);
            this.enterListLabel.Name = "enterListLabel";
            this.enterListLabel.Size = new System.Drawing.Size(134, 19);
            this.enterListLabel.TabIndex = 13;
            this.enterListLabel.Text = "Исходный список";
            // 
            // resultListLabel
            // 
            this.resultListLabel.AutoSize = true;
            this.resultListLabel.Font = new System.Drawing.Font("Times New Roman", 12.75F);
            this.resultListLabel.Location = new System.Drawing.Point(228, 187);
            this.resultListLabel.Name = "resultListLabel";
            this.resultListLabel.Size = new System.Drawing.Size(77, 19);
            this.resultListLabel.TabIndex = 14;
            this.resultListLabel.Text = "Результат";
            // 
            // resultButton
            // 
            this.resultButton.BackColor = System.Drawing.SystemColors.Control;
            this.resultButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.resultButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.resultButton.ForeColor = System.Drawing.Color.Teal;
            this.resultButton.Location = new System.Drawing.Point(321, 53);
            this.resultButton.Name = "resultButton";
            this.resultButton.Size = new System.Drawing.Size(89, 24);
            this.resultButton.TabIndex = 15;
            this.resultButton.Text = "Решить";
            this.resultButton.UseVisualStyleBackColor = false;
            this.resultButton.Click += new System.EventHandler(this.resultButton_Click);
            // 
            // enterListGridView
            // 
            this.enterListGridView.AllowUserToAddRows = false;
            this.enterListGridView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill;
            this.enterListGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.enterListGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dataGridViewTextBoxColumn1,
            this.dataGridViewTextBoxColumn2,
            this.dataGridViewTextBoxColumn3});
            this.enterListGridView.Location = new System.Drawing.Point(11, 206);
            this.enterListGridView.Name = "enterListGridView";
            this.enterListGridView.RowHeadersWidth = 24;
            this.enterListGridView.RowTemplate.Height = 25;
            this.enterListGridView.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.enterListGridView.Size = new System.Drawing.Size(206, 211);
            this.enterListGridView.TabIndex = 16;
            // 
            // dataGridViewTextBoxColumn1
            // 
            this.dataGridViewTextBoxColumn1.HeaderText = "Первая форма";
            this.dataGridViewTextBoxColumn1.Name = "dataGridViewTextBoxColumn1";
            // 
            // dataGridViewTextBoxColumn2
            // 
            this.dataGridViewTextBoxColumn2.HeaderText = "Вторая форма";
            this.dataGridViewTextBoxColumn2.Name = "dataGridViewTextBoxColumn2";
            // 
            // dataGridViewTextBoxColumn3
            // 
            this.dataGridViewTextBoxColumn3.HeaderText = "Третья форма";
            this.dataGridViewTextBoxColumn3.Name = "dataGridViewTextBoxColumn3";
            // 
            // mainGroupBox
            // 
            this.mainGroupBox.Controls.Add(this.firstFormTextBox);
            this.mainGroupBox.Controls.Add(this.resultButton);
            this.mainGroupBox.Controls.Add(this.firstFormLabel);
            this.mainGroupBox.Controls.Add(this.secondFormLabel);
            this.mainGroupBox.Controls.Add(this.thirdFormTextBox);
            this.mainGroupBox.Controls.Add(this.addButton);
            this.mainGroupBox.Controls.Add(this.secondFormTextBox);
            this.mainGroupBox.Controls.Add(this.deleteButton);
            this.mainGroupBox.Controls.Add(this.thirdFormLabel);
            this.mainGroupBox.Location = new System.Drawing.Point(11, 30);
            this.mainGroupBox.Name = "mainGroupBox";
            this.mainGroupBox.Size = new System.Drawing.Size(423, 122);
            this.mainGroupBox.TabIndex = 17;
            this.mainGroupBox.TabStop = false;
            this.mainGroupBox.Text = "Действия";
            // 
            // taskLabel
            // 
            this.taskLabel.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.taskLabel.Location = new System.Drawing.Point(10, 155);
            this.taskLabel.Name = "taskLabel";
            this.taskLabel.Size = new System.Drawing.Size(424, 32);
            this.taskLabel.TabIndex = 18;
            this.taskLabel.Text = "В результат в алфавитном порядке выведутся те глаголы исходного списка, все 3 фор" +
    "мы которых равны.";
            this.taskLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // clearEnterListButton
            // 
            this.clearEnterListButton.BackColor = System.Drawing.SystemColors.Control;
            this.clearEnterListButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.clearEnterListButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.clearEnterListButton.ForeColor = System.Drawing.Color.Black;
            this.clearEnterListButton.Location = new System.Drawing.Point(11, 422);
            this.clearEnterListButton.Name = "clearEnterListButton";
            this.clearEnterListButton.Size = new System.Drawing.Size(206, 24);
            this.clearEnterListButton.TabIndex = 19;
            this.clearEnterListButton.Text = "Очистить исходный список";
            this.clearEnterListButton.UseVisualStyleBackColor = false;
            this.clearEnterListButton.Click += new System.EventHandler(this.clearEnterListButton_Click);
            // 
            // clearResultListButton
            // 
            this.clearResultListButton.BackColor = System.Drawing.SystemColors.Control;
            this.clearResultListButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.clearResultListButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.clearResultListButton.ForeColor = System.Drawing.Color.Black;
            this.clearResultListButton.Location = new System.Drawing.Point(228, 422);
            this.clearResultListButton.Name = "clearResultListButton";
            this.clearResultListButton.Size = new System.Drawing.Size(206, 24);
            this.clearResultListButton.TabIndex = 20;
            this.clearResultListButton.Text = "Очистить результат";
            this.clearResultListButton.UseVisualStyleBackColor = false;
            this.clearResultListButton.Click += new System.EventHandler(this.clearResultListButton_Click);
            // 
            // saveMenuStrip
            // 
            this.saveMenuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.serializationToolStripMenuItem,
            this.commonToolStripMenuItem});
            this.saveMenuStrip.Location = new System.Drawing.Point(0, 0);
            this.saveMenuStrip.Name = "saveMenuStrip";
            this.saveMenuStrip.Padding = new System.Windows.Forms.Padding(5, 2, 0, 2);
            this.saveMenuStrip.Size = new System.Drawing.Size(444, 24);
            this.saveMenuStrip.TabIndex = 21;
            this.saveMenuStrip.Text = "menuStrip1";
            // 
            // serializationToolStripMenuItem
            // 
            this.serializationToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.serializationSaveButton,
            this.serializationLoadButton});
            this.serializationToolStripMenuItem.Name = "serializationToolStripMenuItem";
            this.serializationToolStripMenuItem.Size = new System.Drawing.Size(98, 20);
            this.serializationToolStripMenuItem.Text = "Сериализация";
            // 
            // serializationSaveButton
            // 
            this.serializationSaveButton.Name = "serializationSaveButton";
            this.serializationSaveButton.Size = new System.Drawing.Size(180, 22);
            this.serializationSaveButton.Text = "Сохранить";
            this.serializationSaveButton.Click += new System.EventHandler(this.serializationSaveButton_Click);
            // 
            // serializationLoadButton
            // 
            this.serializationLoadButton.Name = "serializationLoadButton";
            this.serializationLoadButton.Size = new System.Drawing.Size(180, 22);
            this.serializationLoadButton.Text = "Загрузить";
            this.serializationLoadButton.Click += new System.EventHandler(this.serializationLoadButton_Click);
            // 
            // commonToolStripMenuItem
            // 
            this.commonToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.commonSaveButton,
            this.commonLoadButton});
            this.commonToolStripMenuItem.Name = "commonToolStripMenuItem";
            this.commonToolStripMenuItem.Size = new System.Drawing.Size(48, 20);
            this.commonToolStripMenuItem.Text = "Файл";
            // 
            // commonSaveButton
            // 
            this.commonSaveButton.Name = "commonSaveButton";
            this.commonSaveButton.Size = new System.Drawing.Size(180, 22);
            this.commonSaveButton.Text = "Сохранить";
            this.commonSaveButton.Click += new System.EventHandler(this.commonSaveButton_Click);
            // 
            // commonLoadButton
            // 
            this.commonLoadButton.Name = "commonLoadButton";
            this.commonLoadButton.Size = new System.Drawing.Size(180, 22);
            this.commonLoadButton.Text = "Загрузить";
            this.commonLoadButton.Click += new System.EventHandler(this.commonLoadButton_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.ClientSize = new System.Drawing.Size(444, 454);
            this.Controls.Add(this.clearResultListButton);
            this.Controls.Add(this.clearEnterListButton);
            this.Controls.Add(this.taskLabel);
            this.Controls.Add(this.enterListGridView);
            this.Controls.Add(this.resultListLabel);
            this.Controls.Add(this.enterListLabel);
            this.Controls.Add(this.resultListGridView);
            this.Controls.Add(this.mainGroupBox);
            this.Controls.Add(this.saveMenuStrip);
            this.ForeColor = System.Drawing.Color.Black;
            this.MainMenuStrip = this.saveMenuStrip;
            this.Name = "MainWindow";
            this.Text = "Таблица английских глаголов";
            ((System.ComponentModel.ISupportInitialize)(this.resultListGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.enterListGridView)).EndInit();
            this.mainGroupBox.ResumeLayout(false);
            this.mainGroupBox.PerformLayout();
            this.saveMenuStrip.ResumeLayout(false);
            this.saveMenuStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.TextBox firstFormTextBox;
        private System.Windows.Forms.Label firstFormLabel;
        private System.Windows.Forms.Label secondFormLabel;
        private System.Windows.Forms.Label thirdFormLabel;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button deleteButton;
        private System.Windows.Forms.TextBox secondFormTextBox;
        private System.Windows.Forms.TextBox thirdFormTextBox;
        private System.Windows.Forms.DataGridView resultListGridView;
        private System.Windows.Forms.Label enterListLabel;
        private System.Windows.Forms.Label resultListLabel;
        private System.Windows.Forms.Button resultButton;
        private System.Windows.Forms.DataGridView enterListGridView;
        private System.Windows.Forms.GroupBox mainGroupBox;
        private System.Windows.Forms.Label taskLabel;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn4;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn5;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn6;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn2;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn3;
        private System.Windows.Forms.Button clearEnterListButton;
        private System.Windows.Forms.Button clearResultListButton;
        private System.Windows.Forms.MenuStrip saveMenuStrip;
        private System.Windows.Forms.ToolStripMenuItem serializationToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem serializationSaveButton;
        private System.Windows.Forms.ToolStripMenuItem serializationLoadButton;
        private System.Windows.Forms.ToolStripMenuItem commonToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem commonSaveButton;
        private System.Windows.Forms.ToolStripMenuItem commonLoadButton;
    }
}

