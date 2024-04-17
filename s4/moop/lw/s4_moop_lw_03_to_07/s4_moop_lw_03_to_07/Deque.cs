using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;

namespace s4_moop_lw_03_to_07
{   
    [Serializable]
    public class Deque<T> : IDeque<T>, IEnumerable<T>, ICloneable
    {
        private readonly DoubleLinkedList<T> _data;
        
        Deque(DoubleLinkedList<T> data)
        {
            _data = data;
        }
        public Deque()
        {
            _data = new DoubleLinkedList<T>();
        }

        public Deque(params T[] data) : this()
        {
            foreach (T item in data)
                PushBack(item);
        }

        public int Count => _data.Count;
        public bool IsEmpty => _data.IsEmpty;

        public void PushFront(T item) =>_data.AddTo(item, 0);
        public void PushBack(T item) => _data.AddTo(item, Count);
        public T PopFront()
        {
            if (IsEmpty) 
                throw new Exception("Deque is empty.");
            T current = _data.Index(0);
            _data.RemoveAt(0);
            return current;
        }
        public T PopBack()
        {
            if (IsEmpty) 
                throw new Exception("Deque is empty.");
            T current = _data.Index(Count - 1);
            _data.RemoveAt(Count - 1);
            return current;
        }

        public static void Serialize(string path, Deque<T> deque)
        {
            using (FileStream fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write))
                new BinaryFormatter().Serialize(fs, deque);
        }

        public static Deque<T> Deserialize(string path)
        {
            using (FileStream fs = new FileStream(path, FileMode.Open, FileAccess.Read))
                return new BinaryFormatter().Deserialize(fs) as Deque<T>;
        }

        public void Clear() => _data.Clear();
        public T[] ToArray() => _data.ToArray();

        public override string ToString() => $"<{_data.ToString().Trim('[', ']')}>";
        
        public object Clone() => new Deque<T>(_data.Clone() as DoubleLinkedList<T>);

        IEnumerator IEnumerable.GetEnumerator() => ((IEnumerable)this).GetEnumerator();
        IEnumerator<T> IEnumerable<T>.GetEnumerator() => ((IEnumerable<T>)_data).GetEnumerator();
    }
}
