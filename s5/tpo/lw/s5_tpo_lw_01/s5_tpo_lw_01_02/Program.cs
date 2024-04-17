using System;


namespace s5_tpo_lw_01_02
{
    class Program
    {
        //Метод, считающий сумму элементов массива
        private static int Sum(int[] x, int n)
        {                                                           //31
            int s = 0;                                              //32
            for (int i = 0; i < n; i++)                             //33
                s += x[i];                                          //34
            return s;                                               //35
        }                                                           //36

        //Метод для ввода целых чисел с клавиатуры
        private static int ReadInt(string prompt)
        {                                                           //37
            Console.Write(prompt);                                  //38
            int x = int.Parse(Console.ReadLine() ?? string.Empty);  //39
            return x;                                               //40
        }                                                           //41

        private static void Main()
        {                                                           //0
            const int n = 10;                                       //1
            int[] a = { 1, 3, -5, 0, 4, 6, -1, 9, 3, 2 };           //2
            //Найдем максимальный элемент массива                   //3
            int m = a[0];                                           //4
            for (int i = 1; i < n; i++)                             //5
                if (m < a[i])                                       //6
                    m = a[i];                                       //7
            Console.WriteLine(m);                                   //8
            //Найдем сумму элементов массива                        //9
            int s = Sum(a, n);                                      //10
            Console.WriteLine(s);                                   //11
            int z = s / m;                                          //12
            int k = 0;                                              //13
            for (int i = 0; i < n; i++)                             //14
                if (a[i] > z)                                       //15
                    k += a[i];                                      //16
                else                                                //17
                    k -= a[i];                                      //18
            Console.WriteLine(k);                                   //19
            int x = ReadInt("");                                    //20
            int y = ReadInt("");                                    //21
            s = 0;                                                  //22
            while (x != 0)                                          //23
            {                                                       //24
                x--;                                                //25
                y--;                                                //26
                s += x + y;                                         //27
            }                                                       //28
            Console.WriteLine(s);                                   //29
        }                                                           //30
    }
}