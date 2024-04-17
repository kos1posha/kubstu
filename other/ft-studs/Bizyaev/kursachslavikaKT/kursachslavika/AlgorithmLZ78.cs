using System;
using System.Collections.Generic;

namespace kursachslavika
{
    public class NodeLZ78
    {
        public int Index;
        public char? Next;

        public char Separator => AlgorithmLZ78.Separator;

        public NodeLZ78()
            : this(0, ' ')
        {

        }
        public NodeLZ78(int index, char? next)
        {
            Index = index;
            Next = next;
        }

        public string Decode(Dictionary<int, string> dictionary)
        {
            string result;

            try { result = dictionary[Index] + Next; }
            catch { result = Next.ToString(); }

            dictionary.Add(dictionary.Count + 1, result);
            return result;
        }

        public override string ToString()
        {
            if (Next != null)
                return $"{Index}{Separator}{Next}{Separator}";
            else
                return $"{Index}{Separator}eof";
        }
    }

    public static class AlgorithmLZ78
    {
        public static char Separator = ' ';

        public static (string Result, List<NodeLZ78> ToList, Dictionary<string, int> Dictionary) Encode(string text) => Encode(text, ' ');
        public static (string Result, List<NodeLZ78> ToList, Dictionary<string, int> Dictionary) Encode(string text, char separator)
        {
            Separator = separator;

            List<NodeLZ78> toList = new List<NodeLZ78>();
            string result = string.Empty;
            Dictionary<string, int> dictionary = new Dictionary<string, int>();

            string buffer = string.Empty;

            for (int i = 0, index; i < text.Length; i++)
            {
                try { index = dictionary[buffer]; }
                catch { index = 0; }

                buffer += text[i];

                if (!dictionary.ContainsKey(buffer))
                {
                    dictionary.Add(buffer, dictionary.Count + 1);
                    toList.Add(new NodeLZ78(index, text[i]));
                    buffer = string.Empty;
                }

                if (i + 1 > text.Length)
                    toList.Add(new NodeLZ78(index, null));
            }

            foreach (NodeLZ78 node in toList)
                result += node.ToString();

            return (result, toList, dictionary);
        }

        public static string Decode(string encodedText) => Decode(encodedText, ' ');
        public static string Decode(string encodedText, char separator)
        {
            Separator = separator;

            List<NodeLZ78> encodedList = new List<NodeLZ78>();
            string buffer = string.Empty;
            NodeLZ78 node = new NodeLZ78();

            for (int i = 0, j = 0; i < encodedText.Length; i++)
            {
                if (encodedText[i] != separator)
                    buffer += encodedText[i];
                else
                {
                    switch (j)
                    {
                        case 0:
                            node.Index = Convert.ToInt32(buffer);
                            break;
                        case 1:
                            node.Next = Convert.ToChar(buffer);
                            break;
                    }

                    if (j++ == 1)
                    {
                        encodedList.Add(node);
                        node = new NodeLZ78();
                        j = 0;
                    }

                    buffer = string.Empty;
                }
            }

            if (buffer == "eof")
            {
                node.Next = null;
                encodedList.Add(node);
            }

            return Decode(encodedList);
        }
        public static string Decode(List<NodeLZ78> encodedList)
        {
            string result = string.Empty;
            Dictionary<int, string> dictionary = new Dictionary<int, string>();

            foreach (NodeLZ78 node in encodedList)
                result += node.Decode(dictionary);

            return result;
        }
    }
}