using System;
using NUnit.Framework;
using s4_moop_lw_08;

namespace s4_moop_lw_08_test
{
    [TestFixture]
    public static class DefiniteIntegralsCalculatorTest
    {
        public static double E1 = 0.001;
        public static double E2 = 0.00001;
        public static double E3 = 0.0000001;
        
        public static double F3(double x) => DefiniteIntegralsCalculator.F3(x); // (F3, 1.0, 3.0, E)
        public static double F6(double x) => DefiniteIntegralsCalculator.F6(x); // (F6, 0.1, 1.0, E)
        public static double F8(double x) => DefiniteIntegralsCalculator.F8(x); // (F8, 0.5, 2.0, E)
                 
        public static double F3Result = -0.259843140385733;
        public static double F6Result = 0.7248617981947916;
        public static double F8Result = 0.2413467645464059;

        public static string HardRound(double number, int digits) => number.ToString().Remove(digits);
        
        [Test]
        public static void RectangleMethodWithF3()
        {
            double actualE1 = DefiniteIntegralsCalculator.RectangleMethod(F3, 1.0, 3.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.RectangleMethod(F3, 1.0, 3.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.RectangleMethod(F3, 1.0, 3.0, E3);

            string[] expected = { HardRound(F3Result, 3), HardRound(F3Result, 5), HardRound(F3Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void RectangleMethodWithF6()
        {
            double actualE1 = DefiniteIntegralsCalculator.RectangleMethod(F6, 0.1, 1.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.RectangleMethod(F6, 0.1, 1.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.RectangleMethod(F6, 0.1, 1.0, E3);

            string[] expected = { HardRound(F6Result, 3), HardRound(F6Result, 5), HardRound(F6Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void RectangleMethodWithF8()
        {
            double actualE1 = DefiniteIntegralsCalculator.RectangleMethod(F8, 0.5, 2.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.RectangleMethod(F8, 0.5, 2.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.RectangleMethod(F8, 0.5, 2.0, E3);

            string[] expected = { HardRound(F8Result, 3), HardRound(F8Result, 5), HardRound(F8Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void TrapezoidMethodWithF3()
        {
            double actualE1 = DefiniteIntegralsCalculator.TrapezoidMethod(F3, 1.0, 3.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.TrapezoidMethod(F3, 1.0, 3.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.TrapezoidMethod(F3, 1.0, 3.0, E3);

            string[] expected = { HardRound(F3Result, 3), HardRound(F3Result, 5), HardRound(F3Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void TrapezoidMethodWithF6()
        {
            double actualE1 = DefiniteIntegralsCalculator.TrapezoidMethod(F6, 0.1, 1.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.TrapezoidMethod(F6, 0.1, 1.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.TrapezoidMethod(F6, 0.1, 1.0, E3);

            string[] expected = { HardRound(F6Result, 3), HardRound(F6Result, 5), HardRound(F6Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void TrapezoidMethodWithF8()
        {
            double actualE1 = DefiniteIntegralsCalculator.TrapezoidMethod(F8, 0.5, 2.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.TrapezoidMethod(F8, 0.5, 2.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.TrapezoidMethod(F8, 0.5, 2.0, E3);

            string[] expected = { HardRound(F8Result, 3), HardRound(F8Result, 5), HardRound(F8Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public static void SimpsonMethodWithF3()
        {
            double actualE1 = DefiniteIntegralsCalculator.SimpsonMethod(F3, 1.0, 3.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.SimpsonMethod(F3, 1.0, 3.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.SimpsonMethod(F3, 1.0, 3.0, E3);

            string[] expected = { HardRound(F3Result, 3), HardRound(F3Result, 5), HardRound(F3Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void SimpsonMethodWithF6()
        {
            double actualE1 = DefiniteIntegralsCalculator.SimpsonMethod(F6, 0.1, 1.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.SimpsonMethod(F6, 0.1, 1.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.SimpsonMethod(F6, 0.1, 1.0, E3);

            string[] expected = { HardRound(F6Result, 3), HardRound(F6Result, 5), HardRound(F6Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void SimpsonMethodWithF8()
        {
            double actualE1 = DefiniteIntegralsCalculator.SimpsonMethod(F8, 0.5, 2.0, E1);
            double actualE2 = DefiniteIntegralsCalculator.SimpsonMethod(F8, 0.5, 2.0, E2);
            double actualE3 = DefiniteIntegralsCalculator.SimpsonMethod(F8, 0.5, 2.0, E3);

            string[] expected = { HardRound(F8Result, 3), HardRound(F8Result, 5), HardRound(F8Result, 7) };
            string[] actual = { HardRound(actualE1, 3), HardRound(actualE2, 5), HardRound(actualE3, 7) };
            
            Assert.AreEqual(expected, actual);
        }
    }
}