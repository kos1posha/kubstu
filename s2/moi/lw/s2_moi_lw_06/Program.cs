using System;

namespace s2_moi_lw_06
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Введите первый байт: ");
            byte b1 = Convert.ToByte(Console.ReadLine(), 2);
            Console.Write("Введите второй байт: ");
            byte b2 = Convert.ToByte(Console.ReadLine(), 2);
            byte b2_dop = (byte)(~b2 + 1);
            Console.WriteLine($"Их разность: {Convert.ToString((byte)(b1 + b2_dop), 2)}");
        }
    }
}
