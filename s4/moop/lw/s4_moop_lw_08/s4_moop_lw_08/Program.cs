using System;
using System.Collections.Generic;

namespace s4_moop_lw_08
{
    public static class Program
    {
        public static double F3(double x) => DefiniteIntegralsCalculator.F3(x); // (F3, 1.0, 3.0, e)
        public static double F6(double x) => DefiniteIntegralsCalculator.F6(x); // (F6, 0.1, 1.0, e)
        public static double F8(double x) => DefiniteIntegralsCalculator.F8(x); // (F8, 0.5, 2.0, e)

        public static string TestDIC(DefiniteIntegralsCalculator.Function f, double a, double b, double e = 0.0001)
        {
            return $"{DefiniteIntegralsCalculator.RectangleMethod(f, a, b, e)}\n" +
                   $"{DefiniteIntegralsCalculator.TrapezoidMethod(f, a, b, e)}\n" +
                   $"{DefiniteIntegralsCalculator.SimpsonMethod(f, a, b, e)}\n";
        }

        public static void Main(string[] args)
        {
            Console.WriteLine(TestDIC(F3, 1.0, 3.0));
            Console.WriteLine(TestDIC(F6, 0.1, 1.0));
            Console.WriteLine(TestDIC(F8, 0.5, 2.0));
            
            List<byte> bytes = new List<byte>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<short> shorts = new List<short>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<int> ints = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<long> longs = new List<long>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<float> floats = new List<float>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<double> doubles = new List<double>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            List<decimal> decimals = new List<decimal>() { 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            Console.WriteLine("\nmap test:");
            list.print(list.map(bytes, x => (byte)(x * x)));
            list.print(list.map(shorts, x => (short)(x * x)));
            list.print(list.map(ints, x => (x * x)));
            list.print(list.map(longs, x => (x * x)));
            list.print(list.map(floats, x => (x * x)));
            list.print(list.map(doubles, x => (x * x)));
            list.print(list.map(decimals, x => (x * x)));
            
            Console.WriteLine("\nfold test:");
            Console.WriteLine((list.fold(bytes, (x, y) => (byte)(x + y))));
            Console.WriteLine((list.fold(shorts, (x, y) => (short)(x + y))));
            Console.WriteLine((list.fold(ints, (x, y) => (x + y))));
            Console.WriteLine((list.fold(longs, (x, y) => (x + y))));
            Console.WriteLine((list.fold(floats, (x, y) => (x + y))));
            Console.WriteLine((list.fold(doubles, (x, y) => (x + y))));
            Console.WriteLine((list.fold(decimals, (x, y) => (x + y))));
        }
    }
}