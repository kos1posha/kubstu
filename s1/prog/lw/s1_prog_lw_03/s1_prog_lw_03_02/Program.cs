using System;

namespace s1_prog_lw_03_02
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("R = ");
            double R = Convert.ToDouble(Console.ReadLine());
            int ppd = 0;
            int prm = 0;
            for (int k = 0; k < 10; k++)
            {
                Console.Write("x = ");
                double x = Convert.ToDouble(Console.ReadLine());
                Console.Write("y = ");
                double y = Convert.ToDouble(Console.ReadLine());
                if (((x <= R) && (x >= -R)) && ((y <= R) && (y >= -R)))
                {
                    if ((x == 0) || (y == 0))
                    { Console.WriteLine("Попадание"); ppd++; }
                    if ((x > 0) && (y > 0))
                    { Console.WriteLine("Попадание"); ppd++; }
                    if ((x < 0) && (y < 0))
                    { Console.WriteLine("Попадание"); ppd++; }
                    if ((x > 0) && (y < 0))
                    {
                        if ((Math.Pow(x - R, 2) + Math.Pow(y + R, 2)) >= Math.Pow(R, 2))
                        { Console.WriteLine("Попадание"); ppd++; }
                        else
                        { Console.WriteLine("Промах"); prm++; };
                    }
                    if ((x < 0) && (y > 0))
                    {
                        if ((Math.Pow(x + R, 2) + Math.Pow(y - R, 2)) >= Math.Pow(R, 2))
                        { Console.WriteLine("Попадание"); ppd++; }
                        else
                        { Console.WriteLine("Промах"); prm++; };
                    }
                }
                else { Console.WriteLine("Промах"); prm++; };
            }
            Console.WriteLine($"Попадания = {ppd}          Промахи = {prm}", ppd, prm);
        }
    }
}
