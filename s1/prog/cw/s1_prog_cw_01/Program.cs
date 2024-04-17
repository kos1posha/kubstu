using System;

namespace s1_prog_cw_01
{
    class Program
    {
        private static double Accuracy { get; set; }
        // Следующий метод используется для вводов с клавиатуры необходимых данных
        public static void DataInput(ref double firstX, ref double lastX, ref double step, ref double accuracy)
        {
            Console.WriteLine("!!!: - Начальный аргумент должен быть меньше конечного\n" +
                              "     - Шаг не может быть отрицательным или равен нулю\n" +
                              "     - Количество знаков после запятой (точность) не может быть отрицательным\n");
        Uncorrect_1:
        Error_1:
            try
            {
                Console.Write("Введите начальный аргумент: ");
                firstX = Convert.ToDouble(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine($"Некорректный формат ввода. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Error_1;
            }
        Error_2:
            try
            {
                Console.Write("Введите конечный аргумент: ");
                lastX = Convert.ToDouble(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine($"Некорректный формат ввода. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Error_2;
            }
            if (firstX > lastX)
            {
                Console.WriteLine("Начальный аргумент должен быть меньше конечного. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Uncorrect_1;
            }
        Uncorrect_2:
        Error_3:
            try
            {
                Console.Write("Введите шаг: ");
                step = Convert.ToDouble(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine($"Некорректный формат ввода. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Error_3;
            }
            if (step <= 0)
            {
                Console.WriteLine("Шаг не может быть отрицательным или равен нулю. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Uncorrect_2;
            }
        Uncorrect_3:
        Error_4:
            try
            {
                Console.Write("Введите точность (количество знаков после запятой): ");
                accuracy = Math.Pow(10, -Convert.ToInt32(Console.ReadLine()));
                Accuracy = accuracy;
            }
            catch
            {
                Console.WriteLine($"Некорректный формат ввода. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Error_4;
            }
            if (accuracy > 1)
            {
                Console.WriteLine("Количество знаков после запятой не может быть отрицательным. Нажмите любую клавишу, чтобы повторить ввод.");
                Console.ReadKey(true);
                goto Uncorrect_3;
            }
        }
        // Следующий метод используется для вывода на экран таблицы посчитанных значений
        public static void ShowTable(double firstX, double lastX, double step)
        {
            static string Field(string a, string b, string c, string d) => String.Format("|{0,6}|{1,24}|{2,24}|{3,9}|", a, b, c, d);
            string frame = "+------+------------------------+------------------------+---------+";
            Console.WriteLine($"{frame}\n{Field("x", "e^x", "Math.Exp(x)", "count")}\n{frame}");
            for (double x = firstX; x <= lastX; x = Math.Round(x + step, 5))
            {
                Console.WriteLine($"{Field($"{x}", $"{Exp(x).Exponent}", $"{Math.Exp(x)}", $"{Exp(x).Count}")}\n{frame}");
            }
        }
        // Следующий метод создан для подсчета экспоненты. Возвращает экземпляр класса Mode
        public static Node Exp(double x)
        {
            int count = 0;
            double plus = 1, factorial = 1, exponent = 1;
            for (int n = 1; Math.Abs(plus) > Accuracy; n++, count++)
            {
                factorial *= n;
                plus = Math.Pow(x, n) / factorial;
                exponent += plus;
            }
            return new Node(exponent, count);
        }
        static void Main(string[] args)
        {
            double firstX = 0, lastX = 0, step = 0, accuracy = 0;

            DataInput(ref firstX, ref lastX, ref step, ref accuracy);

            Console.Clear();
            Console.WriteLine($"Начальный аргумент = {firstX}\nКонечный аргумент = {lastX}\nШаг = {step}\nТочность = {accuracy}");

            ShowTable(firstX, lastX, step);
        }
    }
}
