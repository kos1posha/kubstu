using System;
using System.Collections.Generic;
using System.Text;

namespace s3_kt_lw_02
{
    static class HaffmansAlgorithm
    {
        public static List<decimal> ProbabilityGenerator(string alphabet)
        {
            List<decimal> pList = new List<decimal>();
            Random random = new Random();
            int probability = 10000;

            for (int i = 0, j = 4; i < alphabet.Length - 1; i++)
            {
                if (i % 8 == 0) j++;
                int currentProbability = random.Next(1, probability / j);
                pList.Add(currentProbability / 10000.0m);
                probability -= currentProbability;
            }
            pList.Add(probability / 10000.0m);

            return pList;
        }

        public static List<Node> GetHaffmansCode(List<Node> alphabet)
            => GetHaffmansCode(GetHaffmansTree(alphabet));
        public static List<Node> GetHaffmansCode(BinaryTree alphabetTree) => HaffmansTreeTraversal(alphabetTree);

        public static List<Node> HaffmansTreeTraversal(BinaryTree alphabetTree) => HaffmansTreeTraversal(alphabetTree, "", new List<Node>());
        public static List<Node> HaffmansTreeTraversal(BinaryTree alphabetTree, string haffmansCode, List<Node> haffmansCodes)
        {
            if (alphabetTree.Left != null)
                HaffmansTreeTraversal(alphabetTree.Left, haffmansCode + "0", haffmansCodes);
            if (alphabetTree.Right != null)
                HaffmansTreeTraversal(alphabetTree.Right, haffmansCode + "1", haffmansCodes);
            if (alphabetTree.Left == null && alphabetTree.Right == null)
                haffmansCodes.Add(new Node(alphabetTree.Data.Probability, alphabetTree.Data.Element, haffmansCode));
            return haffmansCodes;
        }

        public static BinaryTree GetHaffmansTree(List<Node> alphabet)
        {
            List<BinaryTree> alphabetTree = new List<BinaryTree>();
            foreach (Node item in alphabet) alphabetTree.Add(new BinaryTree(item));
            return GetHaffmansTree(alphabetTree);
        }

        public static BinaryTree GetHaffmansTree(List<BinaryTree> alphabet)
        {
            if (alphabet.Count == 1) return alphabet[0];

            alphabet.Sort();
            alphabet.Add(alphabet[0] + alphabet[1]);
            alphabet.RemoveRange(0, 2);
            alphabet.Sort();

            return GetHaffmansTree(alphabet);
        }
    }
}
