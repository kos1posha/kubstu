using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_03_01
{
    class Node<T>
    {
        public T Data;
        public int Index;
        public Node<T> Next;
        public Node() { }
        public Node(T data, Node<T> next, int index)
        {
            Data = data;
            Next = next;
            Index = index;
        }
    }
}
