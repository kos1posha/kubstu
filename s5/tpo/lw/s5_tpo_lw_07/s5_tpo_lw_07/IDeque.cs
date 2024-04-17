namespace s5_tpo_lw_07
{
    interface IDeque<T>
    {
        void PushBack(T item);
        void PushFront(T item);
        T PopBack();
        T PopFront();
    }
}
