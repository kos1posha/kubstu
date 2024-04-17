using System;
using System.Collections.Generic;
using System.Text;

namespace s3_kt_lw_02
{
    class BinaryTree : IComparable
    {
        public Node Data;
        public BinaryTree Left;
        public BinaryTree Right;

        public BinaryTree(decimal probability, string element, string haffmansCode, BinaryTree left, BinaryTree right)
        {
            Data = new Node(probability, element, haffmansCode);
            Left = left; Right = right;
        }
        public BinaryTree(decimal probability, string element, string haffmansCode)
        {
            Data = new Node(probability, element, haffmansCode);
        }
        public BinaryTree(Node data, BinaryTree left, BinaryTree right)
        {
            Data = data;
            Left = left; Right = right;
        }
        public BinaryTree(Node data)
        {
            Data = data;
        }

        public static BinaryTree operator +(BinaryTree operand1, BinaryTree operand2)
        {
            return new BinaryTree(operand1.Data.Probability + operand2.Data.Probability, operand1.Data.Element + operand2.Data.Element, "", operand1, operand2);
        }

        public int CompareTo(object o)
        {
            if (o is BinaryTree tree) return Data.CompareTo(tree.Data);
            else throw new Exception("error");
        }
    }
}
