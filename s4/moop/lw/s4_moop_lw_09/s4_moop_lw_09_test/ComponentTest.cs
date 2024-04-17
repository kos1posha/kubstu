using System;
using System.Collections.Generic;
using System.Diagnostics;
using NUnit.Framework;
using s4_moop_lw_09;

namespace s4_moop_lw_09_test
{
    [TestFixture]
    public static class ComponentTest
    {
        [Test]
        public static void NotSupportedMethodsByLeaf()
        {
            Leaf<int> test = new Leaf<int>(10);
            Leaf<int> child = new Leaf<int>(1);

            Assert.Catch<NotSupportedException>(() => test.FindLeaf(1));
            Assert.Catch<NotSupportedException>(() => test.FindBranch(1));
            
            Assert.Catch<NotSupportedException>(() => test.Find(1));
            Assert.Catch<NotSupportedException>(() => test.Find<Leaf<int>>(1));
            Assert.Catch<NotSupportedException>(() => test.Find<Branch<int>>(1));
            
            Assert.Catch<NotSupportedException>(() => test.Add(1));
            Assert.Catch<NotSupportedException>(() => test.Add(child));
            
            Assert.Catch<NotSupportedException>(() => test.Insert(1, 0));
            Assert.Catch<NotSupportedException>(() => test.Insert(child, 0));
            
            Assert.Catch<NotSupportedException>(() => test.Cut(1));
            Assert.Catch<NotSupportedException>(() => test.Cut(child));
            
            Assert.Catch<NotSupportedException>(() => test.Remove(1));
            Assert.Catch<NotSupportedException>(() => test.Remove(child));
        }
        
        [Test]
        public static void GetEnumeratorWithAnyLeaf()
        {
            Leaf<int> test = new Leaf<int>(10);

            IEnumerable<Component<int>> expected = new int[]{}.GetEnumerator() as IEnumerable<Component<int>>;
            IEnumerable<Component<int>> actual = test.GetEnumerator() as IEnumerable<Component<int>>;

            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void GetEnumeratorWithChildfreeBranch()
        {
            Component<int>[] childs = { };
            Branch<int> test = new Branch<int>(10, childs);

            IEnumerable<Component<int>> expected = childs.GetEnumerator() as IEnumerable<Component<int>>;
            IEnumerable<Component<int>> actual = test.GetEnumerator() as IEnumerable<Component<int>>;

            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void GetEnumeratorWithNormalBranch()
        {
            Component<int>[] childs = { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2)} };
            Branch<int> test = new Branch<int>(10, childs);

            IEnumerable<Component<int>> expected = childs.GetEnumerator() as IEnumerable<Component<int>>;
            IEnumerable<Component<int>> actual = test.GetEnumerator() as IEnumerable<Component<int>>;

            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void CloneWithAnyComponent()
        {
            Leaf<int> testLeaf = new Leaf<int>(1);
            Branch<int> testBranch = new Branch<int>(1);
            
            Leaf<int> cloneLeaf = testLeaf.Clone() as Leaf<int>;
            Branch<int> cloneBranch = testBranch.Clone() as Branch<int>;
            
            Assert.AreEqual(testLeaf, cloneLeaf);
            Assert.AreNotSame(testLeaf, cloneLeaf);
            
            Assert.AreEqual(testBranch, cloneBranch);
            Assert.AreNotSame(testBranch, cloneBranch);
        }
        
        [Test]
        public static void GetHashCodeWithAnyComponent()
        {
            Leaf<int> testLeaf = new Leaf<int>(1);
            Branch<int> testBranch = new Branch<int>(1);

            Leaf<int> cloneLeaf = testLeaf.Clone() as Leaf<int>;
            Branch<int> cloneBranch = testBranch.Clone() as Branch<int>;

            Debug.Assert(cloneLeaf != null, nameof(cloneLeaf) + " != null");
            Assert.AreEqual(testLeaf.GetHashCode(), cloneLeaf.GetHashCode());
            
            Debug.Assert(cloneBranch != null, nameof(cloneBranch) + " != null");
            Assert.AreEqual(testBranch.GetHashCode(), cloneBranch.GetHashCode());
            
            Assert.AreNotEqual(testLeaf.GetHashCode(), testBranch.GetHashCode());
        }
        
        [Test]
        public static void DoOperationWithAnyLeaf()
        {
            Leaf<int> test = new Leaf<int>(10);

            Leaf<int> expected = new Leaf<int>(100);
            Leaf<int> actual = test.DoOperation(10, (x, y) => x * y) as Leaf<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void DoOperationWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);

            Branch<int> expected = new Branch<int>(100);
            Branch<int> actual = test.DoOperation(10, (x, y) => x * y) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void DoOperationWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };

            Branch<int> expected = new Branch<int>(100) { new Leaf<int>(10), new Leaf<int>(20), new Branch<int>(200) { new Leaf<int>(10), new Branch<int>(20) } };
            Branch<int> actual = test.DoOperation(10, (x, y) => x * y) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public static void FindLeafWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);

            Leaf<int> expected = null;
            Leaf<int> actual = test.FindLeaf(2) as Leaf<int>;

            // ReSharper disable once ExpressionIsAlwaysNull
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FindLeafWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };

            Leaf<int> expected = new Leaf<int>(2);
            Leaf<int> actual = test.FindLeaf(2) as Leaf<int>;
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void FindBranchWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
        
            Branch<int> expected = null;
            Branch<int> actual = test.FindBranch(20) as Branch<int>;
            
            // ReSharper disable once ExpressionIsAlwaysNull
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FindBranchWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
            
            Branch<int> expected = new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) };
            Branch<int> actual = test.FindBranch(20) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void FindWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
        
            Component<int> expected = null;
            Component<int> actual = test.Find(2);
            
            // ReSharper disable once ExpressionIsAlwaysNull
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FindWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
        
            Component<int> expected = new Leaf<int>(2);
            Component<int> actual = test.Find(2);
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void AddWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
            
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1) };
            Branch<int> actual = test.Add(1) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void AddWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2) };
        
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
            Branch<int> actual =  test.Add(new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) }) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void InsertWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
        
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1) };
            Branch<int> actual = test.Insert(new Leaf<int>(1), 0) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void InsertWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2) };
            
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
            Branch<int> actual = test.Insert(new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) }, 2) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void CutWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
        
            Branch<int> expected = new Branch<int>(10);
            Branch<int> actual = test.Cut(20) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void CutWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
        
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Leaf<int>(1), new Branch<int>(2) };
            Branch<int> actual = test.Cut(20) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public static void RemoveWithChildfreeBranch()
        {
            Branch<int> test = new Branch<int>(10);
        
            Branch<int> expected = new Branch<int>(10);
            Branch<int> actual = test.Remove(20) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void RemoveWithNormalBranch()
        {
            Branch<int> test = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2), new Branch<int>(20) { new Leaf<int>(1), new Branch<int>(2) } };
        
            Branch<int> expected = new Branch<int>(10) { new Leaf<int>(1), new Leaf<int>(2) };
            Branch<int> actual = test.Remove(20) as Branch<int>;
            
            Assert.AreEqual(expected, actual);
        }
    }
}