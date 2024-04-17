
namespace BizyaevKursach
{
    partial class MainForm
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

     #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.generalTabControl = new System.Windows.Forms.TabControl();
            this.historyPage = new System.Windows.Forms.TabPage();
            this.doneOrdersList = new System.Windows.Forms.TableLayoutPanel();
            this.historyPageClear = new System.Windows.Forms.Label();
            this.profilePage = new System.Windows.Forms.TabPage();
            this.editBox = new System.Windows.Forms.GroupBox();
            this.hiddenOrdersListButton = new System.Windows.Forms.Button();
            this.editPhotoButton = new System.Windows.Forms.Button();
            this.editInfoButton = new System.Windows.Forms.Button();
            this.statBox = new System.Windows.Forms.GroupBox();
            this.registrationDateLabel = new System.Windows.Forms.Label();
            this.doneOrdersCountLabel = new System.Windows.Forms.Label();
            this.canDeliveryLabel = new System.Windows.Forms.Label();
            this.infoBox = new System.Windows.Forms.GroupBox();
            this.telephoneNumberLabel = new System.Windows.Forms.MaskedTextBox();
            this.idLabel = new System.Windows.Forms.Label();
            this.nameLabel = new System.Windows.Forms.Label();
            this.courierPhoto = new System.Windows.Forms.PictureBox();
            this.numberLabel = new System.Windows.Forms.Label();
            this.crutch = new System.Windows.Forms.Panel();
            this.activeOrdersPage = new System.Windows.Forms.TabPage();
            this.activeOrdersList = new System.Windows.Forms.TableLayoutPanel();
            this.activeOrdersClear = new System.Windows.Forms.Label();
            this.inactiveOrdersPage = new System.Windows.Forms.TabPage();
            this.inactiveOrdersList = new System.Windows.Forms.TableLayoutPanel();
            this.inactiveOrdersClear = new System.Windows.Forms.Label();
            this.tabControlIcons = new System.Windows.Forms.ImageList(this.components);
            this.inactiveOrdersCount = new System.Windows.Forms.Label();
            this.activeOrdersCount = new System.Windows.Forms.Label();
            this.exit = new System.Windows.Forms.Label();
            this.generalTabControl.SuspendLayout();
            this.historyPage.SuspendLayout();
            this.profilePage.SuspendLayout();
            this.editBox.SuspendLayout();
            this.statBox.SuspendLayout();
            this.infoBox.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.courierPhoto)).BeginInit();
            this.crutch.SuspendLayout();
            this.activeOrdersPage.SuspendLayout();
            this.inactiveOrdersPage.SuspendLayout();
            this.SuspendLayout();
            // 
            // generalTabControl
            // 
            this.generalTabControl.Alignment = System.Windows.Forms.TabAlignment.Bottom;
            this.generalTabControl.Controls.Add(this.historyPage);
            this.generalTabControl.Controls.Add(this.profilePage);
            this.generalTabControl.Controls.Add(this.activeOrdersPage);
            this.generalTabControl.Controls.Add(this.inactiveOrdersPage);
            this.generalTabControl.Cursor = System.Windows.Forms.Cursors.Default;
            this.generalTabControl.Dock = System.Windows.Forms.DockStyle.Fill;
            this.generalTabControl.ImageList = this.tabControlIcons;
            this.generalTabControl.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.generalTabControl.ItemSize = new System.Drawing.Size(110, 88);
            this.generalTabControl.Location = new System.Drawing.Point(0, 0);
            this.generalTabControl.Margin = new System.Windows.Forms.Padding(0);
            this.generalTabControl.Name = "generalTabControl";
            this.generalTabControl.Padding = new System.Drawing.Point(0, 0);
            this.generalTabControl.SelectedIndex = 0;
            this.generalTabControl.Size = new System.Drawing.Size(443, 450);
            this.generalTabControl.SizeMode = System.Windows.Forms.TabSizeMode.Fixed;
            this.generalTabControl.TabIndex = 0;
            this.generalTabControl.TabStop = false;
            // 
            // historyPage
            // 
            this.historyPage.AutoScroll = true;
            this.historyPage.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.historyPage.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.historyPage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.historyPage.Controls.Add(this.doneOrdersList);
            this.historyPage.Controls.Add(this.historyPageClear);
            this.historyPage.ImageKey = "history.png";
            this.historyPage.Location = new System.Drawing.Point(4, 4);
            this.historyPage.Margin = new System.Windows.Forms.Padding(0);
            this.historyPage.Name = "historyPage";
            this.historyPage.Size = new System.Drawing.Size(435, 354);
            this.historyPage.TabIndex = 1;
            // 
            // doneOrdersList
            // 
            this.doneOrdersList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(255)))));
            this.doneOrdersList.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Outset;
            this.doneOrdersList.ColumnCount = 1;
            this.doneOrdersList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.doneOrdersList.Dock = System.Windows.Forms.DockStyle.Top;
            this.doneOrdersList.Location = new System.Drawing.Point(0, 0);
            this.doneOrdersList.Margin = new System.Windows.Forms.Padding(0);
            this.doneOrdersList.Name = "doneOrdersList";
            this.doneOrdersList.RowCount = 1;
            this.doneOrdersList.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.doneOrdersList.Size = new System.Drawing.Size(431, 0);
            this.doneOrdersList.TabIndex = 3;
            this.doneOrdersList.ControlAdded += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlAdded);
            this.doneOrdersList.ControlRemoved += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlRemoved);
            // 
            // historyPageClear
            // 
            this.historyPageClear.Dock = System.Windows.Forms.DockStyle.Fill;
            this.historyPageClear.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.historyPageClear.ForeColor = System.Drawing.Color.Black;
            this.historyPageClear.Location = new System.Drawing.Point(0, 0);
            this.historyPageClear.Margin = new System.Windows.Forms.Padding(0);
            this.historyPageClear.Name = "historyPageClear";
            this.historyPageClear.Size = new System.Drawing.Size(431, 350);
            this.historyPageClear.TabIndex = 14;
            this.historyPageClear.Text = "Здесь отображается ваша история заказов.\r\n\r\nЗаказ добавляется в историю, \r\nесли б" +
    "ыл успешно вами доставлен.";
            this.historyPageClear.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // profilePage
            // 
            this.profilePage.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.profilePage.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.profilePage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.profilePage.Controls.Add(this.editBox);
            this.profilePage.Controls.Add(this.statBox);
            this.profilePage.Controls.Add(this.infoBox);
            this.profilePage.Controls.Add(this.courierPhoto);
            this.profilePage.Controls.Add(this.crutch);
            this.profilePage.ImageKey = "profile.png";
            this.profilePage.Location = new System.Drawing.Point(4, 4);
            this.profilePage.Margin = new System.Windows.Forms.Padding(6);
            this.profilePage.Name = "profilePage";
            this.profilePage.Padding = new System.Windows.Forms.Padding(6);
            this.profilePage.Size = new System.Drawing.Size(435, 354);
            this.profilePage.TabIndex = 0;
            // 
            // editBox
            // 
            this.editBox.Controls.Add(this.hiddenOrdersListButton);
            this.editBox.Controls.Add(this.editPhotoButton);
            this.editBox.Controls.Add(this.editInfoButton);
            this.editBox.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.editBox.Location = new System.Drawing.Point(271, 202);
            this.editBox.Name = "editBox";
            this.editBox.Size = new System.Drawing.Size(152, 142);
            this.editBox.TabIndex = 24;
            this.editBox.TabStop = false;
            this.editBox.Text = "Изменить";
            // 
            // hiddenOrdersListButton
            // 
            this.hiddenOrdersListButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.hiddenOrdersListButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(218)))), ((int)(((byte)(255)))));
            this.hiddenOrdersListButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.hiddenOrdersListButton.DialogResult = System.Windows.Forms.DialogResult.Yes;
            this.hiddenOrdersListButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.hiddenOrdersListButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.hiddenOrdersListButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.hiddenOrdersListButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.hiddenOrdersListButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.hiddenOrdersListButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.hiddenOrdersListButton.Location = new System.Drawing.Point(6, 103);
            this.hiddenOrdersListButton.Name = "hiddenOrdersListButton";
            this.hiddenOrdersListButton.Size = new System.Drawing.Size(140, 33);
            this.hiddenOrdersListButton.TabIndex = 22;
            this.hiddenOrdersListButton.TabStop = false;
            this.hiddenOrdersListButton.Text = "Скрытые заказы";
            this.hiddenOrdersListButton.UseVisualStyleBackColor = false;
            this.hiddenOrdersListButton.Click += new System.EventHandler(this.hiddenOrdersListButton_Click);
            // 
            // editPhotoButton
            // 
            this.editPhotoButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.editPhotoButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(218)))), ((int)(((byte)(255)))));
            this.editPhotoButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.editPhotoButton.DialogResult = System.Windows.Forms.DialogResult.Yes;
            this.editPhotoButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.editPhotoButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.editPhotoButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.editPhotoButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.editPhotoButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.editPhotoButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.editPhotoButton.Location = new System.Drawing.Point(6, 25);
            this.editPhotoButton.Name = "editPhotoButton";
            this.editPhotoButton.Size = new System.Drawing.Size(140, 33);
            this.editPhotoButton.TabIndex = 23;
            this.editPhotoButton.TabStop = false;
            this.editPhotoButton.Text = "Фото";
            this.editPhotoButton.UseVisualStyleBackColor = false;
            this.editPhotoButton.Click += new System.EventHandler(this.courierPhoto_DoubleClick);
            // 
            // editInfoButton
            // 
            this.editInfoButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.editInfoButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(218)))), ((int)(((byte)(255)))));
            this.editInfoButton.Cursor = System.Windows.Forms.Cursors.Hand;
            this.editInfoButton.DialogResult = System.Windows.Forms.DialogResult.Yes;
            this.editInfoButton.FlatAppearance.BorderColor = System.Drawing.Color.FromArgb(((int)(((byte)(77)))), ((int)(((byte)(61)))), ((int)(((byte)(54)))));
            this.editInfoButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.editInfoButton.FlatAppearance.MouseOverBackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(128)))), ((int)(((byte)(255)))));
            this.editInfoButton.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.editInfoButton.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.editInfoButton.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(192)))));
            this.editInfoButton.Location = new System.Drawing.Point(6, 64);
            this.editInfoButton.Name = "editInfoButton";
            this.editInfoButton.Size = new System.Drawing.Size(140, 33);
            this.editInfoButton.TabIndex = 22;
            this.editInfoButton.TabStop = false;
            this.editInfoButton.Text = "Данные";
            this.editInfoButton.UseVisualStyleBackColor = false;
            this.editInfoButton.Click += new System.EventHandler(this.editInfoButton_Click);
            // 
            // statBox
            // 
            this.statBox.Controls.Add(this.registrationDateLabel);
            this.statBox.Controls.Add(this.doneOrdersCountLabel);
            this.statBox.Controls.Add(this.canDeliveryLabel);
            this.statBox.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.statBox.Font = new System.Drawing.Font("Century Gothic", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.statBox.Location = new System.Drawing.Point(7, 173);
            this.statBox.Name = "statBox";
            this.statBox.Size = new System.Drawing.Size(257, 171);
            this.statBox.TabIndex = 20;
            this.statBox.TabStop = false;
            this.statBox.Text = "Статистика";
            // 
            // registrationDateLabel
            // 
            this.registrationDateLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.registrationDateLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.registrationDateLabel.ForeColor = System.Drawing.Color.Black;
            this.registrationDateLabel.Location = new System.Drawing.Point(6, 26);
            this.registrationDateLabel.Margin = new System.Windows.Forms.Padding(3);
            this.registrationDateLabel.Name = "registrationDateLabel";
            this.registrationDateLabel.Size = new System.Drawing.Size(245, 21);
            this.registrationDateLabel.TabIndex = 17;
            this.registrationDateLabel.Text = "Дата регистрации: ";
            // 
            // doneOrdersCountLabel
            // 
            this.doneOrdersCountLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.doneOrdersCountLabel.AutoEllipsis = true;
            this.doneOrdersCountLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.doneOrdersCountLabel.ForeColor = System.Drawing.Color.Black;
            this.doneOrdersCountLabel.Location = new System.Drawing.Point(6, 53);
            this.doneOrdersCountLabel.Margin = new System.Windows.Forms.Padding(3);
            this.doneOrdersCountLabel.Name = "doneOrdersCountLabel";
            this.doneOrdersCountLabel.Size = new System.Drawing.Size(245, 21);
            this.doneOrdersCountLabel.TabIndex = 18;
            this.doneOrdersCountLabel.Text = "Доставил заказов: ";
            // 
            // canDeliveryLabel
            // 
            this.canDeliveryLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.canDeliveryLabel.AutoEllipsis = true;
            this.canDeliveryLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.canDeliveryLabel.ForeColor = System.Drawing.Color.Black;
            this.canDeliveryLabel.Location = new System.Drawing.Point(6, 80);
            this.canDeliveryLabel.Margin = new System.Windows.Forms.Padding(3);
            this.canDeliveryLabel.Name = "canDeliveryLabel";
            this.canDeliveryLabel.Size = new System.Drawing.Size(245, 88);
            this.canDeliveryLabel.TabIndex = 16;
            this.canDeliveryLabel.Text = "Могу доставить: ";
            // 
            // infoBox
            // 
            this.infoBox.Controls.Add(this.telephoneNumberLabel);
            this.infoBox.Controls.Add(this.idLabel);
            this.infoBox.Controls.Add(this.nameLabel);
            this.infoBox.FlatStyle = System.Windows.Forms.FlatStyle.System;
            this.infoBox.Font = new System.Drawing.Font("Century Gothic", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.infoBox.Location = new System.Drawing.Point(7, 41);
            this.infoBox.Name = "infoBox";
            this.infoBox.Size = new System.Drawing.Size(257, 132);
            this.infoBox.TabIndex = 19;
            this.infoBox.TabStop = false;
            this.infoBox.Text = "Персональные данные";
            // 
            // telephoneNumberLabel
            // 
            this.telephoneNumberLabel.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(192)))), ((int)(((byte)(255)))));
            this.telephoneNumberLabel.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.telephoneNumberLabel.Font = new System.Drawing.Font("Century Gothic", 12F);
            this.telephoneNumberLabel.Location = new System.Drawing.Point(10, 53);
            this.telephoneNumberLabel.Mask = "Телефон: 8 (999) 000-0000";
            this.telephoneNumberLabel.Name = "telephoneNumberLabel";
            this.telephoneNumberLabel.Size = new System.Drawing.Size(241, 20);
            this.telephoneNumberLabel.TabIndex = 18;
            // 
            // idLabel
            // 
            this.idLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.idLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.idLabel.ForeColor = System.Drawing.Color.Black;
            this.idLabel.Location = new System.Drawing.Point(6, 26);
            this.idLabel.Margin = new System.Windows.Forms.Padding(3);
            this.idLabel.Name = "idLabel";
            this.idLabel.Size = new System.Drawing.Size(245, 21);
            this.idLabel.TabIndex = 17;
            this.idLabel.Text = "ID: ";
            // 
            // nameLabel
            // 
            this.nameLabel.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.nameLabel.Font = new System.Drawing.Font("Century Gothic", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.nameLabel.ForeColor = System.Drawing.Color.Black;
            this.nameLabel.Location = new System.Drawing.Point(6, 80);
            this.nameLabel.Margin = new System.Windows.Forms.Padding(3);
            this.nameLabel.Name = "nameLabel";
            this.nameLabel.Size = new System.Drawing.Size(245, 41);
            this.nameLabel.TabIndex = 16;
            this.nameLabel.Text = "ФИО: ";
            // 
            // courierPhoto
            // 
            this.courierPhoto.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(218)))), ((int)(((byte)(255)))));
            this.courierPhoto.BackgroundImage = global::BizyaevKursach.Properties.Resources.courier_photo;
            this.courierPhoto.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.courierPhoto.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.courierPhoto.Location = new System.Drawing.Point(273, 41);
            this.courierPhoto.Margin = new System.Windows.Forms.Padding(6);
            this.courierPhoto.Name = "courierPhoto";
            this.courierPhoto.Size = new System.Drawing.Size(152, 160);
            this.courierPhoto.TabIndex = 12;
            this.courierPhoto.TabStop = false;
            this.courierPhoto.DoubleClick += new System.EventHandler(this.courierPhoto_DoubleClick);
            // 
            // numberLabel
            // 
            this.numberLabel.Font = new System.Drawing.Font("Century Gothic", 18F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.numberLabel.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(64)))));
            this.numberLabel.Location = new System.Drawing.Point(6, 3);
            this.numberLabel.Name = "numberLabel";
            this.numberLabel.Size = new System.Drawing.Size(235, 38);
            this.numberLabel.TabIndex = 11;
            this.numberLabel.Text = "Профиль курьера";
            // 
            // crutch
            // 
            this.crutch.Controls.Add(this.exit);
            this.crutch.Controls.Add(this.numberLabel);
            this.crutch.Location = new System.Drawing.Point(0, 0);
            this.crutch.Name = "crutch";
            this.crutch.Size = new System.Drawing.Size(431, 350);
            this.crutch.TabIndex = 19;
            // 
            // activeOrdersPage
            // 
            this.activeOrdersPage.AutoScroll = true;
            this.activeOrdersPage.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.activeOrdersPage.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.activeOrdersPage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.activeOrdersPage.Controls.Add(this.activeOrdersList);
            this.activeOrdersPage.Controls.Add(this.activeOrdersClear);
            this.activeOrdersPage.ImageKey = "active-orders-icon.png";
            this.activeOrdersPage.Location = new System.Drawing.Point(4, 4);
            this.activeOrdersPage.Margin = new System.Windows.Forms.Padding(0);
            this.activeOrdersPage.Name = "activeOrdersPage";
            this.activeOrdersPage.Size = new System.Drawing.Size(435, 354);
            this.activeOrdersPage.TabIndex = 2;
            // 
            // activeOrdersList
            // 
            this.activeOrdersList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(192)))), ((int)(((byte)(255)))), ((int)(((byte)(192)))));
            this.activeOrdersList.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Outset;
            this.activeOrdersList.ColumnCount = 1;
            this.activeOrdersList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.activeOrdersList.Dock = System.Windows.Forms.DockStyle.Top;
            this.activeOrdersList.Location = new System.Drawing.Point(0, 0);
            this.activeOrdersList.Margin = new System.Windows.Forms.Padding(0);
            this.activeOrdersList.Name = "activeOrdersList";
            this.activeOrdersList.RowCount = 1;
            this.activeOrdersList.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.activeOrdersList.Size = new System.Drawing.Size(431, 0);
            this.activeOrdersList.TabIndex = 2;
            this.activeOrdersList.ControlAdded += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlAdded);
            this.activeOrdersList.ControlRemoved += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlRemoved);
            // 
            // activeOrdersClear
            // 
            this.activeOrdersClear.Dock = System.Windows.Forms.DockStyle.Fill;
            this.activeOrdersClear.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.activeOrdersClear.ForeColor = System.Drawing.Color.Black;
            this.activeOrdersClear.Location = new System.Drawing.Point(0, 0);
            this.activeOrdersClear.Margin = new System.Windows.Forms.Padding(0);
            this.activeOrdersClear.Name = "activeOrdersClear";
            this.activeOrdersClear.Size = new System.Drawing.Size(431, 350);
            this.activeOrdersClear.TabIndex = 13;
            this.activeOrdersClear.Text = "Здесь отображаются ваши активные заказы.\r\n\r\nЧтобы заказ стал активен, нажмите \"Пр" +
    "инять\"\r\nсоотвествующего заказа во вкладке неактивных заказов.";
            this.activeOrdersClear.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // inactiveOrdersPage
            // 
            this.inactiveOrdersPage.AutoScroll = true;
            this.inactiveOrdersPage.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(128)))), ((int)(((byte)(128)))));
            this.inactiveOrdersPage.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.inactiveOrdersPage.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.inactiveOrdersPage.Controls.Add(this.inactiveOrdersList);
            this.inactiveOrdersPage.Controls.Add(this.inactiveOrdersClear);
            this.inactiveOrdersPage.ImageKey = "inactive-order-icon.png";
            this.inactiveOrdersPage.Location = new System.Drawing.Point(4, 4);
            this.inactiveOrdersPage.Margin = new System.Windows.Forms.Padding(0);
            this.inactiveOrdersPage.Name = "inactiveOrdersPage";
            this.inactiveOrdersPage.Size = new System.Drawing.Size(435, 354);
            this.inactiveOrdersPage.TabIndex = 3;
            this.inactiveOrdersPage.Scroll += new System.Windows.Forms.ScrollEventHandler(this.ordersPage_Scroll);
            // 
            // inactiveOrdersList
            // 
            this.inactiveOrdersList.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.inactiveOrdersList.CellBorderStyle = System.Windows.Forms.TableLayoutPanelCellBorderStyle.Outset;
            this.inactiveOrdersList.ColumnCount = 1;
            this.inactiveOrdersList.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.inactiveOrdersList.Dock = System.Windows.Forms.DockStyle.Top;
            this.inactiveOrdersList.Location = new System.Drawing.Point(0, 0);
            this.inactiveOrdersList.Margin = new System.Windows.Forms.Padding(0);
            this.inactiveOrdersList.Name = "inactiveOrdersList";
            this.inactiveOrdersList.RowCount = 1;
            this.inactiveOrdersList.RowStyles.Add(new System.Windows.Forms.RowStyle());
            this.inactiveOrdersList.Size = new System.Drawing.Size(431, 0);
            this.inactiveOrdersList.TabIndex = 6;
            this.inactiveOrdersList.ControlAdded += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlAdded);
            this.inactiveOrdersList.ControlRemoved += new System.Windows.Forms.ControlEventHandler(this.ordersList_ControlRemoved);
            // 
            // inactiveOrdersClear
            // 
            this.inactiveOrdersClear.Dock = System.Windows.Forms.DockStyle.Fill;
            this.inactiveOrdersClear.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.inactiveOrdersClear.ForeColor = System.Drawing.Color.Black;
            this.inactiveOrdersClear.Location = new System.Drawing.Point(0, 0);
            this.inactiveOrdersClear.Margin = new System.Windows.Forms.Padding(0);
            this.inactiveOrdersClear.Name = "inactiveOrdersClear";
            this.inactiveOrdersClear.Size = new System.Drawing.Size(431, 350);
            this.inactiveOrdersClear.TabIndex = 12;
            this.inactiveOrdersClear.Text = "Здесь отображаются неактивные заказы.\r\n\r\nНеактивные заказы добавляет куратор.\r\n\r\n" +
    "Скрытые заказы можно посмотреть во вкладке \r\n\"Профиль ➔ Посмотреть скрытые заказ" +
    "ы\"";
            this.inactiveOrdersClear.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // tabControlIcons
            // 
            this.tabControlIcons.ImageStream = ((System.Windows.Forms.ImageListStreamer)(resources.GetObject("tabControlIcons.ImageStream")));
            this.tabControlIcons.TransparentColor = System.Drawing.Color.Transparent;
            this.tabControlIcons.Images.SetKeyName(0, "inactive-order-icon.png");
            this.tabControlIcons.Images.SetKeyName(1, "active-orders-icon.png");
            this.tabControlIcons.Images.SetKeyName(2, "profile.png");
            this.tabControlIcons.Images.SetKeyName(3, "history.png");
            this.tabControlIcons.Images.SetKeyName(4, "main-page.png");
            // 
            // inactiveOrdersCount
            // 
            this.inactiveOrdersCount.BackColor = System.Drawing.Color.Red;
            this.inactiveOrdersCount.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.inactiveOrdersCount.Location = new System.Drawing.Point(396, 369);
            this.inactiveOrdersCount.Margin = new System.Windows.Forms.Padding(0);
            this.inactiveOrdersCount.Name = "inactiveOrdersCount";
            this.inactiveOrdersCount.Size = new System.Drawing.Size(22, 22);
            this.inactiveOrdersCount.TabIndex = 13;
            this.inactiveOrdersCount.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.inactiveOrdersCount.TextChanged += new System.EventHandler(this.ordersCount_TextChanged);
            this.inactiveOrdersCount.Paint += new System.Windows.Forms.PaintEventHandler(this.ordersCount_Paint);
            // 
            // activeOrdersCount
            // 
            this.activeOrdersCount.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(128)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
            this.activeOrdersCount.Font = new System.Drawing.Font("Century Gothic", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.activeOrdersCount.Location = new System.Drawing.Point(280, 369);
            this.activeOrdersCount.Margin = new System.Windows.Forms.Padding(0);
            this.activeOrdersCount.Name = "activeOrdersCount";
            this.activeOrdersCount.Size = new System.Drawing.Size(22, 22);
            this.activeOrdersCount.TabIndex = 14;
            this.activeOrdersCount.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            this.activeOrdersCount.TextChanged += new System.EventHandler(this.ordersCount_TextChanged);
            this.activeOrdersCount.Paint += new System.Windows.Forms.PaintEventHandler(this.ordersCount_Paint);
            // 
            // exit
            // 
            this.exit.AutoSize = true;
            this.exit.Font = new System.Drawing.Font("Century Gothic", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.exit.ForeColor = System.Drawing.Color.Black;
            this.exit.Location = new System.Drawing.Point(338, 8);
            this.exit.Name = "exit";
            this.exit.Size = new System.Drawing.Size(79, 25);
            this.exit.TabIndex = 12;
            this.exit.Text = "Выход";
            this.exit.Click += new System.EventHandler(this.exitButton_Click);
            this.exit.MouseEnter += new System.EventHandler(this.exit_MouseEnter);
            this.exit.MouseLeave += new System.EventHandler(this.exit_MouseLeave);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(443, 450);
            this.Controls.Add(this.activeOrdersCount);
            this.Controls.Add(this.inactiveOrdersCount);
            this.Controls.Add(this.generalTabControl);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.generalTabControl.ResumeLayout(false);
            this.historyPage.ResumeLayout(false);
            this.profilePage.ResumeLayout(false);
            this.editBox.ResumeLayout(false);
            this.statBox.ResumeLayout(false);
            this.infoBox.ResumeLayout(false);
            this.infoBox.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.courierPhoto)).EndInit();
            this.crutch.ResumeLayout(false);
            this.crutch.PerformLayout();
            this.activeOrdersPage.ResumeLayout(false);
            this.inactiveOrdersPage.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TabControl generalTabControl;
        private System.Windows.Forms.TabPage profilePage;
        private System.Windows.Forms.TabPage historyPage;
        private System.Windows.Forms.TabPage activeOrdersPage;
        private System.Windows.Forms.TabPage inactiveOrdersPage;
        private System.Windows.Forms.ImageList tabControlIcons;
        private System.Windows.Forms.TableLayoutPanel activeOrdersList;
        private System.Windows.Forms.TableLayoutPanel doneOrdersList;
        private System.Windows.Forms.TableLayoutPanel inactiveOrdersList;
        private System.Windows.Forms.Label historyPageClear;
        private System.Windows.Forms.Label numberLabel;
        private System.Windows.Forms.Label activeOrdersClear;
        private System.Windows.Forms.Label inactiveOrdersClear;
        private System.Windows.Forms.PictureBox courierPhoto;
        private System.Windows.Forms.Label inactiveOrdersCount;
        private System.Windows.Forms.Label activeOrdersCount;
        private System.Windows.Forms.Label idLabel;
        private System.Windows.Forms.Label nameLabel;
        private System.Windows.Forms.GroupBox infoBox;
        private System.Windows.Forms.GroupBox statBox;
        private System.Windows.Forms.Label registrationDateLabel;
        private System.Windows.Forms.Label doneOrdersCountLabel;
        private System.Windows.Forms.Label canDeliveryLabel;
        private System.Windows.Forms.MaskedTextBox telephoneNumberLabel;
        private System.Windows.Forms.GroupBox editBox;
        private System.Windows.Forms.Button hiddenOrdersListButton;
        private System.Windows.Forms.Button editPhotoButton;
        private System.Windows.Forms.Button editInfoButton;
        private System.Windows.Forms.Panel crutch;
        private System.Windows.Forms.Label exit;
    }
}

