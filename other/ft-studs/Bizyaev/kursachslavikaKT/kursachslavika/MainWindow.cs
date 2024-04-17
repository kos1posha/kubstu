using System;
using System.IO;
using System.Windows.Forms;

namespace kursachslavika
{
    public partial class LZArchiver : Form
    {
        public string FilePath { get; set; } = string.Empty;
        public string FileContent => File.Exists(FilePath) ? File.ReadAllText(FilePath) : string.Empty;
        public char Separator => separatorComboBoxToolStrip.SelectedItem.ToString() == "Пробел" ? ' ': Convert.ToChar(separatorComboBoxToolStrip.SelectedItem);

        public LZArchiver()
        {
            InitializeComponent();
        }

        private void LZArchiver_Load(object sender, EventArgs e)
        {
            algorithmComboBox.SelectedIndex = 0;
            fontSizeComboBoxToolStrip.SelectedIndex = 1;
            separatorComboBoxToolStrip.SelectedIndex = 0;
        }

        private void decodeButton_Click(object sender, EventArgs e)
        {
            if (encodedTextBox.Text != string.Empty)
                try
                {
                    sequenceLabel.Text = "декодировка...";
                    switch (algorithmComboBox.SelectedIndex)
                    {
                        case 0:
                            decodedTextBox.Text = AlgorithmLZ77.Decode(encodedTextBox.Text, Separator);
                            break;
                        case 1:
                            decodedTextBox.Text = AlgorithmLZ78.Decode(encodedTextBox.Text, Separator);
                            break;
                    }
                    sequenceLabel.Text = "содержимое успешно декодировано";
                }
                catch
                {
                    sequenceLabel.Text = "ошибка декодировки\nвероятно строка имела неверный формат (убедитесь, что исходный текст не должен включать символ-разделитель)";
                }
        }
        private void encodeButton_Click(object sender, EventArgs e)
        {
            if (decodedTextBox.Text != string.Empty)
                try
                {

                    sequenceLabel.Text = "кодировка...";
                    switch (algorithmComboBox.SelectedIndex)
                    {
                        case 0:
                            encodedTextBox.Text = AlgorithmLZ77.Encode(decodedTextBox.Text, Separator).Result;
                            break;
                        case 1:
                            encodedTextBox.Text = AlgorithmLZ78.Encode(decodedTextBox.Text, Separator).Result;
                            break;
                    }
                    sequenceLabel.Text = "содержимое успешно закодировано";
                }
                catch
                {
                    sequenceLabel.Text = "ошибка кодировки";
                }
        }

        private void decodedTextClearButton_Click(object sender, EventArgs e)
        {
            decodedTextBox.Text = string.Empty;

            sequenceLabel.Text = "закодированный текст очищен";
        }
        private void encodedTextClearButton_Click(object sender, EventArgs e)
        {
            encodedTextBox.Text = string.Empty;

            sequenceLabel.Text = "декодированный текст очищен";
        }

        private void showDecodedButton_Click(object sender, EventArgs e)
        {
            if (encodedTextBox.Text != string.Empty)
                try
                {
                    switch (algorithmComboBox.SelectedIndex)
                    {
                        case 0:
                            MessageBox.Show(AlgorithmLZ77.Decode(encodedTextBox.Text, Separator), "Предпоказ декодировки");
                            break;
                        case 1:
                            MessageBox.Show(AlgorithmLZ78.Decode(encodedTextBox.Text, Separator), "Предпоказ декодировки");
                            break;
                    }
                }
                catch
                {
                    MessageBox.Show("ошибка декодировки\nвероятно строка имела неверный формат (убедитесь, что исходный текст не должен включать символ-разделитель)");
                }
        }
        private void showEncodedButton_Click(object sender, EventArgs e)
        {
            if (decodedTextBox.Text != string.Empty)
                try
                {
                    switch (algorithmComboBox.SelectedIndex)
                    {
                        case 0:
                            MessageBox.Show(AlgorithmLZ77.Encode(decodedTextBox.Text, Separator).Result, "Предпоказ кодировки");
                            break;
                        case 1:
                            MessageBox.Show(AlgorithmLZ78.Encode(decodedTextBox.Text, Separator).Result, "Предпоказ кодировки");
                            break;
                    }
                }
                catch
                {
                    MessageBox.Show("ошибка кодировки");
                }
        }

