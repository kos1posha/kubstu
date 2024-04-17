using System;

namespace s5_tpo_lw_01_01
{
    public class Program
    {
        private static int Sqr(int x)
        {                                                           //10
            int q = x * x;                                          //11
            return q;                                               //12
        }                                                           //13

        private static void Main()
        {                                                           //0
            const int n = 10;                                       //1
            int[] a = { 5, 2, 7, -9, 4, 8, -1, 0, 3, 6 };           //2
            //Найдем сумму квадратов                                //3
            //положительных элементов массива                       //4
            int s = 0;                                              //5
            for (int i = 0; i < n; i++)                             //6
                if (a[i] > 0) s += Sqr(a[i]);                       //7
            Console.WriteLine("Сумма квадратов равна: {0}", s);     //8
        }                                                           //9
    }
}