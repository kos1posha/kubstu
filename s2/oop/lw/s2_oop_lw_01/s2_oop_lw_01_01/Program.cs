using System;

namespace s2_oop_lw_01_01
{
    class Program
    {
        static void Main(string[] args)
        {
            Buyer vova = new Buyer("Влад", 19, "М", "pro100vlad", "123123123");
            Buyer.Show(vova);
        }
    }
}
