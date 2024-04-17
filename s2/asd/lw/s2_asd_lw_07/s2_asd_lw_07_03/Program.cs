using System;

namespace s2_asd_lw_07_03
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] A = new int[] { 234, 2347, 321, 32, 1, 3, 4347, 47, 22, 312, 631, 23, 71 };
            int[] B = new int[A.Length];

            for (int i = 0; i < B.Length; i++)
            {
                int minA = i;
                for (int j = i; j < A.Length; j++)
                {
                    if (A[j] < A[minA])
                        minA = j;
                }
                B[i] = A[minA];
                (A[i], A[minA]) = (A[minA], A[i]);
            }

            foreach (int item in B) Console.WriteLine(item);
        }
    }
}