using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_03_01
{
    class SpiralList<T>
    {
        public Node<T> First;
        public Node<T> Last;
        public int Count;
        public bool IsEmpty => Count == 0;
        public SpiralList() { }
        public SpiralList(T[] array)
        {
            foreach (T item in array)
            {
                Add(item);
            }
        }
        public SpiralList(List<T> list)
        {
            foreach (T item in list)
            {
                Add(item);
            }
        }
        public Node<T> ToIndex(int index)
        {
            if (IsEmpty)
            {
                throw new Exception("Spiral list is empty.");
            }
            if (index < 0)
            {
                index = (index % Count) + Count;
            }
            if (index >= Count)
            {
                index %= Count;
            }
            Node<T> temp = First;
            while (true)
            {
                if (temp.Index == index)
                {
                    return temp;
                }
                else
                {
                    temp = temp.Next;
                }
            }
        }
        public void AddTo(T input, int index)
        {
            Node<T> temp;
            if (IsEmpty)
            {
                First = new Node<T>(input, null, Count++);
                Last = First;
                First.Next = Last;
                return;
            }
            if (index == 0)
            {
                First = new Node<T>(input, First, 0);
                Last.Next = First;
                temp = First;
                Count++;
                for (int i = 1; i <= Count - 1; i++)
                {
                    temp = temp.Next;
                    temp.Index++;
                }
                return;
            }
            if (index == Count)
            {
                temp = new Node<T>(input, First, Count++);
                Last.Next = temp;
                Last = temp;
                return;
            }
            temp = ToIndex(index - 1);
            temp.Next = new Node<T>(input, temp.Next, index);
            temp = temp.Next;
            Count++;
            for (int i = temp.Index; i < Count - 1; i++)
            {
                temp = temp.Next;
                temp.Index++;
            }
        }
        public void Add(T input) => AddTo(input, Count);
        public void AddFirst(T input) => AddTo(input, 0);
        public void RemoveTo(int index)
        {
            Node<T> temp;
            if (IsEmpty)
            {
                throw new Exception("Spiral list is empty.");
            }
            if (Count == 1)
            {
                First = null;
                Last = null;
                Count--;
                return;
            }
            if (index == 0)
            {
                temp = Last;
                First = First.Next;
                Last.Next = First;
                Count--;
                for (int i = 0; i <= Count - 1; i++)
                {
                    temp = temp.Next;
                    temp.Index--;
                }
                return;
            }
            if (index == Count - 1)
            {
                Last = ToIndex(--Count - 1);
                Last.Next = First;
                return;
            }
            temp = ToIndex(index - 1);
            temp.Next = temp.Next.Next;
            Count--;
            for (int i = temp.Index; i < Count - 1; i++)
            {
                temp = temp.Next;
                temp.Index--;
            }
        }
        public void Remove() => RemoveTo(Count - 1);
        public void RemoveFirst() => RemoveTo(0);
        public void Clear()
        {
            First = null;
            Last = null;
            Count = 0;
        }
        public void Show()
        {
            if (IsEmpty)
            {
                Console.WriteLine("Spiral list is empty.");
                return;
            }
            Node<T> temp = Last;
            for (int i = 0; i < Count; i++)
            {
                temp = temp.Next;
                Console.WriteLine($"{temp.Index}) {temp.Data}");
            }
        }
    }
}
