
namespace s2_oop_lw_05
{
    partial class Registration
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
            this.regExitButton = new System.Windows.Forms.Button();
            this.regStartButton = new System.Windows.Forms.Button();
            this.labelHeroName = new System.Windows.Forms.Label();
            this.labelHeroClass = new System.Windows.Forms.Label();
            this.heroName = new System.Windows.Forms.TextBox();
            this.heroClass = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // regExitButton
            // 
            this.regExitButton.BackColor = System.Drawing.Color.Gold;
            this.regExitButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.regExitButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.regExitButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.regExitButton.Font = new System.Drawing.Font("NSimSun", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.regExitButton.Location = new System.Drawing.Point(81, 130);
            this.regExitButton.Name = "regExitButton";
            this.regExitButton.Size = new System.Drawing.Size(94, 23);
            this.regExitButton.TabIndex = 0;
            this.regExitButton.Text = "Выход";
            this.regExitButton.UseVisualStyleBackColor = false;
            this.regExitButton.Click += new System.EventHandler(this.regExitButton_Click);
            // 
            // regStartButton
            // 
            this.regStartButton.BackColor = System.Drawing.Color.Gold;
            this.regStartButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.regStartButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(64)))), ((int)(((byte)(0)))));
            this.regStartButton.FlatAppearance.BorderSize = 2;
            this.regStartButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.regStartButton.Font = new System.Drawing.Font("NSimSun", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.regStartButton.Location = new System.Drawing.Point(81, 100);
            this.regStartButton.Name = "regStartButton";
            this.regStartButton.Size = new System.Drawing.Size(94, 23);
            this.regStartButton.TabIndex = 1;
            this.regStartButton.Text = "Начать";
            this.regStartButton.UseVisualStyleBackColor = false;
            this.regStartButton.Click += new System.EventHandler(this.regStartButton_Click);
            // 
            // labelHeroName
            // 
            this.labelHeroName.AutoSize = true;
            this.labelHeroName.BackColor = System.Drawing.Color.Transparent;
            this.labelHeroName.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.labelHeroName.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.labelHeroName.Location = new System.Drawing.Point(110, 8);
            this.labelHeroName.Name = "labelHeroName";
            this.labelHeroName.Size = new System.Drawing.Size(39, 20);
            this.labelHeroName.TabIndex = 2;
            this.labelHeroName.Text = "Имя";
            // 
            // labelHeroClass
            // 
            this.labelHeroClass.AutoSize = true;
            this.labelHeroClass.BackColor = System.Drawing.Color.Transparent;
            this.labelHeroClass.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.labelHeroClass.ForeColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.labelHeroClass.Location = new System.Drawing.Point(108, 49);
            this.labelHeroClass.Name = "labelHeroClass";
            this.labelHeroClass.Size = new System.Drawing.Size(48, 20);
            this.labelHeroClass.TabIndex = 3;
            this.labelHeroClass.Text = "Класс";
            // 
            // heroName
            // 
            this.heroName.Location = new System.Drawing.Point(43, 26);
            this.heroName.MaxLength = 20;
            this.heroName.Name = "heroName";
            this.heroName.Size = new System.Drawing.Size(172, 20);
            this.heroName.TabIndex = 4;
            // 
            // heroClass
            // 
            this.heroClass.BackColor = System.Drawing.SystemColors.Window;
            this.heroClass.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.heroClass.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.heroClass.FormattingEnabled = true;
            this.heroClass.Items.AddRange(new object[] {
            "Мечник",
            "Лучник",
            "Разбойник"});
            this.heroClass.Location = new System.Drawing.Point(43, 69);
            this.heroClass.Name = "heroClass";
            this.heroClass.Size = new System.Drawing.Size(172, 21);
            this.heroClass.TabIndex = 5;
            // 
            // Registration
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::s2_oop_lw_05.Properties.Resources.regbackground;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(257, 165);
            this.Controls.Add(this.heroClass);
            this.Controls.Add(this.heroName);
            this.Controls.Add(this.labelHeroClass);
            this.Controls.Add(this.labelHeroName);
            this.Controls.Add(this.regStartButton);
            this.Controls.Add(this.regExitButton);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Name = "Registration";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Registration";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button regExitButton;
        private System.Windows.Forms.Button regStartButton;
        private System.Windows.Forms.Label labelHeroName;
        private System.Windows.Forms.Label labelHeroClass;
        private System.Windows.Forms.TextBox heroName;
        private System.Windows.Forms.ComboBox heroClass;
    }
}

