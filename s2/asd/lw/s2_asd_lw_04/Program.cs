using System;

namespace s2_asd_lw_04
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryTree btTest = new BinaryTree(new int?[] { -6, -3, 1, -4, -5, -8, -7, -9 });
            btTest.Show();
            Console.WriteLine();
            btTest.DelNegLeafs();
            btTest.Show();
            Console.WriteLine();
            btTest.DelNegLeafs();
            btTest.Show();
        }
    }
}
