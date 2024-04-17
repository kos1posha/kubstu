using System;
using System.Collections.Generic;

namespace s2_asd_lw_07_02
{
    class Student
    {
        public string FirstName { get; private set; }
        public string LastName { get; private set; }
        public DateTime Birthday { get; private set; }
        public int AlgAndDatGrade { get; private set; }
        public int HighMathGrade { get; private set; }
        public int PhysGrade { get; private set; }
        public int ProgGrade { get; private set; }
        public double TotalGrade { get; private set; }
        public Student() { }
        public Student(string firstName, string lastName, DateTime birthday, int algAndDatGrade, int highMathGrade, int physGrade, int progGrade)
        {
            FirstName = firstName;
            LastName = lastName;
            Birthday = birthday;
            SetGrades(algAndDatGrade, highMathGrade, physGrade, progGrade);
        }
        public void SetGrades(int algAndDatGrade, int highMathGrade, int physGrade, int progGrade)
        {
            AlgAndDatGrade = algAndDatGrade;
            HighMathGrade = highMathGrade;
            PhysGrade = physGrade;
            ProgGrade = progGrade;
            TotalGrade = (AlgAndDatGrade + HighMathGrade + PhysGrade + ProgGrade) / 4.0;
        }
        public static Student Generator()
        {
            Random random = new Random();
            string[] firstNames = new string[]
            {
                "Стас", "Гена", "Слава", "Руслан", "Антон", "Денис", "Андрей", "Максим", "Богдан", "Артур", "Матвей", "Влад"
            };
            string[] lastNames = new string[]
            {
                "Комаров", "Пикалюк", "Доценко", "Павлов", "Параскевопулос", "Пахин", "Терешков", "Ктохин", "Балабайко", "Стасюк", "Питкин", "Иванов"
            };
            return new Student(
                        firstNames[random.Next(12)],
                        lastNames[random.Next(12)],
                        new DateTime(random.Next(1998, 2005), random.Next(1, 13), random.Next(1, 29)),
                        random.Next(2, 6), random.Next(2, 6), random.Next(2, 6), random.Next(2, 6));
        }
        public static List<Student> Generator(int N)
        {
            List<Student> group = new List<Student>();
            Random random = new Random();
            string[] firstNames = new string[]
            {
                "Стас", "Гена", "Слава", "Руслан", "Антон", "Денис", "Андрей", "Максим", "Богдан", "Артур", "Матвей", "Влад"
            };
            string[] lastNames = new string[]
            {
                "Комаров", "Пикалюк", "Доценко", "Павлов", "Параскевопулос", "Пахин", "Терешков", "Ктохин", "Балабайко", "Стасюк", "Питкин", "Иванов"
            };
            for (int i = 0; i < N; i++)
            {
                group.Add(
                    new Student(
                        firstNames[random.Next(12)],
                        lastNames[random.Next(12)],
                        new DateTime(random.Next(1998, 2005), random.Next(1, 13), random.Next(1, 29)),
                        random.Next(2, 6), random.Next(2, 6), random.Next(2, 6), random.Next(2, 6)));
            }
            return group;
        }
        public void Show()
        {
            Console.WriteLine(new String('-', 46));
            Console.WriteLine($"Имя: {FirstName} {LastName}\n" +
                              $"День рождения: {Birthday.ToShortDateString()}\n" +
                              $"АСД: {AlgAndDatGrade} Вышмат: {HighMathGrade} Физика: {PhysGrade} Программирование: {ProgGrade}\n" +
                              $"Общая оценка: {TotalGrade}");
        }
    }
}
