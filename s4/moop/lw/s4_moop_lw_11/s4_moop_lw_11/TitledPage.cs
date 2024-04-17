using System;
using System.Linq;

namespace s4_moop_lw_11
{
    public class TitledPage : PageDecorator
    {
        private string _title;
        private Alignment _titleAlignment;
        private bool _separated;
        public TitledPage(IPageProvider instance, string title,
            Alignment titleAlignment = Alignment.Center, bool separated = false)
            : base(instance)
        {
            _title = title;
            _titleAlignment = titleAlignment;
            _separated = separated;
        }
        public override string Content() => $"{GetTitle()}\n\r\n\r{_instance.Content()}";
        private string GetTitle()
        {
            string[] content = _instance.Content().Split('\n');
            string[] lines = _title.Split('\n');
            int maxLength = Math.Max(
                content.Select(line => line.Length).Max(),
                lines.Select(line => line.Length).Max()
            ) - 1;
            string separator = _separated ? new string('-', maxLength) + '\n' : string.Empty;
            switch (_titleAlignment)
            {
                case Alignment.Left:
                    return _title + separator;
                case Alignment.Right:
                    string FullOffset(int titleLength) => new(' ', maxLength - titleLength);
                    return string.Join("\n", lines.Select(line => FullOffset(line.Length) + line)) + separator;
                case Alignment.Center:
                    string HalfOffset(int titleLength) => new(' ', (maxLength - titleLength) / 2);
                    return string.Join("\n", lines.Select(line => HalfOffset(line.Length) + line)) + separator;
                default:
                    throw new NotImplementedException($"Alignment.{_titleAlignment} not implemented yet!");
            }
        }
    }
}