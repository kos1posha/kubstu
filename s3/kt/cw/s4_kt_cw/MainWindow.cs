using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace s3_kt_cw
{
    public partial class SFCArchiver : Form
    {
        int[] decodedBytes;

        public string FilePath { get; set; } = string.Empty;
        public string FileContent => File.Exists(FilePath) ? File.ReadAllText(FilePath) : string.Empty;
        public SplitPrinciple SplitPrinciple = SplitPrinciple.Partially;

        public SFCArchiver()
        {
            InitializeComponent();
        }
        private void LZArchiver_Load(object sender, EventArgs e)
        {
            fontSizeComboBox.SelectedIndex = 1;
        }

        public static (int[] Array, string String) ToBytes(string text)
        {
            List<int> bytes = new List<int>();
            string result = string.Empty;

            foreach (char symbol in text)
                bytes.Add(symbol);

            foreach (int symbol in bytes)
                result += Convert.ToString(symbol, 2);

            return (bytes.ToArray(), result);
        }
        public static string EncodeTo(int[] bytes)
        {
            string result = string.Empty;

            foreach (int symbol in bytes)
                result += (char)symbol;

            return result;
        }

        private void fontSizeComboBoxToolStrip_SelectedIndexChanged(object sender, EventArgs e)
        {
            float fontSize = Convert.ToSingle(fontSizeComboBox.SelectedItem);
            encodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", fontSize);
            decodedTextBox.Font = new System.Drawing.Font("Microsoft Sans Serif", fontSize);
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog fileDialog = new OpenFileDialog())
            {
                fileDialog.Filter = "Текстовые файлы (*.txt)|*.txt|Файлы sfc (*.sfc)|*.sfc";
                fileDialog.ShowDialog();
                if (fileDialog.FileName != string.Empty)
                {
                    FilePath = fileDialog.FileName;
                    if (FilePath.Substring(FilePath.Length - 4) == ".txt")
                        decodedTextBox.Text = FileContent;
                    else
                        encodedTextBox.Text = FileContent;
                    sequenceLabel.Text = $"открыт файл {FilePath}";
                    Text = FilePath;
                }
            }
        }

        private void contentToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                MessageBox.Show(FileContent, $"Содержимое файла {FilePath}");
            else
                sequenceLabel.Text = "пустой файл";
        }

        private void saveDecodedTextToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (StreamWriter fileStream = new StreamWriter(FilePath, false))
            {
                fileStream.Write(decodedTextBox.Text);
                sequenceLabel.Text = $"исходный текст сохранен в файл {FilePath}";
            }
        }

        private void saveAsDecodedTextToolStripMenuItemToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog fileDialog = new SaveFileDialog())
            {
                fileDialog.Filter = "Текстовые файлы (*.txt)|*.txt";
                fileDialog.ShowDialog();

                FilePath = fileDialog.FileName;

                if (fileDialog.FileName != string.Empty)
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
                fileDialog.Filter = "Файлы sfc (*.sfc)|*.sfc";
                fileDialog.ShowDialog();

                FilePath = fileDialog.FileName;

                if (fileDialog.FileName != string.Empty)
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

        private void encodedTextBox_Enter(object sender, EventArgs e)
        {
            decodedTextBox.Focus();
        }

        private void binViewCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            if (!binViewCheckBox.Checked)
            {
                binViewCheckBox.Checked = true;
                (decodedBytes, decodedTextBox.Text) = ToBytes(decodedTextBox.Text);
                decodedTextBox.ReadOnly = true;
            }
            else
            {
                binViewCheckBox.Checked = false;
                decodedTextBox.Text = EncodeTo(decodedBytes);
                decodedTextBox.ReadOnly = false;
            }
        }

        private void encodeButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (decodedTextBox.Text.Length != 0)
                {
                    Stopwatch stopwatch = new Stopwatch();
                    stopwatch.Start();
                    encodedTextBox.Text = SFAlgorithm.Encode(binViewCheckBox.Checked ? EncodeTo(decodedBytes) : decodedTextBox.Text, SplitPrinciple);
                    stopwatch.Stop();
                    sequenceLabel.Text = $"исходный текст успешно сжат\nK = {(decimal)(binViewCheckBox.Checked ? decodedTextBox.Text : ToBytes(decodedTextBox.Text).String).Length / encodedTextBox.Text.Length:F5}, t = {stopwatch.ElapsedMilliseconds} мс";
                }
                else
                {
                    sequenceLabel.Text = $"исходный текст пуст";
                }
            }
            catch
            {
                sequenceLabel.Text = "во время сжатия произошла ошибка";
            }
        }

        private void decodeButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (encodedTextBox.Text.Length != 0)
                {
                    Stopwatch stopwatch = new Stopwatch();
                    stopwatch.Start();
                    decodedTextBox.Text = SFAlgorithm.Decode(encodedTextBox.Text);
                    stopwatch.Stop();
                    sequenceLabel.Text = $"закодированный текст успешно распакован\nt = {stopwatch.ElapsedMilliseconds} мс";
                }
                else
                    sequenceLabel.Text = $"закодированный текст пуст";
            }
            catch
            {
                sequenceLabel.Text = "во время распаковки произошла ошибка";
            }
        }

        private void decodedTextBox_TextChanged(object sender, EventArgs e)
        {
            decodedLabel.Text = $"Исходный текст ({decodedTextBox.Text.Length} симв.)";
        }

        private void encodedTextBox_TextChanged(object sender, EventArgs e)
        {
            encodedLabel.Text = $"Сжатая последовательность ({encodedTextBox.Text.Length} симв.)";
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                using (StreamWriter file = new StreamWriter(FilePath))
                {
                    if (FilePath.Contains(".txt"))
                    {
                        file.Write(decodedTextBox.Text);
                        sequenceLabel.Text = $"исходный текст сохранен в файл {FilePath}";
                    }
                    else if (FilePath.Contains(".sfc"))
                    {
                        file.Write(encodedTextBox.Text);
                        sequenceLabel.Text = $"закодированный текст сохранен в файл {FilePath}";
                    }
                }
            else
                sequenceLabel.Text = "пустой файл";
        }


        private void saveAsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void partiallyCheckBox_Click(object sender, EventArgs e)
        {
            if (!partiallyCheckBox.Checked)
            {
                partiallyCheckBox.Checked = true;
                fullCheckBox.Checked = false;
                SplitPrinciple = SplitPrinciple.Partially;
            }
        }

        private void fullCheckBox_Click(object sender, EventArgs e)
        {
            if (!fullCheckBox.Checked)
            {
                partiallyCheckBox.Checked = false;
                fullCheckBox.Checked = true;
                SplitPrinciple = SplitPrinciple.Full;
            }
        }

        private void closeFileButton_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
            {
                sequenceLabel.Text = $"файл {FilePath} закрыт";
                FilePath = string.Empty;
                Text = "пустой файл";
                decodedTextBox.Text = string.Empty;
                encodedTextBox.Text = string.Empty;
            }
            else
                sequenceLabel.Text = $"пустой файл";
        }

        private void decodedTextBox_KeyPress(object sender, KeyPressEventArgs e)
        {
            sequenceLabel.Text = e.KeyChar.ToString();
        }

        private void decodedTextBox_Click(object sender, EventArgs e)
        {
            sequenceLabel.Text = $"{decodedTextBox.Text.Length} символов";
        }

        private void showEncodedAlphabetButton_Click(object sender, EventArgs e)
        {
            try
            {
                Dictionary<string, char> codedAlphabet = SFAlgorithm.GetCodedAlphabet(encodedTextBox.Text);
                string message = string.Empty;

                int space = 1;
                foreach (KeyValuePair<string, char> node in codedAlphabet)
                    message += $"{node.Value} - {node.Key}{(space++ % 3 == 0 ? "\n" : "\t\t")}";

                if (message != string.Empty)
                    MessageBox.Show(message, $"Всего элементов: {codedAlphabet.Values.Count}");
                else
                    sequenceLabel.Text = "закодированный текст пуст";
            }
            catch
            {
                sequenceLabel.Text = "алфавит не найден";
            }
        }

        private void pasteFromFileButton_Click(object sender, EventArgs e)
        {
            if (FilePath != string.Empty)
                if (FilePath.Substring(FilePath.Length - 4) == ".txt")
                    decodedTextBox.Text = FileContent;
                else
                    encodedTextBox.Text = FileContent;
            else
                sequenceLabel.Text = $"пустой файл";
        }

        private void showEncodedButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (decodedTextBox.Text.Length != 0)
                {
                    Stopwatch stopwatch = new Stopwatch();
                    stopwatch.Start();
                    string message = SFAlgorithm.Encode(decodedTextBox.Text, SplitPrinciple);
                    stopwatch.Stop();
                    MessageBox.Show($"K = {(decimal)ToBytes(decodedTextBox.Text).String.Length / message.Length:F5}, t = {stopwatch.ElapsedMilliseconds} мс\n\n{message}", $"исходный текст успешно сжат ({message.Length} симв.)");
                }
                else
                    sequenceLabel.Text = $"исходный текст пуст";
            }
            catch
            {
                sequenceLabel.Text = "во время сжатия произошла ошибка";
            }
        }

        private void showDecodedButton_Click(object sender, EventArgs e)
        {
            try
            {
                if (encodedTextBox.Text.Length != 0)
                {
                    Stopwatch stopwatch = new Stopwatch();
                    stopwatch.Start();
                    string message = SFAlgorithm.Decode(encodedTextBox.Text);
                    stopwatch.Stop();
                    MessageBox.Show($"t = {stopwatch.ElapsedMilliseconds} мс\n\n{message}", $"закодированный текст успешно распакован ({message.Length} симв.)");
                }
                else
                    sequenceLabel.Text = $"закодированный текст пуст";
            }
            catch
            {
                sequenceLabel.Text = "во время распаковки произошла ошибка";
            }
        }

        private void clearButton_Click(object sender, EventArgs e)
        {
            decodedTextBox.Text = string.Empty;
            decodedBytes = new int[0];
            sequenceLabel.Text = "исходный текст очищен";
        }

        private void aboutSFCodeButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Код Шеннона-Фано строится с помощью дерева. Построение этого дерева начинается от корня. Всё множество кодируемых элементов соответствует корню дерева (вершине первого уровня). Оно разбивается на два подмножества с примерно одинаковыми суммарными вероятностями. Эти подмножества соответствуют двум вершинам второго уровня, которые соединяются с корнем. Далее каждое из этих подмножеств разбивается на два подмножества с примерно одинаковыми суммарными вероятностями. Им соответствуют вершины третьего уровня. Если подмножество содержит единственный элемент, то ему соответствует концевая вершина кодового дерева; такое подмножество разбиению не подлежит. Подобным образом поступаем до тех пор, пока не получим все концевые вершины. Ветви кодового дерева размечаем символами 1 и 0, как в случае кода Хаффмана. При построении кода Шеннона - Фано разбиение множества элементов может быть произведено, вообще говоря, несколькими способами.Выбор разбиения на уровне n может ухудшить варианты разбиения на следующем уровне(n + 1) и привести к не оптимальности кода в целом.Другими словами, оптимальное поведение на каждом шаге пути ещё не гарантирует оптимальности всей совокупности действий.Поэтому код Шеннона - Фано не является оптимальным в общем смысле, хотя и дает оптимальные результаты при некоторых распределениях вероятностей.Для одного и того же распределения вероятностей можно построить, вообще говоря, несколько кодов Шеннона - Фано, и все они могут дать различные результаты.Если построить все возможные коды Шеннона - Фано для данного распределения вероятностей, то среди них будут находиться и все коды Хаффмана, то есть оптимальные коды.", "Об алгоритме Шеннона-Фано");
        }

        private void aboutDividingWaysButton_Click(object sender, EventArgs e)
        {
            MessageBox.Show("В программе реализовано 2 метода деления групп символов на равновероятные подргруппы: полный сдвиг влево и дозаполнение краев.\nПолный сдвиг влево заполняет левую подгруппу элементами из делимой группы до тех пор, пока общая вероятность элементов левой подгруппы не перевалит за половину общей вероятности элементов делимой группы. После этого оставшиеся элементы заносятся в правую подгруппу. Из-за того что список элементов отсортирован по убываю вероятности, элементы с большей вероятносью, добавляющиеся первыми, группируются в относительно небольшие подгруппы, обеспечивая им более короткий код.\nДозаполнение краев по очереди добавляет элементы в левую и правую подгруппы, причем сторона, в которую кладутся элементы, меняется каждый раз, когда общая вероятность элементов текущей подгруппы не перевалит за общую вероятность элементов другой. В этом варианте подгруппы имеют примерно одинаковое количество элементов.", "О делении на подгруппы");
        }
    }
}
