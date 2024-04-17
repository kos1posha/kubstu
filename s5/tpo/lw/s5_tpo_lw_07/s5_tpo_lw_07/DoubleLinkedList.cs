using System;
using System.Collections;
using System.Collections.Generic;

namespace s5_tpo_lw_07
{
    [Serializable]
    public class DoubleLinkedList<T> : IEnumerable<T>
    {
        Node<T> _head;
        Node<T> _tail;
        public int Count { get; private set; }
        public bool IsEmpty => Count == 0;
        Node<T> ItemByIndex(int index)
        {
            int i = 0;
            foreach (Node<T> item in ItemEnumerator()) if (i++ == index) return item;
            throw new IndexOutOfRangeException();
        }
        public T Index(int index)
        {
            int i = 0;
            foreach(T item in this) if (i++ == index) return item;
            throw new IndexOutOfRangeException();
        }
        void AddItem(Node<T> item, int toIndex)
        {
            if (toIndex > Count) throw new IndexOutOfRangeException();
            if (_head == null)
            {
                _head = item;
                _tail = item;
            }
            else if (toIndex == 0)
            {
                item.Next = _head;
                _head.Previous = item;
                _head = item;
            }
            else if (toIndex == Count)
            {
                item.Previous = _tail;
                _tail.Next = item;
                _tail = item;
            }
            else
            {
                Node<T> node = ItemByIndex(toIndex);
                item.Next = node;
                item.Previous = node.Previous;
                node.Previous.Next = item;
                node.Previous = item;
            }
            Count++;
        }

        public void AddTo(T item, int toIndex) => AddItem(new Node<T>(item), toIndex);

        bool RemoveItem(Node<T> item)
        {
            if (item == null) return false;
            if (_head == item)
            {
                item = _head.Next;
                if (Count != 1) _head.Next.Previous = null;
                _head = item;
            }
            else if (_tail == item)
            {
                item = _tail.Previous;
                _tail.Previous.Next = null;
                _tail = item;
            }
            else
            {
                item.Previous.Next = item.Next;
                item.Next.Previous = item.Previous;
            }
            Count--;
            return true;
        }
        public bool RemoveAt(int atIndex) => RemoveItem(ItemByIndex(atIndex));
        public T[] ToArray()
        {
            T[] array = new T[Count];
            int i = 0;
            foreach (T item in this) array[i++] = item;
            return array;
        }
        IEnumerable ItemEnumerator()
        {
            Node<T> current = _head;
            while (current != null)
            {
                yield return current;
                current = current.Next;
            }
        }
        IEnumerator IEnumerable.GetEnumerator() => ((IEnumerable)this).GetEnumerator();
            IEnumerator<T> IEnumerable<T>.GetEnumerator()
        {
            Node<T> current = _head;
            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }
    }
}
