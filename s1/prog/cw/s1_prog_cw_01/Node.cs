using System;
using System.Collections.Generic;
using System.Text;

namespace s1_prog_cw_01
{
    // Следующий класс создан, чтобы хранить в каждой посчитанной экспоненте не только результат ряда Тейлора, но и просуммированных членов ряда
    public class Node
    {
        public double Exponent { get; set; }
        public int Count { get; set; }
        public Node(double exponent, int count) { Exponent = exponent; Count = count; }
    }
}
