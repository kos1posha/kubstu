using System;
using System.Collections.Generic;
using System.Linq;

namespace s4_moop_lw_09
{
    public class Branch<T> : Component<T>
        where T : struct, IEquatable<T>
    {
        protected readonly List<Component<T>> _childs;
        public List<Component<T>> Childs => _childs;
        
        protected IEnumerable<Component<T>> _leafs => _childs.FindAll(child => child is Leaf<T>);
        protected IEnumerable<Component<T>> _branches => _childs.FindAll(child => child is Branch<T>);
        
        public override Component<T> this[int index] => _childs[index];
        public override int this[Component<T> child] => FindChildIndex(child);

        protected Branch() => _childs = new List<Component<T>>();
        public Branch(T data) : this() => _data = data;
        public Branch(T data, IEnumerable<Component<T>> childs) : this(data) => _childs.AddRange(childs);

        public override Component<T> DoOperation(T value, Operation operation)
        {
            _data = operation(_data, value);
            foreach (Component<T> child in _childs) 
                child.DoOperation(value, operation);
            
            return this;
        }

        public override Component<T> FindLeaf(T data) => _leafs.FirstOrDefault(leaf => Equals(data, leaf.Data));
        public override Component<T> FindBranch(T data) => _branches.FirstOrDefault(branch => Equals(data, branch.Data));

        public override Component<T> Find(T data)
        {
            foreach (Component<T> child in _childs)
                if (Equals(child.Data, data)) return child;
            
            return null;
        }
        public override Component<T> Find<TPriority>(T data)
        {
            return typeof(TPriority) == typeof(Leaf<T>) ? 
                Enumerable.Concat(_leafs, _branches).First(child => Equals(child.Data, data)): 
                Enumerable.Concat(_branches, _leafs).First(child => Equals(child.Data, data));
        }
        
        public int FindChildIndex(T data) => FindChildIndex(Find(data));
        public int FindChildIndex(Component<T> child) => _childs.IndexOf(child);

        public override Component<T> Add(T data) => Add(new Leaf<T>(data));
        public override Component<T> Add(Component<T> child)
        {
            if (child == null) throw new NullReferenceException();
            if (ReferenceEquals(child, this) || _childs.Contains(child)) 
                child = child.Clone() as Component<T>;
            
            _childs.Add(child);
            
            return this;
        }

        public override Component<T> Insert(T data, int index) => Insert(new Leaf<T>(data), index);
        public override Component<T> Insert(Component<T> child, int index)
        {
            if (child == null) throw new NullReferenceException();
            if (ReferenceEquals(child, this) || _childs.Contains(child)) 
                child = child.Clone() as Component<T>;
            
            _childs.Insert(index, child);
            
            return this;
        }

        public override Component<T> Cut(T data) => Cut(Find(data));
        public override Component<T> Cut(Component<T> child)
        {
            if (child == null) return this;
            
            foreach (Component<T> grandchild in child)
                Add(grandchild);
            _childs.Remove(child);
            
            return this;
        }

        public override Component<T> Remove(T data) => Remove(Find(data)); 
        public override Component<T> Remove(Component<T> child)
        {
            if (child == null) return this;
            
            _childs.Remove(child);
            
            return this;
        }

        public override IEnumerator<Component<T>> GetEnumerator() => _childs.GetEnumerator();
        
        public override object Clone() => new Branch<T>(_data, _childs.Select(child => child.Clone() as Component<T>));

        public override bool Equals(object obj)
        {
            if (!(obj is Branch<T> branch))
                return false;

            if (!Equals(_data, branch._data))
                return false;
            
            for (int i = 0; i < _childs.Count; i++)
                if (!Equals(this[i], branch[i]))
                    return false;

            return true;
        }
        public override int GetHashCode()
        {
            int hash = base.GetHashCode() ^ typeof(Branch<T>).GetHashCode();

            for (int i = 0; i < _childs.Count; i++)
                hash ^= this[i].GetHashCode() * (i + 1);

            return hash;
        }
        public override string ToString() => ToString(0);
        private string ToString(int depth)
        {
            if (_childs.Count == 0) return base.ToString() + '+';
            
            string separator = new string('\t', depth);
            string childs = String.Join($"\n{separator}\t", _childs.Select
                (child => String.Join($"\n{separator}\t", child.ToString().Split('\n'))));

            return $"{base.ToString()}+{separator}\n{separator}\t{childs}{separator}";
        }
    }
}