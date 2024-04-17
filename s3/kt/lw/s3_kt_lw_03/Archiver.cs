using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace s3_kt_lw_03
{
    public partial class Archiver : Form
    {
        public Archiver()
        {
            InitializeComponent();
        }
        private void readToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                openFileDialog.InitialDirectory = "C:\\Something";
                openFileDialog.Filter = "Бинарные файлы (*.dat)|*.dat";
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    using (BinaryReader reader = new BinaryReader(openFileDialog.OpenFile()))
                    {
                        textBox.Text = string.Empty;
                        while (reader.PeekChar() != -1)
                            textBox.Text += reader.ReadChar();
                    }
                }
            }
        }

        private void writeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            using (SaveFileDialog saveFileDialog = new SaveFileDialog())
            {
                saveFileDialog.Filter = "Бинарные файлы (*.dat)|*.dat";
                saveFileDialog.RestoreDirectory = true;

                if (saveFileDialog.ShowDialog() == DialogResult.OK)
                    using (BinaryWriter writer = new BinaryWriter(saveFileDialog.OpenFile()))
                        writer.Write(textBox.Text.ToCharArray());
            }
        }

        private void textBox_Enter(object sender, EventArgs e)
        {
            if (textBox.Text == "Здесь отображается записываемый текст и текст прочитанного файла.")
            {
                textBox.Text = string.Empty;
                textBox.ForeColor = Color.Black;
            }
        }

        private void textBox_Leave(object sender, EventArgs e)
        {
            if (textBox.Text == "")
            {
                textBox.Text = "Здесь отображается записываемый текст и текст прочитанного файла.";
                textBox.ForeColor = Color.DarkGray;
            }
            else
                textBox.ForeColor = Color.Black;
        }

        private void compressToolStripMenuItem_Click(object sender, EventArgs e)
            => textBox.Text = AlgorithmRLE.Encoding(textBox.Text);

        private void decompressToolStripMenuItem_Click(object sender, EventArgs e)
            => textBox.Text = AlgorithmRLE.Decoding(textBox.Text);
    }
}
