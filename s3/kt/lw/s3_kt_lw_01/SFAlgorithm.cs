using System;
using System.Collections.Generic;
using System.Text;

namespace s3_kt_lw_01
{
    class SFAlgorithm
    {
        public const int GeneralProbability = 10000;
        public static List<Node> ProbabilityGenerator(string alphabet)
        {
            List<Node> pList = new List<Node>();
            Random random = new Random();
            int probability = GeneralProbability;

            for (int i = 0, j = 4; i < alphabet.Length - 2; i++)
            {
                if (i % 4 == 0) j++;
                int currentProbability = random.Next(1, probability / j);
                pList.Add(new Node(currentProbability, alphabet[i], ""));
                probability -= currentProbability;
            }
            pList.Add(new Node(probability, alphabet[^1], ""));

            return pList;
        }

        public static void GetSFCode(List<Node> alphabet)
        {
            GetSFCode(alphabet, 0, alphabet.Count);
        }

        public static void GetSFCode(List<Node> alphabet, int start, int end)
        {
            if (end - start <= 1) return;

            alphabet.Sort(); alphabet.Reverse();

            int mid = start;
            decimal sumStart = alphabet[start].Probability,
                    sumEnd = 0,
                    sum0 = 0,
                    sum1 = 0;

            for (int i = start + 1; i < end; i++)
                sumEnd += alphabet[i].Probability;

            while (sumStart + alphabet[mid].Probability <= sumEnd - alphabet[mid].Probability)
            {
                mid++;
                sumStart += alphabet[mid].Probability;
                sumEnd -= alphabet[mid].Probability;
            }

            for (int i = start; i < mid + 1; i++)
            {
                alphabet[i].SFCode += "0";
                sum0 += alphabet[i].Probability;
                Console.WriteLine($"{alphabet[i].Element}\t{alphabet[i].Probability:F4}\t{alphabet[i].SFCode}");
            }
            for (int i = mid + 1; i < end; i++)
            {
                alphabet[i].SFCode += "1";
                sum1 += alphabet[i].Probability;
                Console.WriteLine($"{alphabet[i].Element}\t{alphabet[i].Probability:F4}\t{alphabet[i].SFCode}");
            }

            Console.WriteLine($"\nstart = {start}\tmid = {mid}\tend = {end}\nsum0 = {sum0:F4}\tsum1 = {sum1:F4}\n");

            if (end - start == 2) return;

            GetSFCode(alphabet, start, mid + 1);
            GetSFCode(alphabet, mid + 1, end);
        }
    }
}
