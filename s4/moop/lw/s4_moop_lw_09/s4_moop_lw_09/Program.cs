using System;

namespace s4_moop_lw_09
{
    internal static class Program
    {
        public static void Main(string[] args)
        {
            Branch<int> branch = new Branch<int>(10)
            {
                new Leaf<int>(1),
                new Branch<int>(2)
                {
                    new Branch<int>(21),
                    new Leaf<int>(22)
                },
                new Branch<int>(3),
                new Leaf<int>(4),
                new Branch<int>(5)
                {
                    new Leaf<int>(51),
                    new Branch<int>(52)
                    {
                        new Branch<int>(521)
                        {
                            new Branch<int>(5211)
                            {
                                new Leaf<int>(52111)
                            }
                        }
                    },
                    new Leaf<int>(53)
                },
                new Leaf<int>(6)
            };

            Console.WriteLine(branch);
        }
    }
}