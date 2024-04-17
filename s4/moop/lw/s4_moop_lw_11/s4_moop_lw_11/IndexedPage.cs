using System;

namespace s4_moop_lw_11
{
    public class IndexedPage : PageDecorator
    {
        private IndexSeparator _indexSeparator;
        private int _indexSpace, _blockLength, _startOffset, _endOffset;
        public IndexedPage(IPageProvider instance, IndexSeparator indexSeparator = IndexSeparator.Point,
            int indexSpace = 1, int blockLength = 1, int startOffset = 0, int endOffset = 0)
            : base(instance)
        {
            if (indexSpace < 0) throw new ArgumentException("Index space can't be less than 0");
            if (blockLength < 1) throw new ArgumentException("Block length  can't be less then 1");
            if (startOffset < 0) throw new ArgumentException("Start offset can't be less then 0");
            if (endOffset < 0) throw new ArgumentException("End offset can't be less then 0");

            _indexSeparator = indexSeparator;
            _indexSpace = indexSpace;
            _blockLength = blockLength;
            _startOffset = startOffset;
            _endOffset = endOffset;
        }
        public override string Content() => IndexedContent();
        private string IndexedContent()
        {
            string[] content = _instance.Content().Split('\n');
            int space = content.Length.ToString().Length;
            string separator = $"{(char)_indexSeparator}{new string(' ', _indexSpace)}";
            string shift = new string(' ', separator.Length + space);
            for (int i = 0 + _startOffset; i < content.Length - _endOffset; i++)
                content[i] = i % _blockLength == 0
                    ? $"{i + 1}{separator}{new string(' ', space - (i + 1).ToString().Length)}{content[i]}"
                    : $"{shift}{content[i]}";
            return string.Join("\n", content);
        }
    }
}