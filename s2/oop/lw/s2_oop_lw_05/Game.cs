using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace s2_oop_lw_05
{
    public partial class Game : Form
    {
        public void UpdateHeroStatus()
        {
            heroHealth.Text = $"{Math.Round(Hero.CurrentHealth, 1)} / {Math.Round(Hero.MaxHealth, 1)}";
            heroWeight.Text = $"{Math.Round(Hero.CurrentWeight, 1)} / {Math.Round(Hero.MaxWeight, 1)}";
            heroGold.Text = $"{Hero.Gold}";
            heroEquipment.Items.Clear();
            heroItems.Items.Clear();
            for (int i = 0; i < Hero.Slots; i++) heroEquipment.Items.Add(Hero.Items[i]);
            for (int i = Hero.Slots; i < Hero.Items.Count; i++) heroItems.Items.Add(Hero.Items[i]);
            if (Hero.CurrentHealth <= 0)
            {
                DialogResult result = MessageBox.Show("Вы умерли. Хотите начать заново?", "Игра окончена", MessageBoxButtons.YesNo);
                if (result == DialogResult.Yes)
                {
                    Registration registration = new Registration();
                    registration.Show();
                    Dispose();
                }
                else Environment.Exit(0);
            }
        }
        public void OnItemsButtons()
        {
            useButton.Enabled = true;
            throwButton.Enabled = true;
        }
        public void OffItemsButtons()
        {
            useButton.Enabled = false;
            throwButton.Enabled = false;
        }
        public void AddItem(Item item)
        {
            Hero.Items.Add(item);
            UpdateHeroStatus();
        }
        public void RemoveItem(int index)
        {
            Hero.Items.RemoveAt(index);
            UpdateHeroStatus();
        }
        public void WriteToHistory(string newHistory)
        {
            history.Text += newHistory + "\n";
            history.SelectionStart = history.Text.Length;
            history.ScrollToCaret();
        }
        public Hero Hero;
        public Random Random = new Random();
        public Dictionary<string, Item> Items = new Dictionary<string, Item>()
        {
            { "startSword", new Sword("Деревянный меч", 4, 20, null, 1, 4, 0.1, 1.5) },
            { "commonSword", new Sword("Обычный меч", 9, 300, null, 3, 9, 0.15, 1.5) },

            { "startBow", new Bow("Старый лук", 4, 20, null, 0, 3, 0.1, 1.5, 0.1) },
            { "commonBow", new Bow("Обычный лук", 5, 250, null, 1, 7, 0.15, 1.5, 0.2) },

            { "startDagger", new Dagger("Кухонный нож", 2, 20, null, 2, 3, 0.3, 2, 0) },
            { "commonDagger", new Dagger("Обычный кинжал", 3, 150, null, 4, 6, 0.4, 2, 1) },

            { "startArmor", new LightArmor("Старые лохмотья", 2, 0, null, 0.05)},
            { "testArmor", new HeavyArmor("Банка из под пива", 0.8, 99999, null, 1)},

            { "startShield", new Shield("Деревянный щит", 5, 20, null, 0.1) },
            { "commonShield", new Shield("Железный щит", 10, 150, null, 0.15) },

            { "startArrowheads", new Arrowheads("Ржавые наконечники", 5, 20, null, 1) },
            { "commonArrowheads", new Arrowheads("Железные наконечники", 10, 0, null, 2) },

            { "startLubricant", new Lubricant("Собственная слюна", 5, 20, null, 0.5) },
            { "commonLubricant", new Lubricant("Крапивная смазка", 0.1, 80, null, 1) },
        };
        public Game(string heroName, string heroClass)
        {
            InitializeComponent();
            WriteToHistory("Вы создали персонажа.");
            List<Item> test = new List<Item>();
            test.AddRange(Items.Values);
            switch (heroClass)
            {
                case "Мечник":
                    heroView.BackgroundImage = Properties.Resources.sworder;
                    Hero = new Sworder(heroName, 200, test);
                    break;
                case "Лучник":
                    heroView.BackgroundImage = Properties.Resources.archer;
                    Hero = new Archer(heroName, 200, test);
                    break;
                case "Разбойник":
                    heroView.BackgroundImage = Properties.Resources.rogue;
                    Hero = new Rogue(heroName, 200, test);
                    break;
            }
            heroInfoBox.Text = heroName;
            this.heroClass.Text = heroClass;
            UpdateHeroStatus();
            eventComboBox.Enabled = false;
        }

        private void eventComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            eventBox.Text = eventComboBox.SelectedItem.ToString();
            switch (eventComboBox.SelectedItem)
            {
                case "Городская площадь":
                    break;
                case "Торговец":
                    break;
                case "Клирик":
                    break;
                case "Противник 1":
                    break;
                case "Противник 2":
                    break;
                case "Противник 3":
                    break;
            }
        }

        private void useButton_Click(object sender, EventArgs e)
        {
            if (useButton.Text == "Снять")
            {
                switch (heroEquipment.SelectedIndex)
                {
                    case 0:
                        AddItem(new Weapon()); Hero.SetWeapon((Weapon)Hero.Items[Hero.Items.Count - 1]);
                        (Hero.Items[Hero.Items.Count - 1], Hero.Items[0]) = (Hero.Items[0], Hero.Items[Hero.Items.Count - 1]);
                        UpdateHeroStatus(); return;
                    case 1:
                        AddItem(new Armor()); Hero.SetArmor((Armor)Hero.Items[Hero.Items.Count - 1]);
                        (Hero.Items[Hero.Items.Count - 1], Hero.Items[1]) = (Hero.Items[1], Hero.Items[Hero.Items.Count - 1]);
                        UpdateHeroStatus(); return;
                    case 2:
                        AddItem(new Accessory()); Hero.SetAccessory((Accessory)Hero.Items[Hero.Items.Count - 1]);
                        (Hero.Items[Hero.Items.Count - 1], Hero.Items[2]) = (Hero.Items[2], Hero.Items[Hero.Items.Count - 1]);
                        UpdateHeroStatus(); return;
                }
            }
            if (heroItems.SelectedItem is Aid aid)
            {
                WriteToHistory(Hero.Use(aid));
            }
            if (heroItems.SelectedItem is Weapon weapon)
            {
                WriteToHistory(Hero.SetWeapon(weapon));
                if (Hero.CanUse(weapon))
                {
                    if (Hero.Items[0].Name.Contains("Слот"))
                    {
                        Hero.Items[0] = Hero.Items[heroItems.SelectedIndex + Hero.Slots];
                        RemoveItem(heroItems.SelectedIndex + Hero.Slots);
                    }
                    else (Hero.Items[heroItems.SelectedIndex + Hero.Slots], Hero.Items[0]) = (Hero.Items[0], Hero.Items[heroItems.SelectedIndex + Hero.Slots]);
                }
            }
            if (heroItems.SelectedItem is Armor armor)
            {
                WriteToHistory(Hero.SetArmor(armor));
                if (Hero.CanUse(armor))
                {
                    if (Hero.Items[1].Name.Contains("Слот"))
                    {
                        Hero.Items[1] = Hero.Items[heroItems.SelectedIndex + Hero.Slots];
                        RemoveItem(heroItems.SelectedIndex + Hero.Slots);
                    }
                    else (Hero.Items[heroItems.SelectedIndex + Hero.Slots], Hero.Items[1]) = (Hero.Items[1], Hero.Items[heroItems.SelectedIndex + Hero.Slots]);
                }
            }
            if (heroItems.SelectedItem is Accessory accessory)
            {
                WriteToHistory(Hero.SetAccessory(accessory));
                if (Hero.CanUse(accessory))
                {
                    if (Hero.Items[2].Name.Contains("Слот"))
                    {
                        Hero.Items[2] = Hero.Items[heroItems.SelectedIndex + Hero.Slots];
                        RemoveItem(heroItems.SelectedIndex + Hero.Slots);
                    }
                    else (Hero.Items[heroItems.SelectedIndex + Hero.Slots], Hero.Items[2]) = (Hero.Items[2], Hero.Items[heroItems.SelectedIndex + Hero.Slots]);
                }
            }
            UpdateHeroStatus();
        }

        private void throwButton_Click(object sender, EventArgs e)
        {
            if (heroItems.SelectedItem == Hero.CurrentWeapon)
            {
                WriteToHistory("Вы не можете выбросить используемое оружие.");
                return;
            }
            if (heroItems.SelectedItem != null)
            {
                DialogResult result = MessageBox.Show("Вы уверены, что хотите это выбросить?", "", MessageBoxButtons.YesNo);
                if (result == DialogResult.Yes)
                {
                    Item item = (Item)heroItems.SelectedItem;
                    RemoveItem(heroItems.SelectedIndex);
                    WriteToHistory($"Вы выбросили из инвентаря следующий предмет: {item.Name.ToLower()}.");
                }
            }
            else WriteToHistory("Выберите предмет из инвентаря.");
        }

        private void quickHealButton_Click(object sender, EventArgs e)
        {
            Aid smallestAid = new Aid(10000);
            int smallestAidIndex = -1;
            for (int i = 0; i < Hero.Items.Count; i++)
            {
                if (Hero.Items[i] is Aid aid && smallestAid.Heal > aid.Heal)
                {
                    smallestAid = aid;
                    smallestAidIndex = i;
                }
            }
            if (smallestAidIndex != -1) WriteToHistory(Hero.Use(smallestAid));
            else WriteToHistory("У вас нет аптечек.");
            UpdateHeroStatus();
        }

        private void quickAidButton_Click(object sender, EventArgs e)
        {
            Aid aid = new Aid(Random.Next(5, 11) * 4);
            if (Hero.CurrentWeight + aid.Weight <= Hero.MaxWeight)
            {
                AddItem(aid);
                WriteToHistory($"Вы нашли следующий предмет: {aid.Name} +{aid.Heal}.");
            }
            else WriteToHistory("Вы не можете это взять, так как инвентарь переполнен.");
        }

        private void quickDamageButton_Click(object sender, EventArgs e)
        {
            Hero.CurrentHealth -= 10;
            UpdateHeroStatus();
        }

        private void settingsButton_Click(object sender, EventArgs e)
        {
            Enabled = false;
            Settings settings = new Settings(this);
            settings.Show();
        }

        private void goButton_Click(object sender, EventArgs e)
        {
            eventComboBox.Enabled = true;
            if (Hero.Location == "town")
            {
                WriteToHistory("Вы отправились в дикие земли.");
                Hero.Location = "wildlands";
                goButton.Text = "В город";
                eventBox.Text = "Дикие земли";
                eventText.Text = "Перед вашими глазами растилаются дикие земли, полные тайн и опасностей.";
            }
            else
            {
                WriteToHistory("Вы отправились в город.");
                Hero.Location = "town";
                goButton.Text = "В дикие земли";
                eventBox.Text = "Город";
                eventText.Text = "Вы видите знакомые очертания города.\n" +
                                 "Горожане по обычному оживлены, торговец зазывает в свою лавку очередного проходимца.\n" +
                                 "Клирик продолжает толкать свои речи об очищении людских умов от скверны.\n" +
                                 "Когда-нибудь до него дойдет, что его добавили только ради интерфейса IDoctor, заявленного в тз.";
            }
            eventComboBox.Items.Clear();
            switch (Hero.Location)
            {
                case "town":
                    eventComboBox.Items.AddRange(new string[] { "Городская площадь", "Торговец", "Клирик" });
                    break;
                case "wildlands":
                    eventComboBox.Items.AddRange(new string[] { "Лагерь", "Противник 1", "Противник 2", "Противник 3" });
                    break;
            }
        }

        private void heroEquipment_SelectedIndexChanged(object sender, EventArgs e)
        {
            OnItemsButtons();
            int index = heroEquipment.SelectedIndex;
            heroItems.SelectedItem = null;
            heroEquipment.SelectedIndex = index;
            useButton.Text = "Снять";
            if (heroEquipment.SelectedItem is Item item && item.Name.Contains("Слот")) OffItemsButtons();
            else OnItemsButtons();
        }

        private void heroItems_SelectedIndexChanged(object sender, EventArgs e)
        {
            OnItemsButtons();
            int index = heroItems.SelectedIndex;
            heroEquipment.SelectedItem = null;
            heroItems.SelectedIndex = index;
            if (heroItems.SelectedItem is Aid) useButton.Text = "Использовать";
            if (heroItems.SelectedItem is Weapon) useButton.Text = "Взять в руки";
            if (heroItems.SelectedItem is Armor) useButton.Text = "Надеть";
            if (heroItems.SelectedItem is Accessory) useButton.Text = "Экипировать";
        }

        private void attackButton_Click(object sender, EventArgs e) 
        {

        }
    }
}
