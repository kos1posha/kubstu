
namespace s2_oop_lw_07
{
    partial class Stopwatch
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
            this.hoursLabel = new System.Windows.Forms.Label();
            this.secondesLabel = new System.Windows.Forms.Label();
            this.minutesLabel = new System.Windows.Forms.Label();
            this.hmSeparator = new System.Windows.Forms.Label();
            this.msSeparator = new System.Windows.Forms.Label();
            this.startButton = new System.Windows.Forms.Button();
            this.stopButton = new System.Windows.Forms.Button();
            this.pauseButton = new System.Windows.Forms.Button();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.SuspendLayout();
            // 
            // hoursLabel
            // 
            this.hoursLabel.AutoSize = true;
            this.hoursLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hoursLabel.Location = new System.Drawing.Point(10, 37);
            this.hoursLabel.Name = "hoursLabel";
            this.hoursLabel.Size = new System.Drawing.Size(32, 37);
            this.hoursLabel.TabIndex = 0;
            this.hoursLabel.Text = "0";
            // 
            // secondesLabel
            // 
            this.secondesLabel.AutoSize = true;
            this.secondesLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.secondesLabel.Location = new System.Drawing.Point(123, 37);
            this.secondesLabel.Name = "secondesLabel";
            this.secondesLabel.Size = new System.Drawing.Size(32, 37);
            this.secondesLabel.TabIndex = 1;
            this.secondesLabel.Text = "0";
            // 
            // minutesLabel
            // 
            this.minutesLabel.AutoSize = true;
            this.minutesLabel.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.minutesLabel.Location = new System.Drawing.Point(67, 37);
            this.minutesLabel.Name = "minutesLabel";
            this.minutesLabel.Size = new System.Drawing.Size(32, 37);
            this.minutesLabel.TabIndex = 2;
            this.minutesLabel.Text = "0";
            // 
            // hmSeparator
            // 
            this.hmSeparator.AutoSize = true;
            this.hmSeparator.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hmSeparator.Location = new System.Drawing.Point(43, 39);
            this.hmSeparator.Name = "hmSeparator";
            this.hmSeparator.Size = new System.Drawing.Size(23, 37);
            this.hmSeparator.TabIndex = 3;
            this.hmSeparator.Text = ":";
            // 
            // msSeparator
            // 
            this.msSeparator.AutoSize = true;
            this.msSeparator.Font = new System.Drawing.Font("Segoe UI", 20.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.msSeparator.Location = new System.Drawing.Point(100, 39);
            this.msSeparator.Name = "msSeparator";
            this.msSeparator.Size = new System.Drawing.Size(23, 37);
            this.msSeparator.TabIndex = 4;
            this.msSeparator.Text = ":";
            // 
            // startButton
            // 
            this.startButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.startIcon;
            this.startButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.startButton.Location = new System.Drawing.Point(10, 91);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(30, 30);
            this.startButton.TabIndex = 5;
            this.startButton.UseVisualStyleBackColor = true;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // stopButton
            // 
            this.stopButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.stopIcon;
            this.stopButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.stopButton.Location = new System.Drawing.Point(124, 91);
            this.stopButton.Name = "stopButton";
            this.stopButton.Size = new System.Drawing.Size(30, 30);
            this.stopButton.TabIndex = 6;
            this.stopButton.UseVisualStyleBackColor = true;
            this.stopButton.Click += new System.EventHandler(this.stopButton_Click);
            // 
            // pauseButton
            // 
            this.pauseButton.BackgroundImage = global::s2_oop_lw_07.Properties.Resources.pauseIcon;
            this.pauseButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pauseButton.Location = new System.Drawing.Point(67, 91);
            this.pauseButton.Name = "pauseButton";
            this.pauseButton.Size = new System.Drawing.Size(30, 30);
            this.pauseButton.TabIndex = 7;
            this.pauseButton.UseVisualStyleBackColor = true;
            this.pauseButton.Click += new System.EventHandler(this.pauseButton_Click);
            // 
            // timer
            // 
            this.timer.Interval = 1000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // Stopwatch
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(163, 144);
            this.Controls.Add(this.pauseButton);
            this.Controls.Add(this.stopButton);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.msSeparator);
            this.Controls.Add(this.hmSeparator);
            this.Controls.Add(this.minutesLabel);
            this.Controls.Add(this.secondesLabel);
            this.Controls.Add(this.hoursLabel);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.Name = "Stopwatch";
            this.Text = "Секундомер";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label hoursLabel;
        private System.Windows.Forms.Label secondesLabel;
        private System.Windows.Forms.Label minutesLabel;
        private System.Windows.Forms.Label hmSeparator;
        private System.Windows.Forms.Label msSeparator;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button stopButton;
        private System.Windows.Forms.Button pauseButton;
        private System.Windows.Forms.Timer timer;
    }
}