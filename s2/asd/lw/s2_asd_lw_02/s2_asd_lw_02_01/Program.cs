using System;

namespace s2_asd_lw_02_01
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] a = new int[10] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            AltList b = new AltList(a);
            b.Add(10);
            b.Show();
            Console.WriteLine("-");
            b.Remove();
            b.Show();
            Console.WriteLine("-");
            b.AddTo(10, 5);
            b.Show();
            Console.WriteLine("-");
            b.RemoveTo(5);
            b.Show();
        }
    }
}
