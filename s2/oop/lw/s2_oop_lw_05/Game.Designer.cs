
namespace s2_oop_lw_05
{
    partial class Game
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
            this.settingsButton = new System.Windows.Forms.Button();
            this.heroInfoBox = new System.Windows.Forms.GroupBox();
            this.heroEquipment = new System.Windows.Forms.ListBox();
            this.quickHealButton = new System.Windows.Forms.Button();
            this.labelHeroHealth = new System.Windows.Forms.Label();
            this.labelHeroClass = new System.Windows.Forms.Label();
            this.labelHeroGold = new System.Windows.Forms.Label();
            this.labelHeroItems = new System.Windows.Forms.Label();
            this.heroHealth = new System.Windows.Forms.Label();
            this.heroWeight = new System.Windows.Forms.Label();
            this.heroGold = new System.Windows.Forms.Label();
            this.heroClass = new System.Windows.Forms.Label();
            this.heroView = new System.Windows.Forms.PictureBox();
            this.heroItems = new System.Windows.Forms.ListBox();
            this.throwButton = new System.Windows.Forms.Button();
            this.useButton = new System.Windows.Forms.Button();
            this.quickAidButton = new System.Windows.Forms.Button();
            this.history = new System.Windows.Forms.RichTextBox();
            this.eventBox = new System.Windows.Forms.GroupBox();
            this.labelEventCreatureName = new System.Windows.Forms.Label();
            this.labelEventCreatureClass = new System.Windows.Forms.Label();
            this.labelEventCreatureLevel = new System.Windows.Forms.Label();
            this.eventCreatureName = new System.Windows.Forms.Label();
            this.eventCreatureLevel = new System.Windows.Forms.Label();
            this.eventCreatureClass = new System.Windows.Forms.Label();
            this.eventText = new System.Windows.Forms.Label();
            this.eventComboBox = new System.Windows.Forms.ComboBox();
            this.goButton = new System.Windows.Forms.Button();
            this.quickDamageButton = new System.Windows.Forms.Button();
            this.attackButton = new System.Windows.Forms.Button();
            this.heroInfoBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.heroView)).BeginInit();
            this.eventBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // settingsButton
            // 
            this.settingsButton.BackColor = System.Drawing.Color.Silver;
            this.settingsButton.BackgroundImage = global::s2_oop_lw_05.Properties.Resources.settings;
            this.settingsButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.settingsButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.settingsButton.FlatAppearance.BorderSize = 2;
            this.settingsButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.settingsButton.Location = new System.Drawing.Point(747, 432);
            this.settingsButton.Margin = new System.Windows.Forms.Padding(4);
            this.settingsButton.Name = "settingsButton";
            this.settingsButton.Size = new System.Drawing.Size(40, 40);
            this.settingsButton.TabIndex = 0;
            this.settingsButton.UseVisualStyleBackColor = false;
            this.settingsButton.Click += new System.EventHandler(this.settingsButton_Click);
            // 
            // heroInfoBox
            // 
            this.heroInfoBox.BackColor = System.Drawing.Color.Transparent;
            this.heroInfoBox.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.heroInfoBox.Controls.Add(this.heroEquipment);
            this.heroInfoBox.Controls.Add(this.quickHealButton);
            this.heroInfoBox.Controls.Add(this.labelHeroHealth);
            this.heroInfoBox.Controls.Add(this.labelHeroClass);
            this.heroInfoBox.Controls.Add(this.labelHeroGold);
            this.heroInfoBox.Controls.Add(this.labelHeroItems);
            this.heroInfoBox.Controls.Add(this.heroHealth);
            this.heroInfoBox.Controls.Add(this.heroWeight);
            this.heroInfoBox.Controls.Add(this.heroGold);
            this.heroInfoBox.Controls.Add(this.heroClass);
            this.heroInfoBox.Controls.Add(this.heroView);
            this.heroInfoBox.Controls.Add(this.heroItems);
            this.heroInfoBox.Controls.Add(this.throwButton);
            this.heroInfoBox.Controls.Add(this.useButton);
            this.heroInfoBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.heroInfoBox.Font = new System.Drawing.Font("Segoe UI", 13F);
            this.heroInfoBox.ForeColor = System.Drawing.Color.White;
            this.heroInfoBox.Location = new System.Drawing.Point(15, 16);
            this.heroInfoBox.Margin = new System.Windows.Forms.Padding(4);
            this.heroInfoBox.Name = "heroInfoBox";
            this.heroInfoBox.Padding = new System.Windows.Forms.Padding(4);
            this.heroInfoBox.Size = new System.Drawing.Size(260, 365);
            this.heroInfoBox.TabIndex = 1;
            this.heroInfoBox.TabStop = false;
            this.heroInfoBox.Text = "name";
            // 
            // heroEquipment
            // 
            this.heroEquipment.BackColor = System.Drawing.Color.Silver;
            this.heroEquipment.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.heroEquipment.DisplayMember = "DisplayMemberName";
            this.heroEquipment.Font = new System.Drawing.Font("Segoe UI", 7.1F);
            this.heroEquipment.FormattingEnabled = true;
            this.heroEquipment.ItemHeight = 12;
            this.heroEquipment.Location = new System.Drawing.Point(6, 133);
            this.heroEquipment.Margin = new System.Windows.Forms.Padding(4);
            this.heroEquipment.Name = "heroEquipment";
            this.heroEquipment.Size = new System.Drawing.Size(246, 36);
            this.heroEquipment.TabIndex = 22;
            this.heroEquipment.SelectedIndexChanged += new System.EventHandler(this.heroEquipment_SelectedIndexChanged);
            // 
            // quickHealButton
            // 
            this.quickHealButton.BackColor = System.Drawing.Color.Silver;
            this.quickHealButton.BackgroundImage = global::s2_oop_lw_05.Properties.Resources.quickaidbutton;
            this.quickHealButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.quickHealButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.quickHealButton.FlatAppearance.BorderSize = 2;
            this.quickHealButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.quickHealButton.Font = new System.Drawing.Font("Segoe UI", 20F);
            this.quickHealButton.ForeColor = System.Drawing.Color.Red;
            this.quickHealButton.Location = new System.Drawing.Point(224, 327);
            this.quickHealButton.Margin = new System.Windows.Forms.Padding(4);
            this.quickHealButton.Name = "quickHealButton";
            this.quickHealButton.Size = new System.Drawing.Size(30, 30);
            this.quickHealButton.TabIndex = 21;
            this.quickHealButton.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.quickHealButton.UseVisualStyleBackColor = false;
            this.quickHealButton.Click += new System.EventHandler(this.quickHealButton_Click);
            // 
            // labelHeroHealth
            // 
            this.labelHeroHealth.AutoSize = true;
            this.labelHeroHealth.BackColor = System.Drawing.Color.Transparent;
            this.labelHeroHealth.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelHeroHealth.Location = new System.Drawing.Point(6, 35);
            this.labelHeroHealth.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelHeroHealth.Name = "labelHeroHealth";
            this.labelHeroHealth.Size = new System.Drawing.Size(65, 15);
            this.labelHeroHealth.TabIndex = 2;
            this.labelHeroHealth.Text = "Здоровье :";
            // 
            // labelHeroClass
            // 
            this.labelHeroClass.AutoSize = true;
            this.labelHeroClass.BackColor = System.Drawing.Color.Transparent;
            this.labelHeroClass.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelHeroClass.Location = new System.Drawing.Point(6, 55);
            this.labelHeroClass.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelHeroClass.Name = "labelHeroClass";
            this.labelHeroClass.Size = new System.Drawing.Size(45, 15);
            this.labelHeroClass.TabIndex = 4;
            this.labelHeroClass.Text = "Класс :";
            // 
            // labelHeroGold
            // 
            this.labelHeroGold.AutoSize = true;
            this.labelHeroGold.BackColor = System.Drawing.Color.Transparent;
            this.labelHeroGold.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelHeroGold.Location = new System.Drawing.Point(6, 75);
            this.labelHeroGold.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelHeroGold.Name = "labelHeroGold";
            this.labelHeroGold.Size = new System.Drawing.Size(53, 15);
            this.labelHeroGold.TabIndex = 3;
            this.labelHeroGold.Text = "Золото :";
            // 
            // labelHeroItems
            // 
            this.labelHeroItems.AutoSize = true;
            this.labelHeroItems.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelHeroItems.Location = new System.Drawing.Point(6, 112);
            this.labelHeroItems.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelHeroItems.Name = "labelHeroItems";
            this.labelHeroItems.Size = new System.Drawing.Size(69, 15);
            this.labelHeroItems.TabIndex = 9;
            this.labelHeroItems.Text = "Инвентарь:";
            // 
            // heroHealth
            // 
            this.heroHealth.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.heroHealth.BackColor = System.Drawing.Color.Transparent;
            this.heroHealth.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.heroHealth.Location = new System.Drawing.Point(70, 32);
            this.heroHealth.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.heroHealth.Name = "heroHealth";
            this.heroHealth.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.heroHealth.Size = new System.Drawing.Size(86, 20);
            this.heroHealth.TabIndex = 5;
            this.heroHealth.Text = "health";
            this.heroHealth.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // heroWeight
            // 
            this.heroWeight.BackColor = System.Drawing.Color.Transparent;
            this.heroWeight.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.heroWeight.Location = new System.Drawing.Point(70, 109);
            this.heroWeight.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.heroWeight.Name = "heroWeight";
            this.heroWeight.Size = new System.Drawing.Size(86, 20);
            this.heroWeight.TabIndex = 7;
            this.heroWeight.Text = "weight";
            this.heroWeight.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // heroGold
            // 
            this.heroGold.AutoEllipsis = true;
            this.heroGold.BackColor = System.Drawing.Color.Transparent;
            this.heroGold.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.heroGold.Location = new System.Drawing.Point(70, 72);
            this.heroGold.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.heroGold.Name = "heroGold";
            this.heroGold.Size = new System.Drawing.Size(86, 20);
            this.heroGold.TabIndex = 20;
            this.heroGold.Text = "gold";
            this.heroGold.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // heroClass
            // 
            this.heroClass.BackColor = System.Drawing.Color.Transparent;
            this.heroClass.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.heroClass.Location = new System.Drawing.Point(70, 52);
            this.heroClass.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.heroClass.Name = "heroClass";
            this.heroClass.Size = new System.Drawing.Size(86, 20);
            this.heroClass.TabIndex = 6;
            this.heroClass.Text = "class";
            this.heroClass.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // heroView
            // 
            this.heroView.BackColor = System.Drawing.Color.Transparent;
            this.heroView.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.heroView.Location = new System.Drawing.Point(158, 17);
            this.heroView.Margin = new System.Windows.Forms.Padding(4);
            this.heroView.Name = "heroView";
            this.heroView.Size = new System.Drawing.Size(102, 109);
            this.heroView.TabIndex = 12;
            this.heroView.TabStop = false;
            // 
            // heroItems
            // 
            this.heroItems.BackColor = System.Drawing.Color.Silver;
            this.heroItems.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.heroItems.DisplayMember = "DisplayMemberName";
            this.heroItems.Font = new System.Drawing.Font("Segoe UI", 7.1F);
            this.heroItems.FormattingEnabled = true;
            this.heroItems.ItemHeight = 12;
            this.heroItems.Location = new System.Drawing.Point(6, 177);
            this.heroItems.Margin = new System.Windows.Forms.Padding(4);
            this.heroItems.Name = "heroItems";
            this.heroItems.Size = new System.Drawing.Size(246, 144);
            this.heroItems.TabIndex = 11;
            this.heroItems.SelectedIndexChanged += new System.EventHandler(this.heroItems_SelectedIndexChanged);
            // 
            // throwButton
            // 
            this.throwButton.BackColor = System.Drawing.Color.Silver;
            this.throwButton.Enabled = false;
            this.throwButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.throwButton.FlatAppearance.BorderSize = 2;
            this.throwButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.throwButton.Font = new System.Drawing.Font("Segoe UI", 8F);
            this.throwButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.throwButton.Location = new System.Drawing.Point(116, 327);
            this.throwButton.Margin = new System.Windows.Forms.Padding(4);
            this.throwButton.Name = "throwButton";
            this.throwButton.Size = new System.Drawing.Size(100, 30);
            this.throwButton.TabIndex = 10;
            this.throwButton.Text = "Выбросить";
            this.throwButton.UseVisualStyleBackColor = false;
            this.throwButton.Click += new System.EventHandler(this.throwButton_Click);
            // 
            // useButton
            // 
            this.useButton.BackColor = System.Drawing.Color.Silver;
            this.useButton.Enabled = false;
            this.useButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.useButton.FlatAppearance.BorderSize = 2;
            this.useButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.useButton.Font = new System.Drawing.Font("Segoe UI", 8F);
            this.useButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.useButton.Location = new System.Drawing.Point(8, 327);
            this.useButton.Margin = new System.Windows.Forms.Padding(4);
            this.useButton.Name = "useButton";
            this.useButton.Size = new System.Drawing.Size(100, 30);
            this.useButton.TabIndex = 1;
            this.useButton.Text = "Использовать";
            this.useButton.UseVisualStyleBackColor = false;
            this.useButton.Click += new System.EventHandler(this.useButton_Click);
            // 
            // quickAidButton
            // 
            this.quickAidButton.BackColor = System.Drawing.Color.Green;
            this.quickAidButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.quickAidButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.quickAidButton.FlatAppearance.BorderSize = 2;
            this.quickAidButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.quickAidButton.Font = new System.Drawing.Font("Segoe UI", 20F);
            this.quickAidButton.ForeColor = System.Drawing.Color.Red;
            this.quickAidButton.Location = new System.Drawing.Point(320, 432);
            this.quickAidButton.Margin = new System.Windows.Forms.Padding(4);
            this.quickAidButton.Name = "quickAidButton";
            this.quickAidButton.Size = new System.Drawing.Size(30, 30);
            this.quickAidButton.TabIndex = 19;
            this.quickAidButton.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.quickAidButton.UseVisualStyleBackColor = false;
            this.quickAidButton.Click += new System.EventHandler(this.quickAidButton_Click);
            // 
            // history
            // 
            this.history.BackColor = System.Drawing.Color.Silver;
            this.history.Cursor = System.Windows.Forms.Cursors.Default;
            this.history.EnableAutoDragDrop = true;
            this.history.Font = new System.Drawing.Font("Segoe UI", 8F);
            this.history.Location = new System.Drawing.Point(15, 388);
            this.history.Name = "history";
            this.history.ReadOnly = true;
            this.history.ScrollBars = System.Windows.Forms.RichTextBoxScrollBars.Vertical;
            this.history.Size = new System.Drawing.Size(260, 133);
            this.history.TabIndex = 13;
            this.history.Text = "";
            // 
            // eventBox
            // 
            this.eventBox.BackColor = System.Drawing.Color.Transparent;
            this.eventBox.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.eventBox.Controls.Add(this.labelEventCreatureName);
            this.eventBox.Controls.Add(this.labelEventCreatureClass);
            this.eventBox.Controls.Add(this.labelEventCreatureLevel);
            this.eventBox.Controls.Add(this.eventCreatureName);
            this.eventBox.Controls.Add(this.eventCreatureLevel);
            this.eventBox.Controls.Add(this.eventCreatureClass);
            this.eventBox.Controls.Add(this.eventText);
            this.eventBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.eventBox.Font = new System.Drawing.Font("Segoe UI", 13F);
            this.eventBox.ForeColor = System.Drawing.Color.White;
            this.eventBox.Location = new System.Drawing.Point(282, 16);
            this.eventBox.Name = "eventBox";
            this.eventBox.Size = new System.Drawing.Size(506, 365);
            this.eventBox.TabIndex = 15;
            this.eventBox.TabStop = false;
            this.eventBox.Text = "Начало приключения";
            // 
            // labelEventCreatureName
            // 
            this.labelEventCreatureName.AutoSize = true;
            this.labelEventCreatureName.BackColor = System.Drawing.Color.Transparent;
            this.labelEventCreatureName.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelEventCreatureName.Location = new System.Drawing.Point(7, 35);
            this.labelEventCreatureName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelEventCreatureName.Name = "labelEventCreatureName";
            this.labelEventCreatureName.Size = new System.Drawing.Size(37, 15);
            this.labelEventCreatureName.TabIndex = 21;
            this.labelEventCreatureName.Text = "Имя :";
            // 
            // labelEventCreatureClass
            // 
            this.labelEventCreatureClass.AutoSize = true;
            this.labelEventCreatureClass.BackColor = System.Drawing.Color.Transparent;
            this.labelEventCreatureClass.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelEventCreatureClass.Location = new System.Drawing.Point(7, 55);
            this.labelEventCreatureClass.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelEventCreatureClass.Name = "labelEventCreatureClass";
            this.labelEventCreatureClass.Size = new System.Drawing.Size(45, 15);
            this.labelEventCreatureClass.TabIndex = 23;
            this.labelEventCreatureClass.Text = "Класс :";
            // 
            // labelEventCreatureLevel
            // 
            this.labelEventCreatureLevel.AutoSize = true;
            this.labelEventCreatureLevel.BackColor = System.Drawing.Color.Transparent;
            this.labelEventCreatureLevel.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.labelEventCreatureLevel.Location = new System.Drawing.Point(7, 75);
            this.labelEventCreatureLevel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.labelEventCreatureLevel.Name = "labelEventCreatureLevel";
            this.labelEventCreatureLevel.Size = new System.Drawing.Size(59, 15);
            this.labelEventCreatureLevel.TabIndex = 22;
            this.labelEventCreatureLevel.Text = "Уровень :";
            // 
            // eventCreatureName
            // 
            this.eventCreatureName.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.eventCreatureName.BackColor = System.Drawing.Color.Transparent;
            this.eventCreatureName.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.eventCreatureName.Location = new System.Drawing.Point(71, 32);
            this.eventCreatureName.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.eventCreatureName.Name = "eventCreatureName";
            this.eventCreatureName.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.eventCreatureName.Size = new System.Drawing.Size(86, 20);
            this.eventCreatureName.TabIndex = 24;
            this.eventCreatureName.Text = "name";
            this.eventCreatureName.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // eventCreatureLevel
            // 
            this.eventCreatureLevel.AutoEllipsis = true;
            this.eventCreatureLevel.BackColor = System.Drawing.Color.Transparent;
            this.eventCreatureLevel.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.eventCreatureLevel.Location = new System.Drawing.Point(71, 72);
            this.eventCreatureLevel.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.eventCreatureLevel.Name = "eventCreatureLevel";
            this.eventCreatureLevel.Size = new System.Drawing.Size(86, 20);
            this.eventCreatureLevel.TabIndex = 26;
            this.eventCreatureLevel.Text = "gold";
            this.eventCreatureLevel.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // eventCreatureClass
            // 
            this.eventCreatureClass.BackColor = System.Drawing.Color.Transparent;
            this.eventCreatureClass.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.eventCreatureClass.Location = new System.Drawing.Point(71, 52);
            this.eventCreatureClass.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.eventCreatureClass.Name = "eventCreatureClass";
            this.eventCreatureClass.Size = new System.Drawing.Size(86, 20);
            this.eventCreatureClass.TabIndex = 25;
            this.eventCreatureClass.Text = "class";
            this.eventCreatureClass.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            // 
            // eventText
            // 
            this.eventText.Font = new System.Drawing.Font("Segoe UI", 10F);
            this.eventText.ForeColor = System.Drawing.Color.White;
            this.eventText.Location = new System.Drawing.Point(6, 177);
            this.eventText.Name = "eventText";
            this.eventText.Size = new System.Drawing.Size(494, 180);
            this.eventText.TabIndex = 14;
            this.eventText.Text = "Вы покинули родные земли по некоторым причинам. \r\nВаше приключение началось.";
            // 
            // eventComboBox
            // 
            this.eventComboBox.DisplayMember = "Name";
            this.eventComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.eventComboBox.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.eventComboBox.FormattingEnabled = true;
            this.eventComboBox.Location = new System.Drawing.Point(282, 387);
            this.eventComboBox.Name = "eventComboBox";
            this.eventComboBox.Size = new System.Drawing.Size(506, 28);
            this.eventComboBox.TabIndex = 17;
            this.eventComboBox.ValueMember = "Name";
            this.eventComboBox.SelectedIndexChanged += new System.EventHandler(this.eventComboBox_SelectedIndexChanged);
            // 
            // goButton
            // 
            this.goButton.BackColor = System.Drawing.Color.Silver;
            this.goButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.goButton.FlatAppearance.BorderSize = 2;
            this.goButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.goButton.Font = new System.Drawing.Font("Segoe UI", 8F);
            this.goButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.goButton.Location = new System.Drawing.Point(643, 432);
            this.goButton.Margin = new System.Windows.Forms.Padding(4);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(96, 40);
            this.goButton.TabIndex = 18;
            this.goButton.Text = "В город";
            this.goButton.UseVisualStyleBackColor = false;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // quickDamageButton
            // 
            this.quickDamageButton.BackColor = System.Drawing.Color.Red;
            this.quickDamageButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.quickDamageButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.quickDamageButton.FlatAppearance.BorderSize = 2;
            this.quickDamageButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.quickDamageButton.Font = new System.Drawing.Font("Segoe UI", 20F);
            this.quickDamageButton.ForeColor = System.Drawing.Color.Red;
            this.quickDamageButton.Location = new System.Drawing.Point(282, 432);
            this.quickDamageButton.Margin = new System.Windows.Forms.Padding(4);
            this.quickDamageButton.Name = "quickDamageButton";
            this.quickDamageButton.Size = new System.Drawing.Size(30, 30);
            this.quickDamageButton.TabIndex = 20;
            this.quickDamageButton.TextAlign = System.Drawing.ContentAlignment.TopCenter;
            this.quickDamageButton.UseVisualStyleBackColor = false;
            this.quickDamageButton.Click += new System.EventHandler(this.quickDamageButton_Click);
            // 
            // attackButton
            // 
            this.attackButton.BackColor = System.Drawing.Color.Silver;
            this.attackButton.Enabled = false;
            this.attackButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.attackButton.FlatAppearance.BorderSize = 2;
            this.attackButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.attackButton.Font = new System.Drawing.Font("Segoe UI", 8F);
            this.attackButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.attackButton.Location = new System.Drawing.Point(535, 432);
            this.attackButton.Margin = new System.Windows.Forms.Padding(4);
            this.attackButton.Name = "attackButton";
            this.attackButton.Size = new System.Drawing.Size(100, 40);
            this.attackButton.TabIndex = 21;
            this.attackButton.Text = "Напасть";
            this.attackButton.UseVisualStyleBackColor = false;
            this.attackButton.Click += new System.EventHandler(this.attackButton_Click);
            // 
            // Game
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.BackgroundImage = global::s2_oop_lw_05.Properties.Resources.gamebackground;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(800, 533);
            this.Controls.Add(this.attackButton);
            this.Controls.Add(this.quickDamageButton);
            this.Controls.Add(this.goButton);
            this.Controls.Add(this.eventComboBox);
            this.Controls.Add(this.eventBox);
            this.Controls.Add(this.history);
            this.Controls.Add(this.heroInfoBox);
            this.Controls.Add(this.settingsButton);
            this.Controls.Add(this.quickAidButton);
            this.Font = new System.Drawing.Font("Segoe UI", 11F);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Game";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Game";
            this.heroInfoBox.ResumeLayout(false);
            this.heroInfoBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.heroView)).EndInit();
            this.eventBox.ResumeLayout(false);
            this.eventBox.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button settingsButton;
        private System.Windows.Forms.GroupBox heroInfoBox;
        private System.Windows.Forms.Label labelHeroHealth;
        private System.Windows.Forms.Button useButton;
        private System.Windows.Forms.Label labelHeroClass;
        private System.Windows.Forms.Label labelHeroGold;
        private System.Windows.Forms.Label heroWeight;
        private System.Windows.Forms.Label heroClass;
        private System.Windows.Forms.Label heroHealth;
        private System.Windows.Forms.Label labelHeroItems;
        private System.Windows.Forms.Button throwButton;
        private System.Windows.Forms.ListBox heroItems;
        private System.Windows.Forms.PictureBox heroView;
        private System.Windows.Forms.RichTextBox history;
        private System.Windows.Forms.GroupBox eventBox;
        private System.Windows.Forms.Label eventText;
        private System.Windows.Forms.Button quickAidButton;
        private System.Windows.Forms.ComboBox eventComboBox;
        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.Label heroGold;
        private System.Windows.Forms.Button quickHealButton;
        private System.Windows.Forms.Button quickDamageButton;
        private System.Windows.Forms.ListBox heroEquipment;
        private System.Windows.Forms.Label labelEventCreatureName;
        private System.Windows.Forms.Label labelEventCreatureClass;
        private System.Windows.Forms.Label labelEventCreatureLevel;
        private System.Windows.Forms.Label eventCreatureName;
        private System.Windows.Forms.Label eventCreatureLevel;
        private System.Windows.Forms.Label eventCreatureClass;
        private System.Windows.Forms.Button attackButton;
    }
}