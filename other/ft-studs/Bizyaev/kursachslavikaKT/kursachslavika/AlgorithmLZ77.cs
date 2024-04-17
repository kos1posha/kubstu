using System;
using System.Collections.Generic;

namespace kursachslavika
{
    public class NodeLZ77
    {
        public int Offset;
        public int Length;
        public char? Next;

        public char Separator => AlgorithmLZ77.Separator;

        public NodeLZ77()
            : this(0, 0, ' ')
        {

        }
        public NodeLZ77(int offset, int length, char? next)
        {
            Offset = offset;
            Length = length;
            Next = next;
        }

        public string Decode(string buffer)
        {
            if (Offset == 0 || Length == 0)
                return Next.ToString();

            string result = string.Empty;
            buffer = buffer.Remove(0, buffer.Length - Offset);

            for (int i = 0, j = 0; i < Length; i++, j++)
            {
                if (j == buffer.Length)
                    j = 0;
                result += buffer[j];
            }

            return Next == null ? result : result + Next;
        }

        public override string ToString()
        {
            if (Next != null)
                return $"{Offset}{Separator}{Length}{Separator}{Next}{Separator}";
            else
                return $"{Offset}{Separator}{Length}{Separator}eof";
        }
    }

    public static class AlgorithmLZ77
    {
        public static char Separator = ' ';

        public static (string Result, List<NodeLZ77> ToList) Encode(string text) => Encode(text, text.Length, ' ');
        public static (string Result, List<NodeLZ77> ToList) Encode(string text, int bufferSize) => Encode(text, bufferSize, ' ');
        public static (string Result, List<NodeLZ77> ToList) Encode(string text, char separator) => Encode(text, text.Length, separator);
        public static (string Result, List<NodeLZ77> ToList) Encode(string text, int bufferSize, char separator)
        {
            Separator = separator;

            string result = string.Empty;
            List<NodeLZ77> toList = new List<NodeLZ77>();

            for (int position = 0, offset, length; position < text.Length; position++)
            {
                (offset, length) = FindMatch(text, bufferSize, position);
                try { toList.Add(new NodeLZ77(offset, length, text[position += length])); }
                catch { toList.Add(new NodeLZ77(offset, length, null)); }
            }

            foreach (NodeLZ77 node in toList)
                result += node.ToString();

            return (result, toList);
        }

        public static string Decode(string encodedText) => Decode(encodedText, ' ');
        public static string Decode(string encodedText, char separator)
        {
            Separator = separator;

            string result = string.Empty;
            string buffer = string.Empty;
            NodeLZ77 node = new NodeLZ77();

            for (int i = 0, j = 0; i < encodedText.Length; i++)
            {
                if (encodedText[i] != separator)
                    buffer += encodedText[i];
                else
                {
                    switch (j)
                    {
                        case 0:
                            node.Offset = Convert.ToInt32(buffer);
                            break;
                        case 1:
                            node.Length = Convert.ToInt32(buffer);
                            break;
                        case 2:
                            node.Next = Convert.ToChar(buffer);
                            break;
                    }

                    if (j++ == 2)
                    {
                        result += node.Decode(result);
                        j = 0;
                    }

                    buffer = string.Empty;
                }
            }

            if (buffer == "eof")
            {
                node.Next = null;
                result += node.Decode(result);
            }

            return result;
        }
        public static string Decode(List<NodeLZ77> encodedList)
        {
            string result = string.Empty;

            foreach (NodeLZ77 node in encodedList)
                result += node.Decode(result);

            return result;
        }

        public static (int Offset, int Length) FindMatch(string text, int bufferSize, int position)
        {
            string buffer = string.Empty;
            int length;

            if (position <= bufferSize)
                bufferSize = position;

            for (int i = bufferSize; i > 0; i--)
                buffer += text[position - i];

            while (buffer.Length > 0)
                if (text[position] != buffer[0]) buffer = buffer.Remove(0, 1);
                else break;

            if (buffer.Length == 0)
                return (0, 0);

            for (length = 0; position < text.Length; position++, length++)
                if (text[position] != buffer[length % buffer.Length])
                    return (buffer.Length, length);

            if (position == text.Length) return (buffer.Length, length);
            else return (buffer.Length, 1);
        }
    }
}