using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_09
{
    [Serializable]
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
        public EngVerb(string allForms)
        {
            string[] convert = allForms.Trim().Split(' ');
            if (convert.Length != 3) new Exception("Uncorrect format.");
            FirstForm = convert[0];
            SecondForm = convert[1];
            ThirdForm = convert[2];
        }
        public int CompareTo(object item)
        {
            if (item is EngVerb engVerb) return FirstForm.CompareTo(engVerb.FirstForm);
            else throw new Exception();
        }
        public override string ToString()
        {
            return $"{FirstForm} {SecondForm} {ThirdForm}";
        }
    }
}
