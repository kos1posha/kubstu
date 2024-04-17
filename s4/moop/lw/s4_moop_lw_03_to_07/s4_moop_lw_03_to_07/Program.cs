using System;

namespace s4_moop_lw_03_to_07
{
internal class Program
{
    static void Continue()
    {
        Console.Write("Нажмите любую клавишу, чтобы продолжить.");
        Console.ReadKey(true);
    }
    
    static void _invalidInput()
    {
        Console.Clear();
        Console.Write("Неверный  ввод.\nНажмите любую клавишу, чтобы повторить попытку.");
        Console.ReadKey(true);
        Console.Clear();
    }

    static int InvalidInput()
    {
        _invalidInput();
        return InputDequeType();
    }
    
    static void InvalidInput<T>(Deque<T> deque, string type)
    {
        _invalidInput();
        StartProgram(deque, type);
    }
    
    static void InvalidInput<T>(Deque<T> deque, string type, int cratch)
    {
        _invalidInput();
        switch (cratch)
        {
            case 1: PushFront(deque, type); break;
            case 2: PushBack(deque, type); break;
        }
    }
    
    static int InputDequeType()
    {
        Console.Write("Выберите тип дека.\n" +
                      "1) char\n" +
                      "2) string\n" +
                      "3) integer\n" +
                      "4) double\n" +
                      "5) boolean\n\n" +
                      "Ввод: ");
        int input = Convert.ToInt32(Console.ReadLine());
        if (input < 1 || input > 5) return InvalidInput();
        else return input;
    }

    static void StartProgram<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        Console.Write($"Текущий дек ({type}): {deque}\n\n" +
                      "Выберите действие.\n" +
                      "1) Добавить в начало.\n" +
                      "2) Добавить в конец.\n" +
                      "3) Извлечь из начала.\n" +
                      "4) Извлечь из конца.\n" +
                      "5) Очистить.\n\n" +
                      "Ввод: ");
        switch (Console.ReadLine())
        {
            case "1": PushFront(deque, type); break;
            case "2": PushBack(deque, type); break;
            case "3": PopFront(deque, type); break;
            case "4": PopBack(deque, type); break;;
            case "5": Clear(deque, type); break;
            default: InvalidInput(deque, type); break;
        }
    }

    static void PushFront<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        Console.Write($"Введите значение ({type}): ");
        string input = Console.ReadLine();
        try
        {
            switch (type)
            {
                case "char":
                    char cValue = Convert.ToChar(input ?? string.Empty);
                    (deque as Deque<char>)?.PushFront(cValue);
                    break;
                case "string":
                    string sValue = Convert.ToString(input);
                    (deque as Deque<string>)?.PushFront(sValue);
                    break;
                case "int":
                    int iValue = Convert.ToInt32(input);
                    (deque as Deque<int>)?.PushFront(iValue);
                    break;
                case "double":
                    double dValue = Convert.ToDouble(input);
                    (deque as Deque<double>)?.PushFront(dValue);
                    break;
                case "boolean":
                    bool bValue = Convert.ToBoolean(input);
                    (deque as Deque<bool>)?.PushFront(bValue);
                    break;
            }
        }
        catch { InvalidInput(deque, type, 1); }
        StartProgram(deque, type);
    }
    
    static void PushBack<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        Console.Write($"Введите значение ({type}): ");
        string input = Console.ReadLine();
        try
        {
            switch (type)
            {
                case "char":
                    char cValue = Convert.ToChar(input ?? string.Empty);
                    (deque as Deque<char>)?.PushBack(cValue);
                    break;
                case "string":
                    string sValue = input;
                    (deque as Deque<string>)?.PushBack(sValue);
                    break;
                case "int":
                    int iValue = Convert.ToInt32(input ?? string.Empty);
                    (deque as Deque<int>)?.PushBack(iValue);
                    break;
                case "double":
                    double dValue = Convert.ToDouble(input ?? string.Empty);
                    (deque as Deque<double>)?.PushBack(dValue);
                    break;
                case "boolean":
                    bool bValue = Convert.ToBoolean(input ?? string.Empty);
                    (deque as Deque<bool>)?.PushBack(bValue);
                    break;
            }
        }
        catch { InvalidInput(deque, type, 2); }
        StartProgram(deque, type);
    }
    
    static void PopFront<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        Console.WriteLine(deque.IsEmpty ? "Дек пуст." : $"Из начала дека извлечено значение {deque.PopFront()}.");
        Continue();
        StartProgram(deque, type);
    }
    
    static void PopBack<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        Console.WriteLine(deque.IsEmpty ? "Дек пуст." : $"Из конца дека извлечено значение {deque.PopBack()}.");
        Continue();
        StartProgram(deque, type);
    }

    static void Clear<T>(Deque<T> deque, string type)
    {
        Console.Clear();
        deque.Clear();
        Console.WriteLine("Дек очищен.");
        Continue();
        StartProgram(deque, type);
    }
    
    static void Main()
    {
        switch (InputDequeType())
        {
            case 1: StartProgram(new Deque<char>(), "char"); break;
            case 2: StartProgram(new Deque<string>(), "string"); break;
            case 3: StartProgram(new Deque<int>(), "int"); break;
            case 4: StartProgram(new Deque<double>(), "double"); break;
            case 5: StartProgram(new Deque<bool>(), "boolean"); break;
        }
    }
}
}