using System;
using System.Collections.Generic;

namespace LZ77
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("LZ77:");

            string text = "abracadabraffffff";
            (string encodedResult, List<NodeLZ77> toList) = AlgorithmLZ77.Encode(text, '-');
            string resultDTL = AlgorithmLZ77.Decode(toList);
            string resultDER = AlgorithmLZ77.Decode(encodedResult, '-');

            Console.WriteLine(encodedResult);
            foreach (NodeLZ77 node in toList) Console.Write(node);

            Console.WriteLine($"\n\n{resultDTL} {(resultDTL == text ? "[верно]" : "[неверно]")}" +
                                $"\n{resultDER} {(resultDER == text ? "[верно]" : "[неверно]")}");

            
            Console.WriteLine("\n\nLZ78:");

            text = "КРАСНАЯ КРАСКАddddddddddd1231d2fkwlnkl2f";
            (string encodedResult2, List<NodeLZ78> toList2, Dictionary<string, int> dictionary) = AlgorithmLZ78.Encode(text, '-');
            resultDTL = AlgorithmLZ78.Decode(toList2);
            resultDER = AlgorithmLZ78.Decode(encodedResult2, '-');

            Console.WriteLine(encodedResult2);
            foreach (NodeLZ78 node in toList2)
                Console.Write(node);

            Console.WriteLine($"\n\n{resultDTL} {(resultDTL == text ? "[верно]" : "[неверно]")}" +
                                            $"\n{resultDER} {(resultDER == text ? "[верно]" : "[неверно]")}");
        }
    }
}
