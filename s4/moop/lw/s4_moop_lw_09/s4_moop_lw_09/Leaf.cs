using System;
using System.Collections.Generic;

namespace s4_moop_lw_09
{
    public class Leaf<T> : Component<T>
        where T : struct, IEquatable<T>
    {
        public override Component<T> this[int index] => throw new NotSupportedException();
        public override int this[Component<T> child] => throw new NotSupportedException();
        
        protected Leaf() { }
        public Leaf(T data) => _data = data;
        
        public override Component<T> DoOperation(T value, Operation operation)
        {
            _data = operation(_data, value);
            return this;
        }

        public override Component<T> FindLeaf(T data) => throw new NotSupportedException();
        public override Component<T> FindBranch(T data) => throw new NotSupportedException();
        public override Component<T> Find(T data) => throw new NotSupportedException();
        public override Component<T> Find<TPriority>(T data) => throw new NotSupportedException();
        public override Component<T> Add(T data) => throw new NotSupportedException();
        public override Component<T> Add(Component<T> child) => throw new NotSupportedException();
        public override Component<T> Insert(T data, int index) => throw new NotSupportedException();
        public override Component<T> Insert(Component<T> child, int index) => throw new NotSupportedException();
        public override Component<T> Cut(T data) => throw new NotSupportedException();
        public override Component<T> Cut(Component<T> child) => throw new NotSupportedException();
        public override Component<T> Remove(T data) => throw new NotSupportedException();
        public override Component<T> Remove(Component<T> child) => throw new NotSupportedException();

        public override IEnumerator<Component<T>> GetEnumerator() { yield break; }

        public override object Clone() => new Leaf<T>(_data);
        
        public override bool Equals(object obj) => obj is Leaf<T> leaf && Equals(_data, leaf._data);
        public override int GetHashCode() => base.GetHashCode() ^ typeof(Leaf<T>).GetHashCode();
        public override string ToString() => base.ToString() + '-';
    }
}