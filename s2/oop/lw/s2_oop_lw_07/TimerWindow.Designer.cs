
namespace s2_oop_lw_07
{
    partial class TimerWindow
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
            this.components = new System.ComponentModel.Container();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.msSeparator = new System.Windows.Forms.Label();
            this.hoursLabel = new System.Windows.Forms.TextBox();
            this.hmSeparator = new System.Windows.Forms.Label();
            this.startButton = new System.Windows.Forms.Button();
            this.pauseButton = new System.Windows.Forms.Button();
            this.stopButton = new System.Windows.Forms.Button();
            this.minutesLabel = new System.Windows.Forms.TextBox();
            this.secondesLabel = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // timer
            // 
            this.timer.Interval = 1000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // msSeparator
            // 
            this.msSeparator.AutoSize = true;
            this.msSeparator.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.msSeparator.Location = new System.Drawing.Point(100, 39);
            this.msSeparator.Name = "msSeparator";
            this.msSeparator.Size = new System.Drawing.Size(23, 37);
            this.msSeparator.TabIndex = 8;
            this.msSeparator.Text = ":";
            // 
            // hoursLabel
            // 
            this.hoursLabel.BackColor = System.Drawing.SystemColors.Control;
            this.hoursLabel.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.hoursLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hoursLabel.Location = new System.Drawing.Point(10, 39);
            this.hoursLabel.MaxLength = 2;
            this.hoursLabel.Name = "hoursLabel";
            this.hoursLabel.Size = new System.Drawing.Size(29, 36);
            this.hoursLabel.TabIndex = 10;
            this.hoursLabel.Text = "0";
            this.hoursLabel.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.hoursLabel.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.hoursLabel_KeyPress);
            // 
            // hmSeparator
            // 
            this.hmSeparator.AutoSize = true;
            this.hmSeparator.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hmSeparator.Location = new System.Drawing.Point(43, 39);
            this.hmSeparator.Name = "hmSeparator";
            this.hmSeparator.Size = new System.Drawing.Size(23, 37);
            this.hmSeparator.TabIndex = 13;
            this.hmSeparator.Text = ":";
            // 
            // startButton
            // 
            this.startButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.startIcon;
            this.startButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.startButton.Location = new System.Drawing.Point(10, 91);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(30, 30);
            this.startButton.TabIndex = 17;
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // pauseButton
            // 
            this.pauseButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.pauseIcon;
            this.pauseButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pauseButton.FlatAppearance.BorderColor = System.Drawing.SystemColors.Control;
            this.pauseButton.FlatAppearance.BorderSize = 3;
            this.pauseButton.Location = new System.Drawing.Point(67, 91);
            this.pauseButton.Name = "pauseButton";
            this.pauseButton.Size = new System.Drawing.Size(30, 30);
            this.pauseButton.TabIndex = 18;
            this.pauseButton.UseVisualStyleBackColor = true;
            this.pauseButton.Click += new System.EventHandler(this.pauseButton_Click);
            // 
            // stopButton
            // 
            this.stopButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.stopIcon;
            this.stopButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.stopButton.FlatAppearance.BorderColor = System.Drawing.SystemColors.Control;
            this.stopButton.FlatAppearance.BorderSize = 3;
            this.stopButton.Location = new System.Drawing.Point(124, 91);
            this.stopButton.Name = "stopButton";
            this.stopButton.Size = new System.Drawing.Size(30, 30);
            this.stopButton.TabIndex = 19;
            this.stopButton.UseVisualStyleBackColor = true;
            this.stopButton.Click += new System.EventHandler(this.stopButton_Click);
            // 
            // minutesLabel
            // 
            this.minutesLabel.BackColor = System.Drawing.SystemColors.Control;
            this.minutesLabel.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.minutesLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.minutesLabel.Location = new System.Drawing.Point(67, 39);
            this.minutesLabel.MaxLength = 2;
            this.minutesLabel.Name = "minutesLabel";
            this.minutesLabel.Size = new System.Drawing.Size(29, 36);
            this.minutesLabel.TabIndex = 20;
            this.minutesLabel.Text = "0";
            this.minutesLabel.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.minutesLabel.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.minutesLabel_KeyPress);
            // 
            // secondesLabel
            // 
            this.secondesLabel.BackColor = System.Drawing.SystemColors.Control;
            this.secondesLabel.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.secondesLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.secondesLabel.Location = new System.Drawing.Point(123, 39);
            this.secondesLabel.MaxLength = 2;
            this.secondesLabel.Name = "secondesLabel";
            this.secondesLabel.Size = new System.Drawing.Size(29, 36);
            this.secondesLabel.TabIndex = 21;
            this.secondesLabel.Text = "0";
            this.secondesLabel.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            this.secondesLabel.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.secondesLabel_KeyPress);
            // 
            // TimerWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(163, 145);
            this.Controls.Add(this.secondesLabel);
            this.Controls.Add(this.minutesLabel);
            this.Controls.Add(this.stopButton);
            this.Controls.Add(this.pauseButton);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.hmSeparator);
            this.Controls.Add(this.hoursLabel);
            this.Controls.Add(this.msSeparator);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "TimerWindow";
            this.Text = "Таймер";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.Label msSeparator;
        private System.Windows.Forms.TextBox hoursLabel;
        private System.Windows.Forms.Label hmSeparator;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button pauseButton;
        private System.Windows.Forms.Button stopButton;
        private System.Windows.Forms.TextBox minutesLabel;
        private System.Windows.Forms.TextBox secondesLabel;
    }
}