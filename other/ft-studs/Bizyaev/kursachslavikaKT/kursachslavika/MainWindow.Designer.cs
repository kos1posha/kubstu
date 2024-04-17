
namespace kursachslavika
{
    partial class LZArchiver
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(LZArchiver));
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.closeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveDecodedTextToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveEncodedTextToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsDecodedTextToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsEncodedTextToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.contentToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.deleteChangesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.algorithmComboBox = new System.Windows.Forms.ToolStripComboBox();
            this.settingsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fontSizeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fontSizeComboBoxToolStrip = new System.Windows.Forms.ToolStripComboBox();
            this.separatorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.separatorComboBoxToolStrip = new System.Windows.Forms.ToolStripComboBox();
            this.closeWithClearCheckBox = new System.Windows.Forms.ToolStripMenuItem();
            this.tableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.encodedTableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.encodedTextClearButton = new System.Windows.Forms.Button();
            this.pasteToEncodedTextFromFileButton = new System.Windows.Forms.Button();
            this.showDecodedButton = new System.Windows.Forms.Button();
            this.encodedTextBox = new System.Windows.Forms.TextBox();
            this.codeButtonsPanel = new System.Windows.Forms.SplitContainer();
            this.encodeButton = new System.Windows.Forms.Button();
            this.decodeButton = new System.Windows.Forms.Button();
            this.decodedTextBox = new System.Windows.Forms.TextBox();
            this.decodedLabel = new System.Windows.Forms.Label();
            this.encodedLabel = new System.Windows.Forms.Label();
            this.decodedTableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.pasteToDecodedTextFromFileButton = new System.Windows.Forms.Button();
            this.showEncodedButton = new System.Windows.Forms.Button();
            this.decodedTextClearButton = new System.Windows.Forms.Button();
            this.sequenceLabel = new System.Windows.Forms.Label();
            this.bottomPanel = new System.Windows.Forms.Panel();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.menuStrip.SuspendLayout();
            this.tableLayoutPanel.SuspendLayout();
            this.encodedTableLayoutPanel.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.codeButtonsPanel)).BeginInit();
            this.codeButtonsPanel.Panel1.SuspendLayout();
            this.codeButtonsPanel.Panel2.SuspendLayout();
            this.codeButtonsPanel.SuspendLayout();
            this.decodedTableLayoutPanel.SuspendLayout();
            this.bottomPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip
            // 
            this.menuStrip.BackColor = System.Drawing.SystemColors.ControlLight;
            this.menuStrip.GripMargin = new System.Windows.Forms.Padding(3);
            this.menuStrip.GripStyle = System.Windows.Forms.ToolStripGripStyle.Visible;
            this.menuStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.algorithmComboBox,
            this.settingsToolStripMenuItem});
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Size = new System.Drawing.Size(784, 25);
            this.menuStrip.TabIndex = 0;
            this.menuStrip.Text = "menuStrip";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openToolStripMenuItem,
            this.closeToolStripMenuItem,
            this.saveToolStripMenuItem,
            this.saveAsToolStripMenuItem,
            this.toolStripSeparator1,
            this.contentToolStripMenuItem,
            this.deleteChangesToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(48, 21);
            this.fileToolStripMenuItem.Text = "Файл";
            // 
            // openToolStripMenuItem
            // 
            this.openToolStripMenuItem.Name = "openToolStripMenuItem";
            this.openToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.openToolStripMenuItem.Text = "Открыть";
            this.openToolStripMenuItem.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // closeToolStripMenuItem
            // 
            this.closeToolStripMenuItem.Name = "closeToolStripMenuItem";
            this.closeToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.closeToolStripMenuItem.Text = "Закрыть";
            this.closeToolStripMenuItem.Click += new System.EventHandler(this.closeToolStripMenuItem_Click);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.saveDecodedTextToolStripMenuItem,
            this.saveEncodedTextToolStripMenuItem});
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.saveToolStripMenuItem.Text = "Сохранить";
            // 
            // saveDecodedTextToolStripMenuItem
            // 
            this.saveDecodedTextToolStripMenuItem.Name = "saveDecodedTextToolStripMenuItem";
            this.saveDecodedTextToolStripMenuItem.Size = new System.Drawing.Size(200, 22);
            this.saveDecodedTextToolStripMenuItem.Text = "Исходный текст";
            this.saveDecodedTextToolStripMenuItem.Click += new System.EventHandler(this.saveDecodedTextToolStripMenuItem_Click);
            // 
            // saveEncodedTextToolStripMenuItem
            // 
            this.saveEncodedTextToolStripMenuItem.Name = "saveEncodedTextToolStripMenuItem";
            this.saveEncodedTextToolStripMenuItem.Size = new System.Drawing.Size(200, 22);
            this.saveEncodedTextToolStripMenuItem.Text = "Закодированный текст";
            this.saveEncodedTextToolStripMenuItem.Click += new System.EventHandler(this.saveEncodedTextToolStripMenuItem_Click);
            // 
            // saveAsToolStripMenuItem
            // 
            this.saveAsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.saveAsDecodedTextToolStripMenuItem,
            this.saveAsEncodedTextToolStripMenuItem});
            this.saveAsToolStripMenuItem.Name = "saveAsToolStripMenuItem";
            this.saveAsToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.saveAsToolStripMenuItem.Text = "Сохранить как";
            // 
            // saveAsDecodedTextToolStripMenuItem
            // 
            this.saveAsDecodedTextToolStripMenuItem.Name = "saveAsDecodedTextToolStripMenuItem";
            this.saveAsDecodedTextToolStripMenuItem.Size = new System.Drawing.Size(200, 22);
            this.saveAsDecodedTextToolStripMenuItem.Text = "Исходный текст";
            this.saveAsDecodedTextToolStripMenuItem.Click += new System.EventHandler(this.saveAsDecodedTextToolStripMenuItemToolStripMenuItem_Click);
            // 
            // saveAsEncodedTextToolStripMenuItem
            // 
            this.saveAsEncodedTextToolStripMenuItem.Name = "saveAsEncodedTextToolStripMenuItem";
            this.saveAsEncodedTextToolStripMenuItem.Size = new System.Drawing.Size(200, 22);
            this.saveAsEncodedTextToolStripMenuItem.Text = "Закодированный текст";
            this.saveAsEncodedTextToolStripMenuItem.Click += new System.EventHandler(this.saveAsEncodedTextToolStripMenuItemToolStripMenuItem_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(178, 6);
            // 
            // contentToolStripMenuItem
            // 
            this.contentToolStripMenuItem.Name = "contentToolStripMenuItem";
            this.contentToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.contentToolStripMenuItem.Text = "Содержимое";
            this.contentToolStripMenuItem.Click += new System.EventHandler(this.contentToolStripMenuItem_Click);
            // 
            // deleteChangesToolStripMenuItem
            // 
            this.deleteChangesToolStripMenuItem.Name = "deleteChangesToolStripMenuItem";
            this.deleteChangesToolStripMenuItem.Size = new System.Drawing.Size(181, 22);
            this.deleteChangesToolStripMenuItem.Text = "Удалить изменения";
            this.deleteChangesToolStripMenuItem.Click += new System.EventHandler(this.deleteChangesToolStripMenuItem_Click);
            // 
            // algorithmComboBox
            // 
            this.algorithmComboBox.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
            this.algorithmComboBox.BackColor = System.Drawing.Color.White;
            this.algorithmComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.algorithmComboBox.FlatStyle = System.Windows.Forms.FlatStyle.Standard;
            this.algorithmComboBox.Font = new System.Drawing.Font("Segoe UI", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.algorithmComboBox.Items.AddRange(new object[] {
            "LZ77",
            "LZ78"});
            this.algorithmComboBox.Margin = new System.Windows.Forms.Padding(3, 0, 12, 0);
            this.algorithmComboBox.Name = "algorithmComboBox";
            this.algorithmComboBox.Size = new System.Drawing.Size(121, 21);
            // 
            // settingsToolStripMenuItem
            // 
            this.settingsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fontSizeToolStripMenuItem,
            this.separatorToolStripMenuItem,
            this.closeWithClearCheckBox});
            this.settingsToolStripMenuItem.Name = "settingsToolStripMenuItem";
            this.settingsToolStripMenuItem.Size = new System.Drawing.Size(79, 21);
            this.settingsToolStripMenuItem.Text = "Настройки";
            // 
            // fontSizeToolStripMenuItem
            // 
            this.fontSizeToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fontSizeComboBoxToolStrip});
            this.fontSizeToolStripMenuItem.Name = "fontSizeToolStripMenuItem";
            this.fontSizeToolStripMenuItem.Size = new System.Drawing.Size(289, 22);
            this.fontSizeToolStripMenuItem.Text = "Размер шрифта";
            // 
            // fontSizeComboBoxToolStrip
            // 
            this.fontSizeComboBoxToolStrip.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.fontSizeComboBoxToolStrip.Items.AddRange(new object[] {
            "8",
            "10",
            "12",
            "14",
            "16",
            "18",
            "20",
            "22",
            "24",
            "28",
            "36",
            "48",
            "72"});
            this.fontSizeComboBoxToolStrip.Name = "fontSizeComboBoxToolStrip";
            this.fontSizeComboBoxToolStrip.Size = new System.Drawing.Size(180, 23);
            this.fontSizeComboBoxToolStrip.SelectedIndexChanged += new System.EventHandler(this.fontSizeComboBoxToolStrip_SelectedIndexChanged);
            // 
            // separatorToolStripMenuItem
            // 
            this.separatorToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.separatorComboBoxToolStrip});
            this.separatorToolStripMenuItem.Name = "separatorToolStripMenuItem";
            this.separatorToolStripMenuItem.Size = new System.Drawing.Size(289, 22);
            this.separatorToolStripMenuItem.Text = "Символ-разделитель";
            // 
            // separatorComboBoxToolStrip
            // 
            this.separatorComboBoxToolStrip.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.separatorComboBoxToolStrip.Items.AddRange(new object[] {
            "Пробел",
            ".",
            "-",
            "_",
            "/",
            "@",
            "*",
            ":",
            ";",
            "`",
            "~",
            "#",
            "$"});
            this.separatorComboBoxToolStrip.MaxLength = 1;
            this.separatorComboBoxToolStrip.Name = "separatorComboBoxToolStrip";
            this.separatorComboBoxToolStrip.Size = new System.Drawing.Size(100, 23);
            // 
            // closeWithClearCheckBox
            // 
            this.closeWithClearCheckBox.Checked = true;
            this.closeWithClearCheckBox.CheckState = System.Windows.Forms.CheckState.Checked;
            this.closeWithClearCheckBox.Name = "closeWithClearCheckBox";
            this.closeWithClearCheckBox.Size = new System.Drawing.Size(289, 22);
            this.closeWithClearCheckBox.Text = "Очищать буферы при закрытии файла";
            this.closeWithClearCheckBox.Click += new System.EventHandler(this.closeWithoutClearCheckBox_Click);
            // 
            // tableLayoutPanel
            // 
            this.tableLayoutPanel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tableLayoutPanel.BackColor = System.Drawing.SystemColors.Control;
            this.tableLayoutPanel.ColumnCount = 3;
            this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 45F));
            this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel.Controls.Add(this.encodedTableLayoutPanel, 2, 2);
            this.tableLayoutPanel.Controls.Add(this.encodedTextBox, 2, 1);
            this.tableLayoutPanel.Controls.Add(this.codeButtonsPanel, 1, 1);
            this.tableLayoutPanel.Controls.Add(this.decodedTextBox, 0, 1);
            this.tableLayoutPanel.Controls.Add(this.decodedLabel, 0, 0);
            this.tableLayoutPanel.Controls.Add(this.encodedLabel, 2, 0);
            this.tableLayoutPanel.Controls.Add(this.decodedTableLayoutPanel, 0, 2);
            this.tableLayoutPanel.Location = new System.Drawing.Point(0, 27);
            this.tableLayoutPanel.Margin = new System.Windows.Forms.Padding(0, 3, 0, 0);
            this.tableLayoutPanel.Name = "tableLayoutPanel";
            this.tableLayoutPanel.RowCount = 3;
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 24F));
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 50F));
            this.tableLayoutPanel.Size = new System.Drawing.Size(784, 353);
            this.tableLayoutPanel.TabIndex = 1;
            // 
            // encodedTableLayoutPanel
            // 
            this.encodedTableLayoutPanel.ColumnCount = 3;
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.Controls.Add(this.encodedTextClearButton, 2, 0);
            this.encodedTableLayoutPanel.Controls.Add(this.pasteToEncodedTextFromFileButton, 0, 0);
            this.encodedTableLayoutPanel.Controls.Add(this.showDecodedButton, 1, 0);
            this.encodedTableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedTableLayoutPanel.Location = new System.Drawing.Point(417, 306);
            this.encodedTableLayoutPanel.Name = "encodedTableLayoutPanel";
            this.encodedTableLayoutPanel.RowCount = 1;
            this.encodedTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.encodedTableLayoutPanel.Size = new System.Drawing.Size(364, 44);
            this.encodedTableLayoutPanel.TabIndex = 8;
            // 
            // encodedTextClearButton
            // 
            this.encodedTextClearButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedTextClearButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodedTextClearButton.Location = new System.Drawing.Point(245, 3);
            this.encodedTextClearButton.Name = "encodedTextClearButton";
            this.encodedTextClearButton.Size = new System.Drawing.Size(116, 38);
            this.encodedTextClearButton.TabIndex = 8;
            this.encodedTextClearButton.Text = "Очистить";
            this.encodedTextClearButton.UseVisualStyleBackColor = true;
            this.encodedTextClearButton.Click += new System.EventHandler(this.encodedTextClearButton_Click);
            // 
            // pasteToEncodedTextFromFileButton
            // 
            this.pasteToEncodedTextFromFileButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pasteToEncodedTextFromFileButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.pasteToEncodedTextFromFileButton.Location = new System.Drawing.Point(3, 3);
            this.pasteToEncodedTextFromFileButton.Name = "pasteToEncodedTextFromFileButton";
            this.pasteToEncodedTextFromFileButton.Size = new System.Drawing.Size(115, 38);
            this.pasteToEncodedTextFromFileButton.TabIndex = 6;
            this.pasteToEncodedTextFromFileButton.Text = "Вставить из файла";
            this.pasteToEncodedTextFromFileButton.UseVisualStyleBackColor = true;
            this.pasteToEncodedTextFromFileButton.Click += new System.EventHandler(this.pasteToEncodedTextFromFileButton_Click);
            // 
            // showDecodedButton
            // 
            this.showDecodedButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.showDecodedButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.showDecodedButton.Location = new System.Drawing.Point(124, 3);
            this.showDecodedButton.Name = "showDecodedButton";
            this.showDecodedButton.Size = new System.Drawing.Size(115, 38);
            this.showDecodedButton.TabIndex = 7;
            this.showDecodedButton.Text = "Предпоказ декодировки";
            this.showDecodedButton.UseVisualStyleBackColor = true;
            this.showDecodedButton.Click += new System.EventHandler(this.showDecodedButton_Click);
            // 
            // encodedTextBox
            // 
            this.encodedTextBox.BackColor = System.Drawing.SystemColors.Window;
            this.encodedTextBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodedTextBox.Location = new System.Drawing.Point(417, 27);
            this.encodedTextBox.Multiline = true;
            this.encodedTextBox.Name = "encodedTextBox";
            this.encodedTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.encodedTextBox.Size = new System.Drawing.Size(364, 273);
            this.encodedTextBox.TabIndex = 2;
            // 
            // codeButtonsPanel
            // 
            this.codeButtonsPanel.BackColor = System.Drawing.SystemColors.Control;
            this.codeButtonsPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.codeButtonsPanel.Location = new System.Drawing.Point(372, 27);
            this.codeButtonsPanel.Name = "codeButtonsPanel";
            this.codeButtonsPanel.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // codeButtonsPanel.Panel1
            // 
            this.codeButtonsPanel.Panel1.Controls.Add(this.encodeButton);
            this.codeButtonsPanel.Panel1.Padding = new System.Windows.Forms.Padding(0, 0, 0, 9);
            // 
            // codeButtonsPanel.Panel2
            // 
            this.codeButtonsPanel.Panel2.Controls.Add(this.decodeButton);
            this.codeButtonsPanel.Panel2.Padding = new System.Windows.Forms.Padding(0, 9, 0, 0);
            this.codeButtonsPanel.Size = new System.Drawing.Size(39, 273);
            this.codeButtonsPanel.SplitterDistance = 131;
            this.codeButtonsPanel.SplitterWidth = 28;
            this.codeButtonsPanel.TabIndex = 0;
            // 
            // encodeButton
            // 
            this.encodeButton.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.encodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodeButton.Location = new System.Drawing.Point(0, 85);
            this.encodeButton.Name = "encodeButton";
            this.encodeButton.Size = new System.Drawing.Size(39, 37);
            this.encodeButton.TabIndex = 0;
            this.encodeButton.Text = "->";
            this.encodeButton.UseVisualStyleBackColor = true;
            this.encodeButton.Click += new System.EventHandler(this.encodeButton_Click);
            // 
            // decodeButton
            // 
            this.decodeButton.Dock = System.Windows.Forms.DockStyle.Top;
            this.decodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodeButton.Location = new System.Drawing.Point(0, 9);
            this.decodeButton.Name = "decodeButton";
            this.decodeButton.Size = new System.Drawing.Size(39, 37);
            this.decodeButton.TabIndex = 1;
            this.decodeButton.Text = "<-";
            this.decodeButton.UseVisualStyleBackColor = true;
            this.decodeButton.Click += new System.EventHandler(this.decodeButton_Click);
            // 
            // decodedTextBox
            // 
            this.decodedTextBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodedTextBox.Location = new System.Drawing.Point(3, 27);
            this.decodedTextBox.Multiline = true;
            this.decodedTextBox.Name = "decodedTextBox";
            this.decodedTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.decodedTextBox.Size = new System.Drawing.Size(363, 273);
            this.decodedTextBox.TabIndex = 1;
            this.decodedTextBox.Text = "abracadabra";
            // 
            // decodedLabel
            // 
            this.decodedLabel.AutoSize = true;
            this.decodedLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodedLabel.Location = new System.Drawing.Point(3, 0);
            this.decodedLabel.Name = "decodedLabel";
            this.decodedLabel.Size = new System.Drawing.Size(363, 24);
            this.decodedLabel.TabIndex = 3;
            this.decodedLabel.Text = "Исходный текст";
            this.decodedLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // encodedLabel
            // 
            this.encodedLabel.AutoSize = true;
            this.encodedLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodedLabel.Location = new System.Drawing.Point(417, 0);
            this.encodedLabel.Name = "encodedLabel";
            this.encodedLabel.Size = new System.Drawing.Size(364, 24);
            this.encodedLabel.TabIndex = 4;
            this.encodedLabel.Text = "Закодированный текст";
            this.encodedLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // decodedTableLayoutPanel
            // 
            this.decodedTableLayoutPanel.ColumnCount = 3;
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.Controls.Add(this.pasteToDecodedTextFromFileButton, 0, 0);
            this.decodedTableLayoutPanel.Controls.Add(this.showEncodedButton, 1, 0);
            this.decodedTableLayoutPanel.Controls.Add(this.decodedTextClearButton, 2, 0);
            this.decodedTableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedTableLayoutPanel.Location = new System.Drawing.Point(3, 306);
            this.decodedTableLayoutPanel.Name = "decodedTableLayoutPanel";
            this.decodedTableLayoutPanel.RowCount = 1;
            this.decodedTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.decodedTableLayoutPanel.Size = new System.Drawing.Size(363, 44);
            this.decodedTableLayoutPanel.TabIndex = 5;
            // 
            // pasteToDecodedTextFromFileButton
            // 
            this.pasteToDecodedTextFromFileButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pasteToDecodedTextFromFileButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.pasteToDecodedTextFromFileButton.Location = new System.Drawing.Point(3, 3);
            this.pasteToDecodedTextFromFileButton.Name = "pasteToDecodedTextFromFileButton";
            this.pasteToDecodedTextFromFileButton.Size = new System.Drawing.Size(115, 38);
            this.pasteToDecodedTextFromFileButton.TabIndex = 2;
            this.pasteToDecodedTextFromFileButton.Text = "Вставить из файла";
            this.pasteToDecodedTextFromFileButton.UseVisualStyleBackColor = true;
            this.pasteToDecodedTextFromFileButton.Click += new System.EventHandler(this.pasteToDecodedTextFromFileButton_Click);
            // 
            // showEncodedButton
            // 
            this.showEncodedButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.showEncodedButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.showEncodedButton.Location = new System.Drawing.Point(124, 3);
            this.showEncodedButton.Name = "showEncodedButton";
            this.showEncodedButton.Size = new System.Drawing.Size(115, 38);
            this.showEncodedButton.TabIndex = 3;
            this.showEncodedButton.Text = "Предпоказ кодировки";
            this.showEncodedButton.UseVisualStyleBackColor = true;
            this.showEncodedButton.Click += new System.EventHandler(this.showEncodedButton_Click);
            // 
            // decodedTextClearButton
            // 
            this.decodedTextClearButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedTextClearButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodedTextClearButton.Location = new System.Drawing.Point(245, 3);
            this.decodedTextClearButton.Name = "decodedTextClearButton";
            this.decodedTextClearButton.Size = new System.Drawing.Size(115, 38);
            this.decodedTextClearButton.TabIndex = 4;
            this.decodedTextClearButton.Text = "Очистить";
            this.decodedTextClearButton.UseVisualStyleBackColor = true;
            this.decodedTextClearButton.Click += new System.EventHandler(this.decodedTextClearButton_Click);
            // 
            // sequenceLabel
            // 
            this.sequenceLabel.AutoEllipsis = true;
            this.sequenceLabel.BackColor = System.Drawing.SystemColors.ControlLight;
            this.sequenceLabel.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.sequenceLabel.ForeColor = System.Drawing.SystemColors.ControlDarkDark;
            this.sequenceLabel.Location = new System.Drawing.Point(0, 0);
            this.sequenceLabel.Name = "sequenceLabel";
            this.sequenceLabel.Padding = new System.Windows.Forms.Padding(3, 0, 3, 0);
            this.sequenceLabel.Size = new System.Drawing.Size(784, 31);
            this.sequenceLabel.TabIndex = 0;
            this.sequenceLabel.Text = "пустой файл";
            this.sequenceLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // bottomPanel
            // 
            this.bottomPanel.BackColor = System.Drawing.SystemColors.Control;
            this.bottomPanel.Controls.Add(this.sequenceLabel);
            this.bottomPanel.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.bottomPanel.Location = new System.Drawing.Point(0, 380);
            this.bottomPanel.Name = "bottomPanel";
            this.bottomPanel.Size = new System.Drawing.Size(784, 31);
            this.bottomPanel.TabIndex = 2;
            // 
            // timer
            // 
            this.timer.Interval = 7000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // LZArchiver
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 411);
            this.Controls.Add(this.bottomPanel);
            this.Controls.Add(this.tableLayoutPanel);
            this.Controls.Add(this.menuStrip);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MainMenuStrip = this.menuStrip;
            this.MinimumSize = new System.Drawing.Size(600, 325);
            this.Name = "LZArchiver";
            this.Text = "Lempel-Ziv-Archiver";
            this.Load += new System.EventHandler(this.LZArchiver_Load);
            this.menuStrip.ResumeLayout(false);
            this.menuStrip.PerformLayout();
            this.tableLayoutPanel.ResumeLayout(false);
            this.tableLayoutPanel.PerformLayout();
            this.encodedTableLayoutPanel.ResumeLayout(false);
            this.codeButtonsPanel.Panel1.ResumeLayout(false);
            this.codeButtonsPanel.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.codeButtonsPanel)).EndInit();
            this.codeButtonsPanel.ResumeLayout(false);
            this.decodedTableLayoutPanel.ResumeLayout(false);
            this.bottomPanel.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel;
        private System.Windows.Forms.SplitContainer codeButtonsPanel;
        private System.Windows.Forms.Button encodeButton;
        private System.Windows.Forms.Button decodeButton;
        private System.Windows.Forms.TextBox encodedTextBox;
        private System.Windows.Forms.TextBox decodedTextBox;
        private System.Windows.Forms.Label decodedLabel;
        private System.Windows.Forms.Label encodedLabel;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveAsToolStripMenuItem;
        private System.Windows.Forms.ToolStripComboBox algorithmComboBox;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.Label sequenceLabel;
        private System.Windows.Forms.ToolStripMenuItem closeToolStripMenuItem;
        private System.Windows.Forms.Panel bottomPanel;
        private System.Windows.Forms.Button pasteToDecodedTextFromFileButton;
        private System.Windows.Forms.Button encodedTextClearButton;
        private System.Windows.Forms.Button showDecodedButton;
        private System.Windows.Forms.Button pasteToEncodedTextFromFileButton;
        private System.Windows.Forms.Button decodedTextClearButton;
        private System.Windows.Forms.Button showEncodedButton;
        private System.Windows.Forms.TableLayoutPanel encodedTableLayoutPanel;
        private System.Windows.Forms.TableLayoutPanel decodedTableLayoutPanel;
        private System.Windows.Forms.ToolStripMenuItem contentToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem deleteChangesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem settingsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem fontSizeToolStripMenuItem;
        private System.Windows.Forms.ToolStripComboBox fontSizeComboBoxToolStrip;
        private System.Windows.Forms.ToolStripMenuItem separatorToolStripMenuItem;
        private System.Windows.Forms.ToolStripComboBox separatorComboBoxToolStrip;
        private System.Windows.Forms.ToolStripMenuItem closeWithClearCheckBox;
        private System.Windows.Forms.ToolStripMenuItem saveDecodedTextToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveEncodedTextToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveAsDecodedTextToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem saveAsEncodedTextToolStripMenuItem;
        private System.Windows.Forms.Timer timer;
    }
}

