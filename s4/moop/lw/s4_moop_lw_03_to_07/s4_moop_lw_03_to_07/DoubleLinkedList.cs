using System;
using System.Collections;
using System.Collections.Generic;

namespace s4_moop_lw_03_to_07
{
    [Serializable]
    public class DoubleLinkedList<T> : IEnumerable<T>, ICloneable
    {
        Node<T> _head;
        Node<T> _tail;
        int _count;

        DoubleLinkedList(Node<T> head, Node<T> tail, int count)
        {
            _head = head;
            _tail = tail;
            _count = count;
        }
        
        public DoubleLinkedList() { }
        
        public DoubleLinkedList(params T[] data)
        {
            foreach (T item in data) Add(item);
        }

        public int Count => _count;
        public bool IsEmpty => _count == 0;

        Node<T> ItemByIndex(int index)
        {
            int i = 0;
            foreach (Node<T> item in ItemEnumerator())
                if (i++ == index) return item;
            throw new IndexOutOfRangeException();
        }
        
        public T Index(int index)
        {
            int i = 0;
            foreach(T item in this)
                if (i++ == index) return item;
            throw new IndexOutOfRangeException();
        }
        
        Node<T> ItemByValue(T value)
        {
            foreach (Node<T> node in ItemEnumerator())
                if (node.Data.Equals(value)) return node;
            return null;
        }
        
        public int Value(T value)
        {
            int i = 0;
            foreach (T item in this)
                if (item.Equals(value)) return i;
                else i++;
            return -1;
        }

        void AddItem(Node<T> item, int toIndex)
        {
            if (toIndex > _count) throw new IndexOutOfRangeException();
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
            else if (toIndex == _count)
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
            _count++;
        }
        
        public void Add(T item) => AddItem(new Node<T>(item), Count);
        
        public void AddTo(T item, int toIndex) => AddItem(new Node<T>(item), toIndex);

        bool RemoveItem(Node<T> item)
        {
            if (item == null) return false;
            if (_head == item)
            {
                item = _head.Next;
                if (_count != 1) _head.Next.Previous = null;
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
            _count--;
            return true;
        }
        
        public bool Remove(T item) => RemoveItem(ItemByValue(item));
        
        public bool RemoveAt(int atIndex) => RemoveItem(ItemByIndex(atIndex));

        public void Clear()
        {
            _head = null;
            _tail = null;
            _count = 0;
        }
        
        public T[] ToArray()
        {
            T[] array = new T[Count];
            
            int i = 0;
            foreach (T item in this)
                array[i++] = item;

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
        IEnumerator IEnumerable.GetEnumerator()
        {
            return ((IEnumerable)this).GetEnumerator();
        }
        IEnumerator<T> IEnumerable<T>.GetEnumerator()
        {
            Node<T> current = _head;
            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }

        public override string ToString()
        {
            if (_head == null) return "[]";
            string s = string.Empty;
            foreach (T data in this)
                s += $"{data}, ";
            return $"[{s.Remove(s.Length - 2)}]";
        }

        public object Clone() => new DoubleLinkedList<T>(_head, _tail, _count);
    }
}
