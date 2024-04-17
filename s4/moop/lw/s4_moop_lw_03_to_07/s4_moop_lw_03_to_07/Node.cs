using System;

namespace s4_moop_lw_03_to_07
{
    [Serializable]
    public class Node<T>
    {
        public T Data { get; set; }
        public Node<T> Previous { get; set; }
        public Node<T> Next { get; set; }

        public Node(T data)
        {
            Data = data;
        }

        public Node<T> GetFirst()
        {
            Node<T> current = this;
            while (current.Previous != null)
                current = current.Previous;
            return current;
        }
        public Node<T> GetLast()
        {
            Node<T> current = this;
            while (current.Next != null)
                current = current.Next;
            return current;
        }
    }
}