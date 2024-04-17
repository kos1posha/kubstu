
namespace s2_oop_lw_07
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
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.menuToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.createToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.timerButton = new System.Windows.Forms.ToolStripMenuItem();
            this.stopwatchButton = new System.Windows.Forms.ToolStripMenuItem();
            this.secret = new System.Windows.Forms.ToolStripMenuItem();
            this.what = new System.Windows.Forms.ToolStripMenuItem();
            this.windowsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.locationToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.cascadeButton = new System.Windows.Forms.ToolStripMenuItem();
            this.horisontalButton = new System.Windows.Forms.ToolStripMenuItem();
            this.verticalButton = new System.Windows.Forms.ToolStripMenuItem();
            this.closeAllButton = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip
            // 
            this.menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.menuToolStripMenuItem,
            this.secret,
            this.windowsToolStripMenuItem});
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Size = new System.Drawing.Size(800, 24);
            this.menuStrip.TabIndex = 1;
            this.menuStrip.Text = "menuStrip1";
            // 
            // menuToolStripMenuItem
            // 
            this.menuToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.createToolStripMenuItem});
            this.menuToolStripMenuItem.Name = "menuToolStripMenuItem";
            this.menuToolStripMenuItem.Size = new System.Drawing.Size(53, 20);
            this.menuToolStripMenuItem.Text = "Меню";
            // 
            // createToolStripMenuItem
            // 
            this.createToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.timerButton,
            this.stopwatchButton});
            this.createToolStripMenuItem.Name = "createToolStripMenuItem";
            this.createToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.createToolStripMenuItem.Text = "Создать";
            // 
            // timerButton
            // 
            this.timerButton.Name = "timerButton";
            this.timerButton.Size = new System.Drawing.Size(180, 22);
            this.timerButton.Text = "Таймер";
            this.timerButton.Click += new System.EventHandler(this.timerButton_Click);
            // 
            // stopwatchButton
            // 
            this.stopwatchButton.Name = "stopwatchButton";
            this.stopwatchButton.Size = new System.Drawing.Size(180, 22);
            this.stopwatchButton.Text = "Секундомер";
            this.stopwatchButton.Click += new System.EventHandler(this.секундомерToolStripMenuItem_Click);
            // 
            // secret
            // 
            this.secret.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.what});
            this.secret.Name = "secret";
            this.secret.Size = new System.Drawing.Size(12, 20);
            // 
            // what
            // 
            this.what.Name = "what";
            this.what.Size = new System.Drawing.Size(209, 22);
            this.what.Text = "А что ты здесь делаешь?";
            this.what.Click += new System.EventHandler(this.what_Click);
            // 
            // windowsToolStripMenuItem
            // 
            this.windowsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.locationToolStripMenuItem,
            this.closeAllButton});
            this.windowsToolStripMenuItem.Name = "windowsToolStripMenuItem";
            this.windowsToolStripMenuItem.Size = new System.Drawing.Size(47, 20);
            this.windowsToolStripMenuItem.Text = "Окна";
            // 
            // locationToolStripMenuItem
            // 
            this.locationToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.cascadeButton,
            this.horisontalButton,
            this.verticalButton});
            this.locationToolStripMenuItem.Name = "locationToolStripMenuItem";
            this.locationToolStripMenuItem.Size = new System.Drawing.Size(180, 22);
            this.locationToolStripMenuItem.Text = "Расположение";
            // 
            // cascadeButton
            // 
            this.cascadeButton.Name = "cascadeButton";
            this.cascadeButton.Size = new System.Drawing.Size(180, 22);
            this.cascadeButton.Text = "Каскадом";
            this.cascadeButton.Click += new System.EventHandler(this.cascadeButton_Click);
            // 
            // horisontalButton
            // 
            this.horisontalButton.Name = "horisontalButton";
            this.horisontalButton.Size = new System.Drawing.Size(180, 22);
            this.horisontalButton.Text = "Горизонтально ";
            this.horisontalButton.Click += new System.EventHandler(this.horisontalButton_Click);
            // 
            // verticalButton
            // 
            this.verticalButton.Name = "verticalButton";
            this.verticalButton.Size = new System.Drawing.Size(180, 22);
            this.verticalButton.Text = "Вертикально";
            this.verticalButton.Click += new System.EventHandler(this.verticalButton_Click);
            // 
            // closeAllButton
            // 
            this.closeAllButton.Name = "closeAllButton";
            this.closeAllButton.Size = new System.Drawing.Size(180, 22);
            this.closeAllButton.Text = "Закрыть все";
            this.closeAllButton.Click += new System.EventHandler(this.closeAllButton_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.menuStrip);
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.menuStrip;
            this.Name = "MainWindow";
            this.Text = "Часы";
            this.menuStrip.ResumeLayout(false);
            this.menuStrip.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.ToolStripMenuItem menuToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem createToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem timerButton;
        private System.Windows.Forms.ToolStripMenuItem stopwatchButton;
        private System.Windows.Forms.ToolStripMenuItem secret;
        private System.Windows.Forms.ToolStripMenuItem windowsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem locationToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem cascadeButton;
        private System.Windows.Forms.ToolStripMenuItem horisontalButton;
        private System.Windows.Forms.ToolStripMenuItem verticalButton;
        private System.Windows.Forms.ToolStripMenuItem closeAllButton;
        private System.Windows.Forms.ToolStripMenuItem what;
    }
}

