using System;
using System.Collections.Generic;
using System.Text;

namespace s3_kt_lw_02
{
    class Node : IComparable
    {
        public decimal Probability;
        public string Element;
        public string HaffmansCode;
        public Node(decimal probability, string element, string haffmansCode)
        {
            Probability = probability;
            Element = element;
            HaffmansCode = haffmansCode;
        }
        public static Node operator +(Node node1, Node node2)
        {
            return new Node(node1.Probability + node2.Probability, node1.Element + node2.Element, "");
        }
        public int CompareTo(object o)
        {
            if (o is Node node) return Probability.CompareTo(node.Probability);
            else throw new Exception("error");
        }
    }
}
