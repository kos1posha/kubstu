using System;
using System.Linq;

namespace s4_moop_lw_11
{
    public class CommentedPage : PageDecorator
    {
        private string _comment;
        private Alignment _commentAlignment;
        private bool _separated;
        public CommentedPage(IPageProvider instance, string comment,
            Alignment commentAlignment = Alignment.Left, bool separated = false)
            : base(instance)
        {
            _comment = comment;
            _commentAlignment = commentAlignment;
            _separated = separated;
        }
        public override string Content() => $"{_instance.Content()}\n\r\n\r{GetComment()}";
        private string GetComment()
        {
            string[] content = _instance.Content().Split('\n');
            string[] lines = _comment.Split('\n');
            int maxLength = Math.Max(
                content.Select(line => line.Length).Max(),
                lines.Select(line => line.Length).Max()
            );
            string separator = (_separated ? new string('-', maxLength) : string.Empty) + '\n';
            switch (_commentAlignment)
            {
                case Alignment.Left:
                    return separator + _comment;
                case Alignment.Right:
                    string FullOffset(int titleLength) => new(' ', maxLength - 1 - titleLength);
                    return separator + string.Join("\n", lines.Select(line => FullOffset(line.Length) + line));
                case Alignment.Center:
                    string HalfOffset(int titleLength) => new(' ', (maxLength - 1 - titleLength) / 2);
                    return separator + string.Join("\n", lines.Select(line => HalfOffset(line.Length) + line));
                default:
                    throw new NotImplementedException($"Alignment.{_commentAlignment} not implemented yet!");
            }
        }
    }
}