using System;

namespace s5_tpo_lw_04
{
    public static class StringExtensions
    {
        public static string Merge(this string source, string mergedString)
        {
            string result = string.Empty;                                                       // 1
            bool sourceBigger = source.Length > mergedString.Length;                            // 2
            int length = sourceBigger                                                           // 3
                ? mergedString.Length                                                           // 4
                : source.Length;                                                                // 5 
            while (length > 0)                                                                  // 6
            {
                length--;                                                                       // 7
                result = result.Insert(0, $"{source[length]}{mergedString[length]}");           // 8
            }
            result += sourceBigger                                                              // 9
                ? source.Substring(mergedString.Length, source.Length - mergedString.Length)    // 10
                : mergedString.Substring(source.Length, mergedString.Length - source.Length);   // 11
            return result;                                                                      // 12
        }
    }
    
    internal static class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("123".Merge("123"));
            Console.WriteLine("".Merge("123"));
            Console.WriteLine("123".Merge(""));
            Console.WriteLine("".Merge(""));
        }
    }
}