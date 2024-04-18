using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s3_kt_cw
{
    public class SFNode : IComparable
    {
        public char Element;
        public int Probability;
        public string SFCode = string.Empty;

        public SFNode(char element, string sfCode)
        {
            Element = element;
            SFCode = sfCode;
        }
        public SFNode(char element, int probability)
        {
            Element = element;
            Probability = probability;
        }

        public string ElementInEncode(Encoding encoding) => Convert.ToString(encoding.GetBytes(Element.ToString())[0], 2);

        public int CompareTo(object o)
        {
            if (o is SFNode node) return Probability.CompareTo(node.Probability);
            else throw new Exception();
        }
        public override string ToString() => $"('{Element}'; {Probability}) - {SFCode}";
    }
}
