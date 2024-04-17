using System;
using System.Collections;
using System.Collections.Generic;

namespace s4_moop_lw_09
{
    public abstract class Component<T> : IEnumerable<Component<T>>, ICloneable
        where T : IEquatable<T>
    {
        protected T _data;
        public T Data
        {
            get => _data;
            set => _data = value;
        }

        public abstract Component<T> this[int index] { get; }
        public abstract int this[Component<T> child] { get; }

        public delegate T Operation(T x, T y);

        public abstract Component<T> DoOperation(T value, Operation operation);

        public abstract Component<T> FindLeaf(T data);
        public abstract Component<T> FindBranch(T data);
        public abstract Component<T> Find(T data);
        public abstract Component<T> Find<TPriority>(T data) where TPriority : Component<T>;
        public abstract Component<T> Add(T data);
        public abstract Component<T> Add(Component<T> child);
        public abstract Component<T> Insert(T data, int index);
        public abstract Component<T> Insert(Component<T> child, int index);
        public abstract Component<T> Cut(T data);
        public abstract Component<T> Cut(Component<T> child);
        public abstract Component<T> Remove(T data);
        public abstract Component<T> Remove(Component<T> child);

        public abstract IEnumerator<Component<T>> GetEnumerator();
        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
        
        public abstract object Clone();
        
        public override bool Equals(object obj) => obj is Component<T> component && Equals(_data, component._data);
        public override int GetHashCode() => _data.GetHashCode() ^ typeof(Component<T>).GetHashCode();
        public override string ToString() => _data.ToString();
    }
}