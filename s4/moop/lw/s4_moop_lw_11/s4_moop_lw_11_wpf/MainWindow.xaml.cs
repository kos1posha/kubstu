using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Linq;
using System;
using System.Windows.Forms;
using System.Drawing;
using RadioButton = System.Windows.Controls.RadioButton;
using Brushes = System.Windows.Media.Brushes;
using System.Collections.Generic;
using TextBox = System.Windows.Controls.TextBox;
using s4_moop_lw_11;
using Page = s4_moop_lw_11.Page;

namespace s4_moop_lw_11_wpf
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private bool _titleClicked;
        private bool _titleSeparated;
        private bool _commentClicked;
        private bool _commentSeparated;
        private bool _indexedClicked;
        //private bool _blockedClicked;

        public MainWindow()
        {
            InitializeComponent();
            TitleBox.CommandBindings.Add(new CommandBinding(ApplicationCommands.Paste, (_, _) => { } ));
            TitleBox.CommandBindings.Add(new CommandBinding(ApplicationCommands.Undo, (_, _) => { }));
            StartOffsetIndex.CommandBindings.Add(new CommandBinding(ApplicationCommands.Paste, (_, _) => { }));
            EndOffsetIndex.CommandBindings.Add(new CommandBinding(ApplicationCommands.Paste, (_, _) => { }));
        }

        private void Titled_Click(object sender, RoutedEventArgs e)
        {
            if ((bool)Titled.IsChecked!) TitleBlock.Visibility = Visibility.Visible;
            else
            {
                TitleBlock.Visibility = Visibility.Collapsed;
                TitleSeparatorBox.Visibility = Visibility.Collapsed;

                TitleSeparatedButton.Content = "Добавить разделитель";
                TitleBox.Text = "Введите заголовок";
                TitleLeftAlign.IsChecked = true;
                TitleBox.Foreground = Brushes.LightGray;
                TitleLinesLeftCount.Text = $"Осталось строк: 3";

                _titleClicked = false;
                _titleSeparated = false;
            }
        }

        private void TitleAlign_Checked(object sender, RoutedEventArgs e)
        {
            RadioButton align = sender as RadioButton;
            switch (align?.Name)
            {
                case "TitleLeftAlign":
                    TitleBox.TextAlignment = TextAlignment.Left;
                    TitleSeparatorBox.TextAlignment = TextAlignment.Left;
                    return;
                case "TitleRightAlign":
                    TitleBox.TextAlignment = TextAlignment.Right;
                    TitleSeparatorBox.TextAlignment = TextAlignment.Right;
                    return;
                case "TitleCenterAlign":
                    TitleBox.TextAlignment = TextAlignment.Center;
                    TitleSeparatorBox.TextAlignment = TextAlignment.Center;
                    return;
            }
        }

        private void TitleBox_GotFocus(object sender, RoutedEventArgs e)
        {
            if (_titleClicked) return;
            else
            {
                TitleBox.Text = string.Empty;
                TitleBox.Foreground = Brushes.Black;
                TitleLinesLeftCount.Text = $"Осталось строк: 2";

                _titleClicked = true;
            }
        }

        private void TitleBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (!_titleClicked) return;
            else
            {
                if (TitleBox.LineCount == 4)
                {
                    TextChange change = e.Changes.Last();
                    if (change.AddedLength < 3)
                    {
                        int oldCaretIndex = TitleBox.CaretIndex;
                        TitleBox.Text = TitleBox.Text.Remove(change.Offset, change.AddedLength);
                        TitleBox.CaretIndex = oldCaretIndex - 2;
                    }
                }

                List<int> lengths = new List<int>();
                for (int i = 0; i < TitleBox.LineCount; i++)
                    lengths.Add(TitleBox.GetLineLength(i));
                int maxLength = lengths.Max();
                TitleSeparatorBox.Text = new string('-', maxLength);

                TitleLinesLeftCount.Text = $"Осталось строк: {3 - TitleBox.LineCount}";
            }
        }

        private void TitleBox_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            int caretLineIndex = TitleBox.GetLineIndexFromCharacterIndex(TitleBox.CaretIndex);
            string caretLineText = TitleBox.GetLineText(caretLineIndex) + e.Text;
            int caretLineWidth = TextRenderer.MeasureText(caretLineText, new Font(TitleBox.FontFamily.Source, (float)TitleBox.FontSize)).Width;

            if (caretLineWidth >= 310)
                e.Handled = true;
        }

        private void TitleSeparatedButton_Click(object sender, RoutedEventArgs e)
        {
            if (_titleSeparated)
            {
                TitleSeparatedButton.Content = "Добавить разделитель";
                TitleSeparatorBox.Visibility = Visibility.Collapsed;
            }
            else
            {
                TitleSeparatedButton.Content = "Скрыть разделитель";
                TitleSeparatorBox.Visibility = Visibility.Visible;
            }
            _titleSeparated = !_titleSeparated;
        }

        private void Commented_Click(object sender, RoutedEventArgs e)
        {
            if ((bool)Commented.IsChecked!) CommentBlock.Visibility = Visibility.Visible;
            else
            {
                CommentBlock.Visibility = Visibility.Collapsed;
                CommentSeparatorBox.Visibility = Visibility.Collapsed;

                CommentSeparatedButton.Content = "Добавить разделитель";
                CommentBox.Text = "Введите заголовок";
                CommentLeftAlign.IsChecked = true;
                CommentBox.Foreground = Brushes.LightGray;
                CommentLinesLeftCount.Text = $"Осталось строк: 3";

                _commentClicked = false;
                _commentSeparated = false;
            }
        }

        private void CommentAlign_Checked(object sender, RoutedEventArgs e)
        {
            RadioButton align = sender as RadioButton;
            switch (align?.Name)
            {
                case "CommentLeftAlign":
                    CommentBox.TextAlignment = TextAlignment.Left;
                    CommentSeparatorBox.TextAlignment = TextAlignment.Left;
                    return;
                case "CommentRightAlign":
                    CommentBox.TextAlignment = TextAlignment.Right;
                    CommentSeparatorBox.TextAlignment = TextAlignment.Right;
                    return;
                case "CommentCenterAlign":
                    CommentBox.TextAlignment = TextAlignment.Center;
                    CommentSeparatorBox.TextAlignment = TextAlignment.Center;
                    return;
            }
        }

        private void CommentBox_GotFocus(object sender, RoutedEventArgs e)
        {
            if (_commentClicked) return;
            else
            {
                CommentBox.Text = string.Empty;
                CommentBox.Foreground = Brushes.Black;
                CommentLinesLeftCount.Text = $"Осталось строк: 2";

                _commentClicked = true;
            }
        }

        private void CommentBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            if (!_commentClicked) return;
            else
            {
                if (CommentBox.LineCount == 4)
                {
                    TextChange change = e.Changes.Last();
                    if (change.AddedLength < 3)
                    {
                        int oldCaretIndex = CommentBox.CaretIndex;
                        CommentBox.Text = CommentBox.Text.Remove(change.Offset, change.AddedLength);
                        CommentBox.CaretIndex = oldCaretIndex - 2;
                    }
                }

                List<int> lengths = new List<int>();
                for (int i = 0; i < CommentBox.LineCount; i++)
                    lengths.Add(CommentBox.GetLineLength(i));
                int maxLength = lengths.Max();
                CommentSeparatorBox.Text = new string('-', maxLength);

                CommentLinesLeftCount.Text = $"Осталось строк: {3 - CommentBox.LineCount}";
            }
        }

        private void CommentBox_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            int caretLineIndex = CommentBox.GetLineIndexFromCharacterIndex(CommentBox.CaretIndex);
            string caretLineText = CommentBox.GetLineText(caretLineIndex) + e.Text;
            int caretLineWidth = TextRenderer.MeasureText(caretLineText, new Font(CommentBox.FontFamily.Source, (float)CommentBox.FontSize)).Width;

            if (caretLineWidth >= 310)
                e.Handled = true;
        }

        private void CommentSeparatedButton_Click(object sender, RoutedEventArgs e)
        {
            if (_commentSeparated)
            {
                CommentSeparatedButton.Content = "Добавить разделитель";
                CommentSeparatorBox.Visibility = Visibility.Collapsed;
            }
            else
            {
                CommentSeparatedButton.Content = "Скрыть разделитель";
                CommentSeparatorBox.Visibility = Visibility.Visible;
            }
            _commentSeparated = !_commentSeparated;
        }

        private void Indexed_Click(object sender, RoutedEventArgs e)
        {
            if ((bool)Indexed.IsChecked!) IndexedBlock.Visibility = Visibility.Visible;
            else
            {
                IndexedBlock.Visibility = Visibility.Collapsed;
                TitleSeparatorBox.Visibility = Visibility.Collapsed;

                IndexSeparatorComboBox.SelectedIndex = 0;
                StartOffsetIndex.Text = "0";
                EndOffsetIndex.Text = "0";
                IndexLengthTextBox.Text = "0";
                IndexSeparatorTextBox.Text = "0";

                _indexedClicked = false;
            }
        }

        //private void Blocked_Click(object sender, RoutedEventArgs e)
        //{
        //    if ((bool)Blocked.IsChecked!) BlockedBlock.Visibility = Visibility.Visible;
        //    else
        //    {
        //        BlockedBlock.Visibility = Visibility.Collapsed;
        //        TitleSeparatorBox.Visibility = Visibility.Collapsed;

        //        _indexedClicked = false;
        //    }
        //}

        private void OnlyDigits_PreviewTextInput(object sender, TextCompositionEventArgs e)
        {
            e.Handled = !char.IsDigit(e.Text[0]);
        }

        private void PadLeft_TextChanged(object sender, TextChangedEventArgs e)
        {
            TextBox textBox = sender as TextBox;
            if (textBox.Text == "0") return;

            textBox.Text = textBox.Text.Trim(' ').TrimStart('0');
        }

        private void Buid_Click(object sender, RoutedEventArgs e)
        {
            IPageProvider page = new Page(DocumentTextBox.Text);

            if ((bool)Indexed.IsChecked)
            {
                IndexSeparator separator;
                switch (IndexSeparatorComboBox.SelectedIndex)
                {
                    case 0:
                        separator = IndexSeparator.Point;
                        break;
                    case 1:
                        separator = IndexSeparator.Comma;
                        break;
                    case 2:
                        separator = IndexSeparator.Space;
                        break;
                    case 3:
                        separator = IndexSeparator.NewLine;
                        break;
                    case 4:
                        separator = IndexSeparator.Parenthesis;
                        break;
                    case 5:
                        separator = IndexSeparator.Bracket;
                        break;
                    case 6:
                        separator = IndexSeparator.Brace;
                        break;
                    case 7:
                        separator = IndexSeparator.Chevron;
                        break;
                    default:
                        throw new Exception();
                }

                page = new IndexedPage(
                    page,
                    separator,
                    Convert.ToInt32(IndexSeparatorTextBox.Text),
                    Convert.ToInt32(IndexLengthTextBox.Text),
                    Convert.ToInt32(StartOffsetIndex.Text),
                    Convert.ToInt32(EndOffsetIndex.Text));
            }

            if ((bool)Titled.IsChecked)
            {
                Alignment alignment;
                if ((bool)TitleLeftAlign.IsChecked)
                    alignment = Alignment.Left;
                else if ((bool)TitleRightAlign.IsChecked)
                    alignment = Alignment.Right;
                else
                    alignment = Alignment.Center;

                page = new TitledPage(
                    page,
                    TitleBox.Text,
                    alignment,
                    TitleSeparatorBox.Visibility == Visibility.Visible);
            }

            if ((bool)Commented.IsChecked)
            {
                Alignment alignment;
                if ((bool)CommentLeftAlign.IsChecked)
                    alignment = Alignment.Left;
                else if ((bool)CommentRightAlign.IsChecked)
                    alignment = Alignment.Right;
                else
                    alignment = Alignment.Center;

                page = new CommentedPage(
                    page,
                    CommentBox.Text,
                    alignment,
                    CommentSeparatorBox.Visibility == Visibility.Visible);
            }

            DocumentTextBox.Text = page.Content();
        }
    }
}
