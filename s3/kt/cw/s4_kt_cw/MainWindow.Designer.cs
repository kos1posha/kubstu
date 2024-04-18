
namespace s3_kt_cw
{
    partial class SFCArchiver
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
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.openFileButton = new System.Windows.Forms.ToolStripMenuItem();
            this.closeFileButton = new System.Windows.Forms.ToolStripMenuItem();
            this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsDecodedTextFileButton = new System.Windows.Forms.ToolStripMenuItem();
            this.saveAsEncodedTextFileButton = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.fileContentButton = new System.Windows.Forms.ToolStripMenuItem();
            this.pasteFromFileButton = new System.Windows.Forms.ToolStripMenuItem();
            this.settingsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fontSizeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.fontSizeComboBox = new System.Windows.Forms.ToolStripComboBox();
            this.dividingWaysToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.partiallyCheckBox = new System.Windows.Forms.ToolStripMenuItem();
            this.fullCheckBox = new System.Windows.Forms.ToolStripMenuItem();
            this.infoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutSFCodeButton = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutDividingWaysButton = new System.Windows.Forms.ToolStripMenuItem();
            this.tableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.encodedTableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.showCodedAlphabetButton = new System.Windows.Forms.Button();
            this.decodeButton = new System.Windows.Forms.Button();
            this.showDecodedButton = new System.Windows.Forms.Button();
            this.encodedTextBox = new System.Windows.Forms.TextBox();
            this.decodedTextBox = new System.Windows.Forms.TextBox();
            this.decodedLabel = new System.Windows.Forms.Label();
            this.encodedLabel = new System.Windows.Forms.Label();
            this.decodedTableLayoutPanel = new System.Windows.Forms.TableLayoutPanel();
            this.clearButton = new System.Windows.Forms.Button();
            this.encodeButton = new System.Windows.Forms.Button();
            this.showEncodedButton = new System.Windows.Forms.Button();
            this.sequenceLabel = new System.Windows.Forms.Label();
            this.bottomPanel = new System.Windows.Forms.Panel();
            this.timer = new System.Windows.Forms.Timer(this.components);
            this.binViewCheckBox = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip.SuspendLayout();
            this.tableLayoutPanel.SuspendLayout();
            this.encodedTableLayoutPanel.SuspendLayout();
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
            this.settingsToolStripMenuItem,
            this.infoToolStripMenuItem});
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Size = new System.Drawing.Size(874, 24);
            this.menuStrip.TabIndex = 0;
            this.menuStrip.Text = "menuStrip";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.openFileButton,
            this.closeFileButton,
            this.saveToolStripMenuItem,
            this.saveAsToolStripMenuItem,
            this.toolStripSeparator1,
            this.fileContentButton,
            this.pasteFromFileButton});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(48, 20);
            this.fileToolStripMenuItem.Text = "Файл";
            // 
            // openFileButton
            // 
            this.openFileButton.Name = "openFileButton";
            this.openFileButton.Size = new System.Drawing.Size(175, 22);
            this.openFileButton.Text = "Открыть";
            this.openFileButton.Click += new System.EventHandler(this.openToolStripMenuItem_Click);
            // 
            // closeFileButton
            // 
            this.closeFileButton.Name = "closeFileButton";
            this.closeFileButton.Size = new System.Drawing.Size(175, 22);
            this.closeFileButton.Text = "Закрыть";
            this.closeFileButton.Click += new System.EventHandler(this.closeFileButton_Click);
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            this.saveToolStripMenuItem.Size = new System.Drawing.Size(175, 22);
            this.saveToolStripMenuItem.Text = "Сохранить";
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.saveToolStripMenuItem_Click);
            // 
            // saveAsToolStripMenuItem
            // 
            this.saveAsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.saveAsDecodedTextFileButton,
            this.saveAsEncodedTextFileButton});
            this.saveAsToolStripMenuItem.Name = "saveAsToolStripMenuItem";
            this.saveAsToolStripMenuItem.Size = new System.Drawing.Size(175, 22);
            this.saveAsToolStripMenuItem.Text = "Сохранить как";
            // 
            // saveAsDecodedTextFileButton
            // 
            this.saveAsDecodedTextFileButton.Name = "saveAsDecodedTextFileButton";
            this.saveAsDecodedTextFileButton.Size = new System.Drawing.Size(200, 22);
            this.saveAsDecodedTextFileButton.Text = "Исходный текст";
            this.saveAsDecodedTextFileButton.Click += new System.EventHandler(this.saveAsDecodedTextToolStripMenuItemToolStripMenuItem_Click);
            // 
            // saveAsEncodedTextFileButton
            // 
            this.saveAsEncodedTextFileButton.Name = "saveAsEncodedTextFileButton";
            this.saveAsEncodedTextFileButton.Size = new System.Drawing.Size(200, 22);
            this.saveAsEncodedTextFileButton.Text = "Закодированный текст";
            this.saveAsEncodedTextFileButton.Click += new System.EventHandler(this.saveAsEncodedTextToolStripMenuItemToolStripMenuItem_Click);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            this.toolStripSeparator1.Size = new System.Drawing.Size(172, 6);
            // 
            // fileContentButton
            // 
            this.fileContentButton.Name = "fileContentButton";
            this.fileContentButton.Size = new System.Drawing.Size(175, 22);
            this.fileContentButton.Text = "Содержимое";
            this.fileContentButton.Click += new System.EventHandler(this.contentToolStripMenuItem_Click);
            // 
            // pasteFromFileButton
            // 
            this.pasteFromFileButton.Name = "pasteFromFileButton";
            this.pasteFromFileButton.Size = new System.Drawing.Size(175, 22);
            this.pasteFromFileButton.Text = "Вставить из файла";
            this.pasteFromFileButton.Click += new System.EventHandler(this.pasteFromFileButton_Click);
            // 
            // settingsToolStripMenuItem
            // 
            this.settingsToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fontSizeToolStripMenuItem,
            this.dividingWaysToolStripMenuItem,
            this.binViewCheckBox});
            this.settingsToolStripMenuItem.Name = "settingsToolStripMenuItem";
            this.settingsToolStripMenuItem.Size = new System.Drawing.Size(79, 20);
            this.settingsToolStripMenuItem.Text = "Настройки";
            // 
            // fontSizeToolStripMenuItem
            // 
            this.fontSizeToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fontSizeComboBox});
            this.fontSizeToolStripMenuItem.Name = "fontSizeToolStripMenuItem";
            this.fontSizeToolStripMenuItem.Size = new System.Drawing.Size(244, 22);
            this.fontSizeToolStripMenuItem.Text = "Размер шрифта";
            // 
            // fontSizeComboBox
            // 
            this.fontSizeComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.fontSizeComboBox.DropDownWidth = 75;
            this.fontSizeComboBox.Items.AddRange(new object[] {
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
            "48"});
            this.fontSizeComboBox.Name = "fontSizeComboBox";
            this.fontSizeComboBox.Size = new System.Drawing.Size(75, 23);
            this.fontSizeComboBox.SelectedIndexChanged += new System.EventHandler(this.fontSizeComboBoxToolStrip_SelectedIndexChanged);
            // 
            // dividingWaysToolStripMenuItem
            // 
            this.dividingWaysToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.partiallyCheckBox,
            this.fullCheckBox});
            this.dividingWaysToolStripMenuItem.Name = "dividingWaysToolStripMenuItem";
            this.dividingWaysToolStripMenuItem.Size = new System.Drawing.Size(244, 22);
            this.dividingWaysToolStripMenuItem.Text = "Способ деления на подгруппы";
            // 
            // partiallyCheckBox
            // 
            this.partiallyCheckBox.Checked = true;
            this.partiallyCheckBox.CheckState = System.Windows.Forms.CheckState.Checked;
            this.partiallyCheckBox.Name = "partiallyCheckBox";
            this.partiallyCheckBox.Size = new System.Drawing.Size(188, 22);
            this.partiallyCheckBox.Text = "Полный сдвиг влево";
            this.partiallyCheckBox.Click += new System.EventHandler(this.partiallyCheckBox_Click);
            // 
            // fullCheckBox
            // 
            this.fullCheckBox.Name = "fullCheckBox";
            this.fullCheckBox.Size = new System.Drawing.Size(188, 22);
            this.fullCheckBox.Text = "Дозаполнение краев";
            this.fullCheckBox.Click += new System.EventHandler(this.fullCheckBox_Click);
            // 
            // infoToolStripMenuItem
            // 
            this.infoToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutSFCodeButton,
            this.aboutDividingWaysButton});
            this.infoToolStripMenuItem.Name = "infoToolStripMenuItem";
            this.infoToolStripMenuItem.Size = new System.Drawing.Size(65, 20);
            this.infoToolStripMenuItem.Text = "Справка";
            // 
            // aboutSFCodeButton
            // 
            this.aboutSFCodeButton.Name = "aboutSFCodeButton";
            this.aboutSFCodeButton.Size = new System.Drawing.Size(240, 22);
            this.aboutSFCodeButton.Text = "Об алгоритме Шеннона-Фано";
            this.aboutSFCodeButton.Click += new System.EventHandler(this.aboutSFCodeButton_Click);
            // 
            // aboutDividingWaysButton
            // 
            this.aboutDividingWaysButton.Name = "aboutDividingWaysButton";
            this.aboutDividingWaysButton.Size = new System.Drawing.Size(240, 22);
            this.aboutDividingWaysButton.Text = "О делении на подгруппы";
            this.aboutDividingWaysButton.Click += new System.EventHandler(this.aboutDividingWaysButton_Click);
            // 
            // tableLayoutPanel
            // 
            this.tableLayoutPanel.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.tableLayoutPanel.BackColor = System.Drawing.SystemColors.Control;
            this.tableLayoutPanel.ColumnCount = 2;
            this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 50F));
            this.tableLayoutPanel.Controls.Add(this.encodedTableLayoutPanel, 1, 2);
            this.tableLayoutPanel.Controls.Add(this.encodedTextBox, 1, 1);
            this.tableLayoutPanel.Controls.Add(this.decodedTextBox, 0, 1);
            this.tableLayoutPanel.Controls.Add(this.decodedLabel, 0, 0);
            this.tableLayoutPanel.Controls.Add(this.encodedLabel, 1, 0);
            this.tableLayoutPanel.Controls.Add(this.decodedTableLayoutPanel, 0, 2);
            this.tableLayoutPanel.Location = new System.Drawing.Point(0, 27);
            this.tableLayoutPanel.Margin = new System.Windows.Forms.Padding(0, 3, 0, 0);
            this.tableLayoutPanel.Name = "tableLayoutPanel";
            this.tableLayoutPanel.RowCount = 3;
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 24F));
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 50F));
            this.tableLayoutPanel.Size = new System.Drawing.Size(874, 422);
            this.tableLayoutPanel.TabIndex = 1;
            // 
            // encodedTableLayoutPanel
            // 
            this.encodedTableLayoutPanel.ColumnCount = 3;
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.encodedTableLayoutPanel.Controls.Add(this.showCodedAlphabetButton, 0, 0);
            this.encodedTableLayoutPanel.Controls.Add(this.decodeButton, 0, 0);
            this.encodedTableLayoutPanel.Controls.Add(this.showDecodedButton, 1, 0);
            this.encodedTableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedTableLayoutPanel.Location = new System.Drawing.Point(440, 375);
            this.encodedTableLayoutPanel.Name = "encodedTableLayoutPanel";
            this.encodedTableLayoutPanel.RowCount = 1;
            this.encodedTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.encodedTableLayoutPanel.Size = new System.Drawing.Size(431, 44);
            this.encodedTableLayoutPanel.TabIndex = 8;
            // 
            // showCodedAlphabetButton
            // 
            this.showCodedAlphabetButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.showCodedAlphabetButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.showCodedAlphabetButton.Location = new System.Drawing.Point(146, 3);
            this.showCodedAlphabetButton.Name = "showCodedAlphabetButton";
            this.showCodedAlphabetButton.Size = new System.Drawing.Size(137, 38);
            this.showCodedAlphabetButton.TabIndex = 10;
            this.showCodedAlphabetButton.Text = "Просмотреть алфавит";
            this.showCodedAlphabetButton.UseVisualStyleBackColor = true;
            this.showCodedAlphabetButton.Click += new System.EventHandler(this.showEncodedAlphabetButton_Click);
            // 
            // decodeButton
            // 
            this.decodeButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodeButton.Location = new System.Drawing.Point(3, 3);
            this.decodeButton.Name = "decodeButton";
            this.decodeButton.Size = new System.Drawing.Size(137, 38);
            this.decodeButton.TabIndex = 9;
            this.decodeButton.Text = "Распаковать";
            this.decodeButton.UseVisualStyleBackColor = true;
            this.decodeButton.Click += new System.EventHandler(this.decodeButton_Click);
            // 
            // showDecodedButton
            // 
            this.showDecodedButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.showDecodedButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.showDecodedButton.Location = new System.Drawing.Point(289, 3);
            this.showDecodedButton.Name = "showDecodedButton";
            this.showDecodedButton.Size = new System.Drawing.Size(139, 38);
            this.showDecodedButton.TabIndex = 7;
            this.showDecodedButton.Text = "Предпоказ распаковки\r\n";
            this.showDecodedButton.UseVisualStyleBackColor = true;
            this.showDecodedButton.Click += new System.EventHandler(this.showDecodedButton_Click);
            // 
            // encodedTextBox
            // 
            this.encodedTextBox.BackColor = System.Drawing.SystemColors.Window;
            this.encodedTextBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodedTextBox.Location = new System.Drawing.Point(440, 27);
            this.encodedTextBox.Multiline = true;
            this.encodedTextBox.Name = "encodedTextBox";
            this.encodedTextBox.ReadOnly = true;
            this.encodedTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.encodedTextBox.Size = new System.Drawing.Size(431, 342);
            this.encodedTextBox.TabIndex = 2;
            this.encodedTextBox.TextChanged += new System.EventHandler(this.encodedTextBox_TextChanged);
            this.encodedTextBox.Enter += new System.EventHandler(this.encodedTextBox_Enter);
            // 
            // decodedTextBox
            // 
            this.decodedTextBox.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodedTextBox.Location = new System.Drawing.Point(3, 27);
            this.decodedTextBox.Multiline = true;
            this.decodedTextBox.Name = "decodedTextBox";
            this.decodedTextBox.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.decodedTextBox.Size = new System.Drawing.Size(431, 342);
            this.decodedTextBox.TabIndex = 1;
            this.decodedTextBox.Click += new System.EventHandler(this.decodedTextBox_Click);
            this.decodedTextBox.TextChanged += new System.EventHandler(this.decodedTextBox_TextChanged);
            this.decodedTextBox.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.decodedTextBox_KeyPress);
            // 
            // decodedLabel
            // 
            this.decodedLabel.AutoSize = true;
            this.decodedLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.decodedLabel.Location = new System.Drawing.Point(3, 0);
            this.decodedLabel.Name = "decodedLabel";
            this.decodedLabel.Size = new System.Drawing.Size(431, 24);
            this.decodedLabel.TabIndex = 3;
            this.decodedLabel.Text = "Исходный текст (0 симв.)";
            this.decodedLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // encodedLabel
            // 
            this.encodedLabel.AutoEllipsis = true;
            this.encodedLabel.AutoSize = true;
            this.encodedLabel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodedLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodedLabel.Location = new System.Drawing.Point(440, 0);
            this.encodedLabel.Name = "encodedLabel";
            this.encodedLabel.Size = new System.Drawing.Size(431, 24);
            this.encodedLabel.TabIndex = 4;
            this.encodedLabel.Text = "Сжатая последовательность (0 симв.)";
            this.encodedLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // decodedTableLayoutPanel
            // 
            this.decodedTableLayoutPanel.ColumnCount = 3;
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 33.33333F));
            this.decodedTableLayoutPanel.Controls.Add(this.clearButton, 0, 0);
            this.decodedTableLayoutPanel.Controls.Add(this.encodeButton, 0, 0);
            this.decodedTableLayoutPanel.Controls.Add(this.showEncodedButton, 1, 0);
            this.decodedTableLayoutPanel.Dock = System.Windows.Forms.DockStyle.Fill;
            this.decodedTableLayoutPanel.Location = new System.Drawing.Point(3, 375);
            this.decodedTableLayoutPanel.Name = "decodedTableLayoutPanel";
            this.decodedTableLayoutPanel.RowCount = 1;
            this.decodedTableLayoutPanel.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.decodedTableLayoutPanel.Size = new System.Drawing.Size(431, 44);
            this.decodedTableLayoutPanel.TabIndex = 5;
            // 
            // clearButton
            // 
            this.clearButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.clearButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.clearButton.Location = new System.Drawing.Point(146, 3);
            this.clearButton.Name = "clearButton";
            this.clearButton.Size = new System.Drawing.Size(137, 38);
            this.clearButton.TabIndex = 5;
            this.clearButton.Text = "Очистить";
            this.clearButton.UseVisualStyleBackColor = true;
            this.clearButton.Click += new System.EventHandler(this.clearButton_Click);
            // 
            // encodeButton
            // 
            this.encodeButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.encodeButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.encodeButton.Location = new System.Drawing.Point(3, 3);
            this.encodeButton.Name = "encodeButton";
            this.encodeButton.Size = new System.Drawing.Size(137, 38);
            this.encodeButton.TabIndex = 4;
            this.encodeButton.Text = "Сжать";
            this.encodeButton.UseVisualStyleBackColor = true;
            this.encodeButton.Click += new System.EventHandler(this.encodeButton_Click);
            // 
            // showEncodedButton
            // 
            this.showEncodedButton.Dock = System.Windows.Forms.DockStyle.Fill;
            this.showEncodedButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(204)));
            this.showEncodedButton.Location = new System.Drawing.Point(289, 3);
            this.showEncodedButton.Name = "showEncodedButton";
            this.showEncodedButton.Size = new System.Drawing.Size(139, 38);
            this.showEncodedButton.TabIndex = 3;
            this.showEncodedButton.Text = "Предпоказ сжатия";
            this.showEncodedButton.UseVisualStyleBackColor = true;
            this.showEncodedButton.Click += new System.EventHandler(this.showEncodedButton_Click);
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
            this.sequenceLabel.Size = new System.Drawing.Size(874, 31);
            this.sequenceLabel.TabIndex = 0;
            this.sequenceLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
            // 
            // bottomPanel
            // 
            this.bottomPanel.BackColor = System.Drawing.SystemColors.Control;
            this.bottomPanel.Controls.Add(this.sequenceLabel);
            this.bottomPanel.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.bottomPanel.Location = new System.Drawing.Point(0, 449);
            this.bottomPanel.Name = "bottomPanel";
            this.bottomPanel.Size = new System.Drawing.Size(874, 31);
            this.bottomPanel.TabIndex = 2;
            // 
            // timer
            // 
            this.timer.Interval = 7000;
            this.timer.Tick += new System.EventHandler(this.timer_Tick);
            // 
            // binViewCheckBox
            // 
            this.binViewCheckBox.Name = "binViewCheckBox";
            this.binViewCheckBox.Size = new System.Drawing.Size(244, 22);
            this.binViewCheckBox.Text = "Двоичное представление";
            this.binViewCheckBox.Click += new System.EventHandler(this.binViewCheckBox_CheckedChanged);
            // 
            // SFCArchiver
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(874, 480);
            this.Controls.Add(this.bottomPanel);
            this.Controls.Add(this.tableLayoutPanel);
            this.Controls.Add(this.menuStrip);
            this.MainMenuStrip = this.menuStrip;
            this.MinimumSize = new System.Drawing.Size(640, 270);
            this.Name = "SFCArchiver";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "пустой файл";
            this.Load += new System.EventHandler(this.LZArchiver_Load);
            this.menuStrip.ResumeLayout(false);
            this.menuStrip.PerformLayout();
            this.tableLayoutPanel.ResumeLayout(false);
            this.tableLayoutPanel.PerformLayout();
            this.encodedTableLayoutPanel.ResumeLayout(false);
            this.decodedTableLayoutPanel.ResumeLayout(false);
            this.bottomPanel.ResumeLayout(false);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel;
        private System.Windows.Forms.TextBox encodedTextBox;
        private System.Windows.Forms.TextBox decodedTextBox;
        private System.Windows.Forms.Label decodedLabel;
        private System.Windows.Forms.Label encodedLabel;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem openFileButton;
        private System.Windows.Forms.ToolStripMenuItem saveAsToolStripMenuItem;
        private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
        private System.Windows.Forms.Label sequenceLabel;
        private System.Windows.Forms.ToolStripMenuItem closeFileButton;
        private System.Windows.Forms.Panel bottomPanel;
        private System.Windows.Forms.TableLayoutPanel encodedTableLayoutPanel;
        private System.Windows.Forms.TableLayoutPanel decodedTableLayoutPanel;
        private System.Windows.Forms.ToolStripMenuItem fileContentButton;
        private System.Windows.Forms.ToolStripMenuItem settingsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem fontSizeToolStripMenuItem;
        private System.Windows.Forms.ToolStripComboBox fontSizeComboBox;
        private System.Windows.Forms.ToolStripMenuItem saveAsDecodedTextFileButton;
        private System.Windows.Forms.ToolStripMenuItem saveAsEncodedTextFileButton;
        private System.Windows.Forms.Timer timer;
        private System.Windows.Forms.ToolStripMenuItem infoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutSFCodeButton;
        private System.Windows.Forms.ToolStripMenuItem aboutDividingWaysButton;
        private System.Windows.Forms.ToolStripMenuItem dividingWaysToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem partiallyCheckBox;
        private System.Windows.Forms.ToolStripMenuItem fullCheckBox;
        private System.Windows.Forms.Button showDecodedButton;
        private System.Windows.Forms.Button showEncodedButton;
        private System.Windows.Forms.Button showCodedAlphabetButton;
        private System.Windows.Forms.Button decodeButton;
        private System.Windows.Forms.Button clearButton;
        private System.Windows.Forms.Button encodeButton;
        private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem pasteFromFileButton;
        private System.Windows.Forms.ToolStripMenuItem binViewCheckBox;
    }
}

