using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace s2_oop_lw_02
{
    public class Phone
    {
        public static List<Phone> Data = new List<Phone>()
        {
            new Phone("Smasung", "A40", 284, true),
            new Phone("Pineaplle", "bPhone XS", 23, false),
            new Phone("Xlomy", "Note 10 Pro", 893, true),
            new Phone("Yeskia", "C20", 117, false),
            new Phone("Слава", "Бизяев", 1, false)
        };
        string Firm;
        string Model;
        int Quantity;
        bool SecondHand;
        public Phone(string firm, string model, int quantity, bool secondHand)
        {
            Firm = firm;
            Model = model;
            Quantity = quantity;
            SecondHand = secondHand;
        }
        public static string ShowData()
        {
            string output = null;
            for (int i = 0; i < Data.Count; i++)
            {
                output += $"{i + 1}) {Data[i].Firm} {Data[i].Model} / {Data[i].Quantity} / {Data[i].SecondHand}" + Environment.NewLine;
            }
            return output;
        }
    }
}