        private void fontSizeComboBoxToolStrip_SelectedIndexChanged(object sender, EventArgs e)
        {
            float fontSize = Convert.ToSingle(fontSizeComboBoxToolStrip.SelectedItem);
            encodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", fontSize);
            decodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", fontSize);
        }

        private void closeWithoutClearCheckBox_Click(object sender, EventArgs e)
        {
            if (closeWithClearCheckBox.Checked)
                closeWithClearCheckBox.Checked = false;
            else
                closeWithClearCheckBox.Checked = true;
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog fileDialog = new OpenFileDialog())
            {
                fileDialog.Filter = "Текстовые файлы (*.txt)|*.txt|Файлы dat (*.dat)|*.dat";
                fileDialog.ShowDialog();
                FilePath = fileDialog.FileName;
                decodedTextBox.Text = FileContent;
                sequenceLabel.Text = $"открыт файл {FilePath}";
            }
        }

        private void pasteToDecodedTextFromFileButton_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                decodedTextBox.Text = FileContent;
            sequenceLabel.Text = "содержимое файла скопированно в окно исходного текста";
        }

        private void pasteToEncodedTextFromFileButton_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                encodedTextBox.Text = FileContent;
            sequenceLabel.Text = "содержимое файла скопированно в окно закодированного текста";
        }

        private void closeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
            {
                sequenceLabel.Text = $"файл {FilePath} закрыт без сохранения";
                FilePath = string.Empty;
                if (closeWithClearCheckBox.Checked)
                {
                    decodedTextBox.Text = string.Empty;
                    encodedTextBox.Text = string.Empty;
                }
            }
        }

        private void contentToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                MessageBox.Show(FileContent, $"Содержимое файла {FilePath}");
        }

        private void deleteChangesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                encodedTextBox.Text = FileContent;
            sequenceLabel.Text = "изменения отменены";
        }

        private void saveDecodedTextToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (StreamWriter fileStream = new StreamWriter(FilePath, false))
            {
                fileStream.Write(decodedTextBox.Text);
                sequenceLabel.Text = $"исходный текст сохранен в файл {FilePath}";
            }
        }

        private void saveEncodedTextToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (StreamWriter fileStream = new StreamWriter(FilePath, false))
            {
                fileStream.Write(encodedTextBox.Text);
                sequenceLabel.Text = $"декодированный текст сохранен в файл {FilePath}";
            }
        }

        private void saveAsDecodedTextToolStripMenuItemToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog fileDialog = new SaveFileDialog())
            {
                fileDialog.Filter = "Текстовые файлы (*.txt)|*.txt|Файлы dat (*.dat)|*.dat";
                fileDialog.ShowDialog();

                FilePath = fileDialog.FileName;

                using (StreamWriter file = new StreamWriter(fileDialog.FileName))
                {
                    file.Write(decodedTextBox.Text);
                    sequenceLabel.Text = $"исходный текст сохранен в файл {FilePath}";
                }
            }
        }

        private void saveAsEncodedTextToolStripMenuItemToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog fileDialog = new SaveFileDialog())
            {
                fileDialog.Filter = "Текстовые файлы (*.txt)|*.txt|Файлы dat (*.dat)|*.dat";
                fileDialog.ShowDialog();

                FilePath = fileDialog.FileName;

                using (StreamWriter file = new StreamWriter(FilePath))
                {
                    file.Write(encodedTextBox.Text);
                    sequenceLabel.Text = $"закодированный текст сохранен в файл {FilePath}";
                }
            }
        }

        private void timer_Tick(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                sequenceLabel.Text = FilePath;
        }
    }
}
