using System;
using System.Diagnostics;
using System.Linq;

namespace s5_tpo_lw_02
{
    public static class Program
    {
        public static byte ArithmeticProgressionSum(byte a, byte d, byte n)
        {
            byte result = a;
            for (byte i = 1, old = a; i < n; i++)
            {
                try { checked { result += old += d; } }
                catch (OverflowException e) { Debug.Assert(false, e.Message); return 0; }
            }
            return result;
        }

        public static void Main(string[] args)
        {
            foreach (int step in new [] {1, 7, 3, 5, 9})
                DefiniteIntegralsCalculator.DebuggedSteps.Add(step);
            
            foreach (int step in new [] {1, 2, 3, 4})
                DefiniteIntegralsCalculator.TracedSteps.Add(step);
            
            Console.WriteLine(DefiniteIntegralsCalculator.TrapezoidMethod(DefiniteIntegralsCalculator.F3, 1, 3));
            Console.WriteLine(DefiniteIntegralsCalculator.TrapezoidMethod(DefiniteIntegralsCalculator.F6, 0.1, 1));
            Console.WriteLine(DefiniteIntegralsCalculator.TrapezoidMethod(DefiniteIntegralsCalculator.F8, 0.5, 2));
            Console.WriteLine(DefiniteIntegralsCalculator.RectangleMethod(DefiniteIntegralsCalculator.F3, 1, 3));
            Console.WriteLine(DefiniteIntegralsCalculator.RectangleMethod(DefiniteIntegralsCalculator.F6, 0.1, 1));
            Console.WriteLine(DefiniteIntegralsCalculator.RectangleMethod(DefiniteIntegralsCalculator.F8, 0.5, 2));
            Console.WriteLine(DefiniteIntegralsCalculator.SimpsonMethod(DefiniteIntegralsCalculator.F3, 1, 3));
            Console.WriteLine(DefiniteIntegralsCalculator.SimpsonMethod(DefiniteIntegralsCalculator.F6, 0.1, 1));
            Console.WriteLine(DefiniteIntegralsCalculator.SimpsonMethod(DefiniteIntegralsCalculator.F8, 0.5, 2));
        }
    }
}