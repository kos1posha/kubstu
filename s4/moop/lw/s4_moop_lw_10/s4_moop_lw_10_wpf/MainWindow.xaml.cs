using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows;
using System.Windows.Controls;
using s4_moop_lw_10;
using Action = s4_moop_lw_10.Action;

namespace s4_moop_lw_10_wpf
{
    public partial class MainWindow : Window
    {
        readonly Human human = new Human();
        readonly Cat cat = new Cat();
        readonly Dog dog = new Dog();
        readonly Carrot carrot = new Carrot();

        Action[] actions = {
            Action.Nothing, Action.Sleep, Action.Shit, Action.Eat, Action.Smoke, Action.ShakesPlasticBag,
            Action.SaysPussPussPuss, Action.SaysWhoIsGoodBoy, Action.SaysBadWords,
            Action.CleansCatLitterBox, Action.CleansDogSheet, Action.CleansParrotCell,
            Action.PutOnCatFood,Action.PutOnDogFood, Action.PutOnCarrotFood,
            Action.PlaysOnPiano, Action.PlaysOnGuitar
        };

        Location[] locations = {
            Location.Bedroom, Location.Kitchen, Location.Bathroom, Location.Balcony, Location.Hall
        };

        string[] rActions = {
            "Ничего", "Лечь спать", "Пойти в туалет", "Поесть", "Покурить", "Потрясти пакетиком",
            "- Кс-кс-кс", "- Кто хороший мальчик?", "- **** ****** *****",
            "Почистить кошачий лоток", "Почистить собачую простынь", "Почистить клетку попугая",
            "Наложить еды коту", "Наложить еды собаке", "Наложить еды попугаю",
            "Сыграть на пианино", "Сыграть на гитаре"
        };

        string[] rLocations = {
            "Спальня", "Кухня", "Ванная комната", "Балкон", "Зал"
        };

        public static int ItemToIndex(string item)
        {
            switch (item)
            {
                case "Спальня": return 0;
                case "Кухня": return 1;
                case "Ванная комната": return 2;
                case "Балкон": return 3;
                case "Зал": return 4;
                case "Ничего": return 0;
                case "Лечь спать": return 1;
                case "Пойти в туалет": return 2;
                case "Поесть": return 3;
                case "Покурить": return 4;
                case "Потрясти пакетиком": return 5;
                case "- Кс-кс-кс": return 6;
                case "- Кто хороший мальчик?": return 7;
                case "- **** ****** *****": return 8;
                case "Почистить кошачий лоток": return 9;
                case "Почистить собачую простынь": return 10;
                case "Почистить клетку попугая": return 11;
                case "Наложить еды коту": return 12;
                case "Наложить еды собаке": return 13;
                case "Наложить еды попугаю": return 14;
                case "Сыграть на пианино": return 15;
                case "Сыграть на гитаре": return 16;
                default: return -1;
            }
        }

        public static string Translate(Enum state)
        {
            switch (state)
            {
                case Location.Bedroom: return "Спальня";
                case Location.Kitchen: return "Кухня";
                case Location.Bathroom: return "Ванная";
                case Location.Balcony: return "Балкон";
                case Location.Hall: return "Зал";
                case Action.Nothing: return "Ничего";
                case Action.Sleep: return "Спит";
                case Action.Shit: return "В туалете";
                case Action.Eat: return "Ест";
                case Action.Smoke: return "Курит";
                case Action.ShakesPlasticBag: return "Трясет пластиковым пакетом";
                case Action.SaysPussPussPuss: return "Зовет кота";
                case Action.SaysWhoIsGoodBoy: return "Зовет собаку";
                case Action.SaysBadWords: return "Говорит плохие слова";
                case Action.CleansCatLitterBox: return "Чистит кошачий лоток";
                case Action.CleansDogSheet: return "Чистит собачью простынку";
                case Action.CleansParrotCell: return "Чистит клетку попугая";
                case Action.PutOnCatFood: return "Кладет еду коту";
                case Action.PutOnDogFood: return "Кладет еду собаке";
                case Action.PutOnCarrotFood: return "Кладет еду попугаю";
                case Action.PlaysOnPiano: return "Играет на пианино";
                case Action.PlaysOnGuitar: return "Играет на гитаре";
                default: return string.Empty;
            }
        }

