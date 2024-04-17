using System;

namespace s5_tpo_lw_06
{
    internal static class Program
    {
        public static void Main()
        {
            Console.WriteLine(NumberBaseConverter.Base8ToBase10("1"));
            Console.WriteLine(NumberBaseConverter.Base8ToBase10("123"));
            Console.WriteLine(NumberBaseConverter.Base8ToBase10("1234"));
            Console.WriteLine(NumberBaseConverter.Base8ToBase10("12345"));
        }
    }
}