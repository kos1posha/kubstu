using System;
using System.Collections.Generic;

namespace s2_asd_lw_07_02
{
    class Program
    {
        public static int FindMin(List<Student> group, int startIndex)
        {
            int index = startIndex;
            for (int i = startIndex; i < group.Count; i++)
            {
                if (group[i].Birthday < group[index].Birthday)
                    index = i;
            }
            return index;
        }
        public static void SelectionSort(List<Student> group)
        {
            for (int i = 0; i < group.Count; i++)
            {
                int min = FindMin(group, i);
                (group[i], group[min]) = (group[min], group[i]);
            }
        }
        static void Main(string[] args)
        {
            Console.Write("Введите N: ");
            int N = Convert.ToInt32(Console.ReadLine());
            Console.Clear();

            List<Student> group = Student.Generator(N);

            SelectionSort(group);

            foreach (Student student in group) student.Show();
            Console.WriteLine(new String('-', 46));
        }
    }
}