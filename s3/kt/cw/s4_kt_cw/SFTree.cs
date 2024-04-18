using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s3_kt_cw
{
    public class SFTree
    {
        public readonly List<SFNode> Data;
        public SFTree Left { get; private set; }
        public SFTree Right { get; private set; }
        public int GeneralProbability
        {
            get
            {
                int value = 0;
                foreach (SFNode node in Data)
                    value += node.Probability;
                return value;
            }
        }

        public bool GetIsLeaf() => Data.Count <= 1;

        public bool IsRoot { get; private set; }

        SFTree()
        {
            Data = new List<SFNode>();
            IsRoot = false;
        }
        public SFTree(string text, SplitPrinciple splitPrinciple)
        {
            Data = GetProbabilityAlphabet(text);
            IsRoot = true;
            UpdateBranches(splitPrinciple);
        }

        void UpdateBranches(SplitPrinciple splitPrinciple)
        {
            if (GetIsLeaf() && !IsRoot) return;

            Data.Sort(); Data.Reverse();

            SplitTree(splitPrinciple);

            Left.AppendChar(0).UpdateBranches(splitPrinciple);
            Right.AppendChar(1).UpdateBranches(splitPrinciple);
        }
        void SplitTree(SplitPrinciple splitPrinciple)
        {
            Left = new SFTree();
            Right = new SFTree();

            switch (splitPrinciple)
            {
                case (SplitPrinciple.Full):
                    {
                        int i = 0;

                        while (i < Data.Count && Left.GeneralProbability < GeneralProbability / 2)
                            Left.Data.Add(Data[i++]);
                        while (i < Data.Count)
                            Right.Data.Add(Data[i++]);

                        break;
                    }
                case (SplitPrinciple.Partially):
                    {
                        Left.Data.Add(Data[0]);
                        bool side = true;

                        for (int i = 1; i < Data.Count; side = !side)
                            if (side)
                                while (Left.GeneralProbability >= Right.GeneralProbability)
                                    try { Right.Data.Add(Data[i++]); }
                                    catch { break; }
                            else
                                while (Left.GeneralProbability < Right.GeneralProbability)
                                    try { Left.Data.Add(Data[i++]); }
                                    catch { break; }

                        break;
                    }
            }
        }
        SFTree AppendChar(byte number)
        {
            foreach (SFNode node in Data)
                node.SFCode += number.ToString();

            return this;
        }
        public string GetEncodedAlphabet()
        {
            string result = string.Empty;

            foreach (SFNode node in Data)
                result += $"{Convert.ToString((short)node.Element, 2)} {node.SFCode} ";

            return $"{result}";
        }
        public static List<SFNode> GetProbabilityAlphabet(string text)
        {
            List<SFNode> alphabet = new List<SFNode>();

            foreach (char symbol in text)
            {
                foreach (SFNode node in alphabet)
                    if (node.Element == symbol)
                    {
                        node.Probability += 1;
                        goto isOld;
                    }
                alphabet.Add(new SFNode(symbol, 1));
            isOld:;
            }

            return alphabet;
        }
    }
}
