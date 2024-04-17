using System;
using System.Collections.Generic;
using System.Linq;

namespace s4_moop_lw_08
{
    public static class list
    {
        public delegate T fx<T>(T x);

        public delegate T fxy<T>(T x, T y);

        public static IEnumerable<T> map<T>(IEnumerable<T> xs, fx<T> f)
        {
            foreach (T x in xs)
                yield return f(x);
        }

        public static T fold<T>(IEnumerable<T> xs, fxy<T> f, T primary = default(T))
        {
            foreach (T x in xs)
                primary = f(primary, x);

            return primary;
        }

        public static void print<T>(IEnumerable<T> enumerable) => 
            Console.WriteLine($"[{string.Join(", ", enumerable)}]");
    }
}