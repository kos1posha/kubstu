using System;

namespace s4_moop_lw_08
{
    public static class DefiniteIntegralsCalculator
    {
        public enum NumericalIntegration
        {
            RectangleMethod,
            TrapezoidMethod,
            SimpsonsMethod
        }

        public delegate double Function(double x);

        public static double F3(double x) => (1 - Math.Exp(0.7 / x)) / (x + 2);
        public static double F6(double x) => Math.Log(1 + x) / x;
        public static double F8(double x) => 1 / (Math.Sqrt(x) * (Math.Exp(0.9 * x) + 3));

        static double RungeAccuracyCheck(double Ih, double I2h, NumericalIntegration niMethod)
        {
            switch (niMethod)
            {
                case NumericalIntegration.RectangleMethod:
                case NumericalIntegration.TrapezoidMethod:
                    return Math.Abs(Ih - I2h) / 3;
                case NumericalIntegration.SimpsonsMethod:
                    return Math.Abs(Ih - I2h) / 15;
                default:
                    throw new Exception("Как ты сюда попал вообще?");
            }
        }
        static double RAC(double Ih, double I2h, NumericalIntegration niMethod) => RungeAccuracyCheck(Ih, I2h, niMethod);

        static void ArgumentCheck(double a, double b, double e)
        {
            if (a >= b) throw new ArgumentException($"Верхний предел (b: {b}) должен быть строго больше нижнего предела (a: {a})");
            if (e >= 1) throw new ArgumentException($"Точность (e: {e}) должна быть строго меньше 1");
        }
        
        public static double RectangleMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            double result = 0,
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.RectangleMethod) > e; h *= 0.5)
            {
                old = result;
                result = 0;

                for (double x = a + h; x < b; x += h)
                    result += f(x);

                result *= h;
            }
            return result;
        }
        
        public static double TrapezoidMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            double edges = (f(a) + f(b)) * 0.5, 
                   result = edges, 
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.TrapezoidMethod) > e; h *= 0.5)
            {
                old = result;
                result = edges;
                for (double x = a + h; x < b; x += h)
                    result += f(x);
                result *= h;
            }
            return result;
        }

        public static double SimpsonMethod(Function f, double a, double b, double e = 0.0001)
        {
            ArgumentCheck(a, b, e);
            double edges = f(a) + f(b), 
                   result = edges, 
                   old = double.MaxValue;
            for (double h = (b - a) * 0.5; RAC(result, old, NumericalIntegration.SimpsonsMethod) > e; h *= 0.5)
            {
                old = result;
                double odds = 0, evens = 0;
                bool isOdd = true;
                for (double x = a + h; x < b; x += h)
                {
                    if (isOdd) odds += f(x);
                    else evens += f(x);
                    isOdd = !isOdd;
                }
                result = (edges + 4 * odds + 2 * evens) * h/3;
            }
            return result;
        }
    }
}