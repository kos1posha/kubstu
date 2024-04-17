using System;

namespace AlgorithmKMP_wpr
{
    class Program
    {
        static int[] GetPrefixFunction(string text)
        {
            int[] prefFunc = new int[text.Length];

            for (int i = 1; i < text.Length; i++)
            {
                for (int j = 1; j <= i; j++)
                {
                    if (text.Substring(0, j) == text.Substring(i - j + 1, j))
                    {
                        prefFunc[i] = j;
                    }
                }
            }
            return prefFunc;
        }
        static int AlgorithmKMP(string haystack, string needle)
        {
            int[] prefFunc = GetPrefixFunction(haystack);
            int index = 0;

            for (int i = 0; i < haystack.Length; i++)
            {
                while (index > 0 && needle[index] != haystack[i])
                {
                    index = prefFunc[index - 1];
                }
                if (needle[index] == haystack[i])
                {
                    index++;
                }
                if (index == needle.Length)
                {
                    return i - index + 1;
                }
            }
            return -1;
        }
        static void Main(string[] args)
        {
            string[] haystack = new string[5] { "accacca", "abcabd", "ababcad", "aaaaaaa", "abcabcd" };
            string[] needle = new string[5] { "cacc", "cabd", "c", "aaaaaaa", "bcdb" };
            //foreach (string sample in haystack)
            //{
            //    Console.WriteLine(sample);
            //    foreach (int item in GetPrefixFunction(sample))
            //        Console.Write(item);
            //    Console.WriteLine("\n");
            //}
            for (int i = 0; i < 5; i++)
            {
                Console.WriteLine($"{needle[i]} is substring {haystack[i]} from {AlgorithmKMP(haystack[i], needle[i])} position.");
            }
        }
    }
}
