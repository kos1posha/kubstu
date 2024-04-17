using System;

namespace s2_asd_lw_03_02
{
    struct Student : IComparable
    {
        public string Name;
        public string Group;
        public int[] Grades;
        public Student(string name, string group, int[] grades)
        {
            Name = name;
            Group = group;
            Grades = grades;
        }
        public int CompareTo(object item)
        {
            if (item is Student student) return Name.CompareTo(student.Name);
            else throw new Exception();
        }
    }
}
