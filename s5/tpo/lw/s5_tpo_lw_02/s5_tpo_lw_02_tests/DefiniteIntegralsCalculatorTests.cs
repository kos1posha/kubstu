using System;
using NUnit.Framework;
using static s5_tpo_lw_02.DefiniteIntegralsCalculator;

namespace s5_tpo_lw_02_tests
{
    [TestFixture]
    public class DefiniteIntegralsCalculatorTests
    {
        public NumericalIntegrationMethod[] testMethods = {
            RectangleMethod,
            TrapezoidMethod,
            SimpsonMethod
        };
        
        public (Function f, double a, double b, double expected)[] testData = {
            (F3, 1, 3, -0.259),
            (F6, 0.1, 1, 0.724),
            (F8, 0.5, 2, 0.241)
        };
        
        [Test]
        public void NumericalIntegrationMethods_Valid_Test()
        {
            DebuggedSteps.Add(1);
            TracedSteps.Add(1);
            
            foreach (NumericalIntegrationMethod method in testMethods)
            {
                _testMethod(method);
            }
        }
           
        [Test]
        public void NumericalIntegrationMethods_Exception_Test()
        {
            Assert.Throws<ArgumentException>(() => { RectangleMethod(F3, 3, 1); });
            Assert.Throws<ArgumentException>(() => { TrapezoidMethod(F6, 0.1, 1, e: -0.0001); });
            Assert.Throws<ArgumentException>(() => { SimpsonMethod(F8, 0.5, 2, e: 1.0001); });
            Assert.Throws<NotImplementedException>(() => { RungeAccuracyCheck(0.9, 1, NumericalIntegration.NotImplementedMethod); });
        }
        
        private void _testMethod(NumericalIntegrationMethod method)
        {
            foreach ((Function f, double a, double b, double expected) test in testData)
            {
                double res = method(test.f, test.a, test.b);
                bool assertCondition = res > 0 
                    ? test.expected < res && res < test.expected + 0.001
                    : test.expected > res && res > test.expected - 0.001;
                Assert.IsTrue(assertCondition);
            }
        }
    }
}