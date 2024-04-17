using System;
using System.Collections.Generic;
using System.Linq;

namespace s4_moop_lw_11
{
    public class BlockedPage : PageDecorator
    {
        private BlockSeparator _blockSeparator;
        private int _blockLength, _blockSpace, _startOffset, _endOffset;
        public BlockedPage(IPageProvider instance, BlockSeparator blockSeparator = BlockSeparator.Space,
            int blockLength = 1, int blockSpace = 1, int startOffset = 0, int endOffset = 0)
            : base(instance)
        {
            if (blockLength < 1) throw new ArgumentException("Block length can't be less then 1");
            if (blockSpace < 1) throw new ArgumentException("Block space can't be less then 1");
            if (startOffset < 0) throw new ArgumentException("Start offset can't be less then 0");
            if (endOffset < 0) throw new ArgumentException("End offset can't be less then 0");
            _blockSeparator = blockSeparator;
            _blockLength = blockLength;
            _blockSpace = blockSpace;
            _startOffset = startOffset;
            _endOffset = endOffset;
        }
        public override string Content() => BlockedContent();
        private string BlockedContent()
        {
            string[] content = _instance.Content().Split('\n');
            int maxLength = content.Select(line => line.Length).Max();
            string separator = new string((char)_blockSeparator, maxLength);
            List<string> blocks = new List<string>();
            for (int i = 0 + _startOffset; i < content.Length - _endOffset; i += _blockLength)
            {
                string block = string.Empty;
                for (int j = i; j - i < _blockLength && j < content.Length - _endOffset; j++)
                    block += content[j] + '\n';
                blocks.Add(block);
            }
            return string.Join("\n", content.Take(_startOffset)) + '\n' +
                   string.Join(new string('\n', _blockSpace / 2) + separator + new string('\n', (_blockSpace + 1) / 2), blocks) +
                   string.Join("\n", content.Skip(content.Length - _endOffset));
        }
    }
}