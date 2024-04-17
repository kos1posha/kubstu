namespace s4_moop_lw_03_to_07
{
    interface IDeque<T>
    {
        void PushBack(T item);
        void PushFront(T item);
        T PopBack();
        T PopFront();
        void Clear();
    }
}
