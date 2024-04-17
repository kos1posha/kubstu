using System;

namespace s2_oml_lw_09
{
    class Program
    {
        public static double Mul(double x, double y)
        {
            if (y == 0) return 0;
            return x + Mul(x, y - 1);
        }
        public static double Power(int x, int y)
        {
            if (y <= 0) return 1;
            return Mul(x, Power(x, y - 1));
        }
        public static double Dec(int y)
        {
            if (y <= 0) return 0;
            return Dec(y - 1);
        }
        public static double Sub(int x, int y)
        {
            if (x < y) return 0;
            return x - y;
        }
        public static double Sgn(int y)
        {
            if (y > 0) return 1;
            if (y < 0) return -1;
            return 0;
        }
        public static double F(int x, int y)
        {
            if (x > y) return x - y;
            else return y - x;
        }
        public static double Equal(double x, double y)
        {
            if (x == y) return 1;
            return 0;
        }
        public static double Lower(double x, double y)
        {
            if (x < y) return x;
            return y;
        }
        public static double Greater(double x, double y)
        {
            if (x > y) return x;
            return y;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Mul(4, 9));
            Console.WriteLine(Power(2, 3));
            Console.WriteLine(Dec(8));
            Console.WriteLine(Sub(9, 2));
            Console.WriteLine(Sgn(-3));
            Console.WriteLine(F(4, 11));
            Console.WriteLine(Equal(7, 7));
            Console.WriteLine(Lower(-2, 7));
            Console.WriteLine(Greater(-2, 7));
        }
    }
}