        public static string SplitString(string content, int length)
        {
            if (content.Length <= length)
                return content;

            char[] charsForEOL = { '.', ',', ' ', '?', '!' };
            string result = "";

            do
            {
                for (int i = length; i >= 1; i--)
                {
                    if (charsForEOL.Contains(content[i]))
                    {
                        result += content.Substring(0, i) + "\n";
                        content = content.Substring(i + 1);
                        break;
                    }
                    if (i == 1)
                    {
                        result += content.Substring(0, length) + "\n";
                        content = content.Substring(length + 1);
                    }
                }
            } while (content.Length > length);

            return result + content;
        }

        public MainWindow()
        {
            InitializeComponent();

            UpdateStates();
            UpdateActions();
            UpdateLocations();
        }

        public void UpdateStates()
        {
            humanActionLbl.Text = Translate(human.Action);
            humanLocationLbl.Text = Translate(human.Location);
            catActionLbl.Text = Translate(cat.Action);
            catLocationLbl.Text = Translate(cat.Location);
            dogActionLbl.Text = Translate(dog.Action);
            dogLocationLbl.Text = Translate(dog.Location);
            carrotActionLbl.Text = Translate(carrot.Action);
            carrotLocationLbl.Text = Translate(carrot.Location);
        }

        public void UpdateActions()
        {
            List<string> content = new List<string>();
            foreach (string action in rActions)
                if (human.CanIDo(actions[ItemToIndex(action)]))
                    content.Add(action);

            actionCmbBx.ItemsSource = content;
        }

        public void UpdateLocations()
        {
            List<string> content = new List<string>();
            foreach (string location in rLocations)
                if (human.CanIGo(locations[ItemToIndex(location)]))
                    content.Add(location);

            locationCmbBx.ItemsSource = content;
        }

        private void ChBx_Click(object sender, RoutedEventArgs e)
        {
            CheckBox checkBox = sender as CheckBox;

            switch (checkBox.Name)
            {
                case "catChBx":
                    catTxtBx.Text += ((bool)checkBox.IsChecked ? human.Subscribe(cat) : human.Unsubscribe(cat)) + '\n';
                    break;
                case "dogChBx":
                    dogTxtBx.Text += ((bool)checkBox.IsChecked ? human.Subscribe(dog) : human.Unsubscribe(dog)) + '\n';
                    break;
                case "carrotChBx":
                    carrotTxtBx.Text += ((bool)checkBox.IsChecked ? human.Subscribe(carrot) : human.Unsubscribe(carrot)) + '\n';
                    break;
            }

            UpdateStates();
        }

        private void ClearBtn_Click(object sender, RoutedEventArgs e)
        {
            Button button = sender as Button;

            switch (button.Name)
            {
                case "catClearBtn":
                    catTxtBx.Text = string.Empty;
                    break;
                case "dogClearBtn":
                    dogTxtBx.Text = string.Empty;
                    break;
                case "carrotClearBtn":
                    carrotTxtBx.Text = string.Empty;
                    break;
            }

            UpdateStates();
        }

        private void CmbBx_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            ComboBox comboBox = sender as ComboBox;
            if (comboBox.SelectedIndex == -1)
                return;
            string reactions = string.Empty;

            switch (comboBox.Name)
            {
                case "actionCmbBx":
                    reactions = human.Update(actions[ItemToIndex((string)actionCmbBx.SelectedItem)]);
                    break;
                case "locationCmbBx":
                    reactions = human.Update(locations[ItemToIndex((string)locationCmbBx.SelectedItem)]);
                    break;
            }

            UpdateStates();
            UpdateActions();
            UpdateLocations();

            foreach (string reaction in reactions.Split('\n').Where(r => r != ""))
                switch (reaction[0])
                {
                    case '1':
                        catTxtBx.Text += reaction.Remove(0, 2) + '\n';
                        break;
                    case '2':
                        dogTxtBx.Text += reaction.Remove(0, 2) + '\n';
                        break;
                    case '3':
                        carrotTxtBx.Text += reaction.Remove(0, 2) + '\n';
                        break;
                    default:
                        break;
                }

            actionCmbBx.SelectedIndex = -1;
            locationCmbBx.SelectedIndex = -1;
        }

        private void TxtBx_TextChanged(object sender, TextChangedEventArgs e)
        {
            TextBox textBox = sender as TextBox;

            string[] lines = textBox.Text.Split('\n');

            for (int i = 0; i < lines.Length; i++)
            {
                lines[i] = SplitString(lines[i], 35);
            }

            textBox.Text = string.Join("\n", lines);

            textBox.ScrollToEnd();
        }
    }
}
