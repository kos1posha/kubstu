using System.Collections.Generic;

namespace LZ77
{


    public static class AlgorithmLZW
    {
        public static (string Result, Dictionary<string, int> Dictionary) Encode(string text)
        {
            string result = string.Empty;
            Dictionary<string, int> dictionary = GetDictionary(text);
            string buffer = string.Empty;

            foreach (char next in text)
                if (dictionary.ContainsKey(buffer + next))
                    buffer += next;
                else
                {
                    result += dictionary[buffer];
                    dictionary.Add(buffer + next, dictionary.Count);
                    buffer = next.ToString();
                }

            return (result + dictionary[buffer], dictionary);
        }

        public static string Encode(string text, Dictionary<string, int> alphabet)
        {
            Dictionary<int, string> dictionary = new Dictionary<int, string>();
            foreach (KeyValuePair<string, int> pair in alphabet)
                dictionary.Add(pair.Value, pair.Key);

            string result = string.Empty;
            string buffer = string.Empty;

            foreach (char next in text)
            {

            }

            return result;
        }

        public static Dictionary<string, int> GetDictionary(string text)
        {
            Dictionary<string, int> result = new Dictionary<string, int>();

            foreach (char next in text)
                if (!result.ContainsKey(next.ToString()))
                    result.Add(next.ToString(), result.Count);

            return result;
        }
    }
}