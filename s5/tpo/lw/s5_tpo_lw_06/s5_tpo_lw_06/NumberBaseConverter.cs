using System;
using System.Collections.Generic;

namespace s5_tpo_lw_06
{
    public static class NumberBaseConverter
    {
        public static int Base8ToBase10(string stringNB8)
        {
            if (!int.TryParse(stringNB8, out int target))                                                                       // 1
                throw new ArgumentException("String must be integer.");                                                         // 2
            if (target < 0)                                                                                                     // 3
                throw new ArgumentOutOfRangeException(nameof(stringNB8));                                                       // 4
            List<int> digits = new List<int>();                                                                                 // 5
            foreach (char c in stringNB8)                                                                                       // 6
                if (char.IsDigit(c))                                                                                            // 7
                {                                                                                                               
                    int digit = int.Parse(c.ToString());                                                                        // 8
                    if (digit > 7)                                                                                              // 9
                        throw new FormatException("The number contains characters not found in the 8-based number system.");    // 10
                    digits.Add(digit);                                                                                          // 11
                }                               
            digits.Reverse();                                                                                                   // 12
            int result = 0;                                                                                                     // 13
            for (int i = 0; i < digits.Count; i++)                                                                              // 14
            {
                int digit = digits[i];                                                                                          // 15
                result += digit * (int) Math.Pow(8, i);                                                                         // 16
            }
            return result;                                                                                                      // 17
        }
    }
}