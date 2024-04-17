using System;
using System.Collections.Generic;

namespace s3_kt_lw_02
{
    class Program
    {
        static void Main(string[] args)
        {
            List<Node> alphabet = new List<Node>();
            string letters = "abcdefghijklmnopqrstuvwxyz";
            List<decimal> probabilityList = HaffmansAlgorithm.ProbabilityGenerator(letters);

            for (int i = 0; i < letters.Length; i++)
                alphabet.Add(new Node(probabilityList[i], $"{letters[i]}", ""));

            List<Node> result = HaffmansAlgorithm.GetHaffmansCode(alphabet);
            result.Sort(); result.Reverse();

            foreach (Node item in result)
                Console.WriteLine("{0,3} {1,6:F4} {2,15}", item.Element, item.Probability, item.HaffmansCode);
        }
    }
}