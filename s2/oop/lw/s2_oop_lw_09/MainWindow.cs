using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Windows.Forms;

namespace s2_oop_lw_09
{
    public partial class MainWindow : Form
    {
        public List<EngVerb> initList = new List<EngVerb>()
        {
            new EngVerb("do", "did", "done"),
            new EngVerb("go", "went", "gone"),
            new EngVerb("split", "split", "split"),
            new EngVerb("know", "knew", "known"),
            new EngVerb("grow", "grew", "grown"),
            new EngVerb("burst", "burst", "burst")
        };
        public List<EngVerb> resultList = new List<EngVerb>();
        public BinaryFormatter binaryFormatter = new BinaryFormatter();
        public string serializePath = @"save\serialize.bin";
        public string commonPath = @"save\common.txt";

        public MainWindow()
        {
            InitializeComponent();
            for (int i = 0; i < initList.Count; i++)
            {
                enterListGridView.Rows.Add(initList[i].FirstForm, initList[i].SecondForm, initList[i].ThirdForm);
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            if (firstFormTextBox.Text.Trim() == "" || secondFormTextBox.Text.Trim() == "" || thirdFormTextBox.Text.Trim() == "")
            {
                MessageBox.Show("Пожалуйста, заполните все поля форм глаголов.");
            }
            else
            {
                int i = initList.Count;
                initList.Add(new EngVerb(firstFormTextBox.Text, secondFormTextBox.Text, thirdFormTextBox.Text));
                enterListGridView.Rows.Add(initList[i].FirstForm.Trim(), initList[i].SecondForm.Trim(), initList[i].ThirdForm.Trim());
            }
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            try
            {
                int i = enterListGridView.SelectedRows[0].Index;
                initList.RemoveAt(i);
                enterListGridView.Rows.Remove(enterListGridView.SelectedRows[0]);
            }
            catch
            {
                MessageBox.Show("Выберите строку исходного списка.");
            }

        }

        private void resultButton_Click(object sender, EventArgs e)
        {
            resultList.Clear();
            resultListGridView.Rows.Clear();
            for (int i = 0; i < initList.Count; i++)
            {
                if (initList[i].FirstForm == initList[i].SecondForm && initList[i].FirstForm == initList[i].ThirdForm)
                {
                    resultList.Add(initList[i]);
                }
            }
            resultList.Sort();
            for (int i = 0; i < resultList.Count; i++)
            {
                resultListGridView.Rows.Add(resultList[i].FirstForm, resultList[i].SecondForm, resultList[i].ThirdForm);
            }
        }
        private void clearEnterListButton_Click(object sender, EventArgs e)
        {
            enterListGridView.Rows.Clear();
        }
        private void clearResultListButton_Click(object sender, EventArgs e)
        {
            resultListGridView.Rows.Clear();
        }
        private void serializationSaveButton_Click(object sender, EventArgs e)
        {
            using (FileStream file = new FileStream(serializePath, FileMode.OpenOrCreate))
            {
                binaryFormatter.Serialize(file, initList);
            }
        }

        private void serializationLoadButton_Click(object sender, EventArgs e)
        {
            using (FileStream file = new FileStream(serializePath, FileMode.OpenOrCreate))
            {
                initList = binaryFormatter.Deserialize(file) as List<EngVerb>;
            }
            foreach (EngVerb item in initList)
            {
                enterListGridView.Rows.Add(item.FirstForm, item.SecondForm, item.ThirdForm);
            }
        }

        private void commonSaveButton_Click(object sender, EventArgs e)
        {
            using (StreamWriter writer = new StreamWriter(commonPath))
            {
                for (int i = 0; i < initList.Count; i++)
                {
                    writer.WriteLine(initList[i].ToString());
                }
            }
        }

        private void commonLoadButton_Click(object sender, EventArgs e)
        {
            using (StreamReader reader = new StreamReader(commonPath))
            {
                for (int i = 0; i < initList.Count; i++)
                {
                    initList[i] = new EngVerb(reader.ReadLine());
                }
            }
            foreach (EngVerb item in initList)
            {
                enterListGridView.Rows.Add(item.FirstForm, item.SecondForm, item.ThirdForm);
            }
        }
    }
}
