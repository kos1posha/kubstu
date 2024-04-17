using System;
using System.Collections.Generic;
using System.Text;

namespace s3_kt_lw_01
{
    class Node : IComparable
    {
        public decimal Probability { get; }
        public char Element { get; set; }
        public string SFCode { get; set; }
        public Node(decimal probability, char element, string sfCode)
        {
            Probability = probability / SFAlgorithm.GeneralProbability;
            Element = element;
            SFCode = sfCode;
        }
        public int CompareTo(object o)
        {
            if (o is Node node) return Probability.CompareTo(node.Probability);
            else throw new Exception("error");
        }
    }
}
