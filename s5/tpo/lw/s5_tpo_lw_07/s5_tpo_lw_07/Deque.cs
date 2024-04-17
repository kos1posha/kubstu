using System;

namespace s5_tpo_lw_07
{
    [Serializable]
    public class Deque<T> : IDeque<T>
    {
        private readonly DoubleLinkedList<T> _data;
        
        public Deque() => _data = new DoubleLinkedList<T>();

        public Deque(params T[] data) : this() { foreach (T item in data) PushBack(item); }
        public int Count => _data.Count;
        public bool IsEmpty => _data.IsEmpty;
        public void PushFront(T item) =>_data.AddTo(item, 0);
        public void PushBack(T item) => _data.AddTo(item, Count);
        public T PopFront()
        {
            if (IsEmpty) throw new Exception("Deque is empty.");
            T current = _data.Index(0);
            _data.RemoveAt(0);
            return current;
        }
        public T PopBack()
        {
            if (IsEmpty) throw new Exception("Deque is empty.");
            T current = _data.Index(Count - 1);
            _data.RemoveAt(Count - 1);
            return current;
        }
        public T[] ToArray() => _data.ToArray();
    }
}
