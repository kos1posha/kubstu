using System;
using System.Collections.Generic;
using System.Diagnostics;


namespace s5_tpo_lw_02
{
    public static class DefiniteIntegralsCalculator
    {
        public static readonly SortedSet<int> DebuggedSteps = new SortedSet<int>();
        public static readonly SortedSet<int> TracedSteps = new SortedSet<int>();

        public enum NumericalIntegration
        {
            RectangleMethod,
            TrapezoidMethod,
            SimpsonsMethod,
            NotImplementedMethod
        }

        public delegate double Function(double x);
        public delegate double NumericalIntegrationMethod(Function f, double a, double b, double e = 0.0001);
        
        public static double F3(double x) => (1 - Math.Exp(0.7 / x)) / (x + 2);
        public static double F6(double x) => Math.Log(1 + x) / x;
        public static double F8(double x) => 1 / (Math.Sqrt(x) * (Math.Exp(0.9 * x) + 3));

        public static double RungeAccuracyCheck(double Ih, double I2h, NumericalIntegration method)
        {
            switch (method)
            {
                case NumericalIntegration.RectangleMethod:
                case NumericalIntegration.TrapezoidMethod:
                    return Math.Abs(Ih - I2h) / 3;
                case NumericalIntegration.SimpsonsMethod:
                    return Math.Abs(Ih - I2h) / 15;
                default:
                    throw new NotImplementedException("Реализация данного метода отсутствует.");
            }
        }
        static double RAC(double Ih, double I2h, NumericalIntegration method) => RungeAccuracyCheck(Ih, I2h, method);

        static void ArgumentCheck(double a, double b, double e)
        {
            if (a >= b) throw new ArgumentException($"Верхний предел (b: {b}) должен быть строго больше нижнего предела (a: {a})");
            if (e <= 0 || e >= 1) throw new ArgumentException($"Точность (e: {e}) должна быть строго больше 0 и строго меньше 1");
        }

        public static double RectangleMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            Stack<int> debuggedSteps = new Stack<int>(DebuggedSteps.Reverse());
            Stack<int> tracedSteps = new Stack<int>(TracedSteps.Reverse());
            int step = 0;
            double result = 0,
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.RectangleMethod) > e; h *= 0.5, step++)
            {
                old = result;
                result = 0;
                for (double x = a + h; x < b; x += h)
                {
                    Debug.Assert(x > a && x < b);
                    result += f(x);
                }
                result *= h;
                _debug(debuggedSteps, step, result);
                _trace(tracedSteps, step, result);
            }
            return result;
        }

        public static double TrapezoidMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            Stack<int> debuggedSteps = new Stack<int>(DebuggedSteps.Reverse());
            Stack<int> tracedSteps = new Stack<int>(TracedSteps.Reverse());
            int step = 0;
            double edges = (f(a) + f(b)) * 0.5, 
                   result = edges, 
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.TrapezoidMethod) > e; h *= 0.5, step++)
            {
                old = result;
                result = edges;
                for (double x = a + h; x < b; x += h)
                {
                    Debug.Assert(x > a && x < b);
                    result += f(x);
                }
                result *= h;
                _debug(debuggedSteps, step, result);
                _trace(tracedSteps, step, result);
            }
            return result;
        }

        public static double SimpsonMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            Stack<int> debuggedSteps = new Stack<int>(DebuggedSteps.Reverse());
            Stack<int> tracedSteps = new Stack<int>(TracedSteps.Reverse());
            int step = 0;
            double edges = f(a) + f(b), 
                   result = edges, 
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.SimpsonsMethod) > e; h *= 0.5, step++)
            {
                old = result;
                double odds = 0, evens = 0;
                bool isOdd = true;
                for (double x = a + h; x < b; x += h)
                {
                    Debug.Assert(x > a && x < b);
                    if (isOdd) odds += f(x);
                    else evens += f(x);
                    isOdd = !isOdd;
                }
                result = (edges + 4 * odds + 2 * evens) * h/3;
                _debug(debuggedSteps, step, result);
                _trace(tracedSteps, step, result);
            }
            return result;
        }
        
        private static void _debug(Stack<int> debuggedSteps, int step, double result)
        {
            if (debuggedSteps.Count == 0) return;
            if (step == debuggedSteps.Peek())
                Debug.WriteLine($"[Debug] Step {debuggedSteps.Pop()}: {result}");
        }
        
        private static void _trace(Stack<int> tracedSteps, int step, double result)
        {
            if (tracedSteps.Count == 0) return;
            if (step == tracedSteps.Peek())
                Trace.WriteLine($"[Trace] Step {tracedSteps.Pop()}: {result}");
        }
    }
}