using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s3_kt_cw
{
    public static class SFAlgorithm
    {
        public static string Encode(string text, SplitPrinciple splitPrinciple)
        {
            SFTree tree = new SFTree(text, splitPrinciple);
            string result = tree.GetEncodedAlphabet();

            foreach (char symbol in text)
                foreach (SFNode node in tree.Data)
                    if (node.Element == symbol)
                        result += node.SFCode;

            return result;
        }
        public static string Decode(string text)
        {
            string result = text.Split(' ')[text.Split(' ').Length - 1];

            Dictionary<string, char> alphabet = GetCodedAlphabet(text);

            string buffer = string.Empty;
            for (int i = 0, shift = 0; i < result.Length; i++, shift = i)
            {
                while (!alphabet.ContainsKey(buffer))
                    buffer += result[shift++];

                result = result.Remove(i, shift - i).Insert(i, alphabet[buffer].ToString());
                buffer = string.Empty;
            }

            return result;
        }

        public static Dictionary<string, char> GetCodedAlphabet(string encodedText)
        {
            List<string> codedAlphabet = new List<string>();

            codedAlphabet.AddRange(encodedText.Split(' '));
            codedAlphabet.RemoveAt(codedAlphabet.Count - 1);

            Dictionary<string, char> alphabet = new Dictionary<string, char>();
            for (int i = 0; i < codedAlphabet.Count; i += 2)
                alphabet.Add(codedAlphabet[i + 1], Convert.ToChar(Convert.ToInt16(codedAlphabet[i], 2)));

            return alphabet;
        }
    }
}
