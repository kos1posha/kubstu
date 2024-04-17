using System;
using System.Collections.Generic;

namespace s3_kt_lw_03
{
    static class AlgorithmRLE
    {
        public static char FindRarestSymbol(string text)
        {
            char rarest = 'q'; int rarestCount = int.MaxValue;
            Dictionary<char, int> symbolCountPairs = new Dictionary<char, int>();

            foreach (char s in text)
            {
                if (symbolCountPairs.ContainsKey(s))
                {
                    symbolCountPairs[s]++;
                    if (rarestCount > symbolCountPairs[s])
                        (rarest, rarestCount) = (s, symbolCountPairs[s]);
                }
                else if (!Char.IsDigit(s))
                {
                    symbolCountPairs.Add(s, 1);
                    (rarest, rarestCount) = (s, 1);
                }
            }

            return rarest;
        }

        public static string Encoding(string text)
        {
            if (text == string.Empty) return string.Empty;

            string changedText = text;
            char rarest = FindRarestSymbol(text);

            for (int i = 0, j; i < changedText.Length; i++)
            {
                char symbol = changedText[i];

                for (j = i + 1; j < changedText.Length; j++)
                    if (changedText[j] != changedText[i])
                        break;
                if ((j - i < 4) && (symbol != rarest))
                    continue;

                changedText = changedText.Remove(i, j - i).Insert(i, $"{rarest}{symbol}{j - i}{rarest}");
                i += $"{rarest}{symbol}{j - i}{rarest}".Length - 1;
            }

            if (changedText.Length >= text.Length) return text;
            else return rarest + changedText;
        }

        public static string Decoding(string text)
        {
            if (text == string.Empty) return string.Empty;

            char prefix = text[0];
            text = text.Remove(0, 1);

            for (int i = 0; i < text.Length; i++)
            {
                if (text[i] != prefix)
                    continue;

                char symbol = text[i + 1];
                string sCount = string.Empty;
                int iCount;

                for (int j = i + 2; j < text.Length; j++)
                {
                    if (text[j] != prefix)
                        sCount += text[j];
                    else break;
                }
                iCount = Convert.ToInt32(sCount);

                text = text.Remove(i, sCount.Length + 3).Insert(i, new String(symbol, iCount));
                i += iCount - 1;
            }

            return text;
        }
    }
}
