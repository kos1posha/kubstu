using System;

namespace s3_kt_lw_01
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Node> test = SFAlgorithm.ProbabilityGenerator("abcdefgwhijklmnopqrstuvwxyz");
            SFAlgorithm.GetSFCode(test);

            decimal sumSFCl = 0,
                    sumP = 0;

            foreach (Node item in test)
            {
                sumSFCl += item.SFCode.Length;
                sumP += item.Probability;
            }
            for (int i = 0; i < test.Count; i++)
            {
                Console.WriteLine("{0,3} {1,6:F4} {2,15} {3:F5}", test[i].Element, test[i].Probability, test[i].SFCode, test[i].SFCode.Length / sumSFCl);
            }

            Console.WriteLine($"\nsumP = {sumP:F4}");
        }
    }
}