using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_08
{
    public struct EngVerb : IComparable
    {
        public string FirstForm;
        public string SecondForm;
        public string ThirdForm;
        public EngVerb(string firstForm, string secondForm, string thirdForm)
        {
            FirstForm = firstForm;
            SecondForm = secondForm;
            ThirdForm = thirdForm;
        }
        public int CompareTo(object item)
        {
            if (item is EngVerb engVerb) return FirstForm.CompareTo(engVerb.FirstForm);
            else throw new Exception();
        }
    }
}
