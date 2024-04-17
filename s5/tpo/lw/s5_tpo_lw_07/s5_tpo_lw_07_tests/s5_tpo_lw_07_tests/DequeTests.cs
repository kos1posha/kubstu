using NUnit.Framework;
using s5_tpo_lw_07;

namespace s5_tpo_lw_07_tests
{
    [TestFixture]
    public class DequeTests
    {
        [Test]
        public void Create_EmptyDeque_Test()
        {
            Deque<int> deque = new Deque<int>();
            Assert.IsFalse(deque is null);
        }
        
        [Test]
        public void PopFront_EmptyDeque_Test()
        {
            Deque<int> deque = new Deque<int>();
            Assert.Catch(() => { deque.PopFront(); });
        }
        
        [Test]
        public void PopBack_EmptyDeque_Test()
        {
            Deque<int> deque = new Deque<int>();
            Assert.Catch(() => { deque.PopBack(); });
        }
        
        [Test]
        public void PushFront_EmptyDeque_Test()
        {
            Deque<int> deque = new Deque<int>();
            deque.PushFront(1);
            Assert.AreEqual(new[] { 1 }, deque.ToArray());
        }
        
        [Test]
        public void PushBack_EmptyDeque_Test()
        {
            Deque<int> deque = new Deque<int>();
            deque.PushBack(1);
            Assert.AreEqual(new[] { 1 }, deque.ToArray());
        }

        [Test]
        public void Create_FillDeque_Test()
        {
            Deque<int> deque = new Deque<int>(1, 2, 3);
            Assert.IsFalse(deque is null);
            Assert.AreEqual(new[] { 1, 2, 3 }, deque.ToArray());
        }
        
        [Test]
        public void PopFront_FillDeque_Test()
        {
            Deque<int> deque = new Deque<int>(1, 2, 3);
            int pop = deque.PopFront();
            Assert.AreEqual(new[] { 2, 3 }, deque.ToArray());
            Assert.AreEqual(1, pop);
        }

        [Test]
        public void PopBack_FillDeque_Test()
        {
            Deque<int> deque = new Deque<int>(1, 2, 3);
            int pop = deque.PopBack();
            Assert.AreEqual(new[] { 1, 2 }, deque.ToArray());
            Assert.AreEqual(3, pop);
        }
        
        [Test]
        public void PushFront_FillDeque_Test()
        {
            Deque<int> deque = new Deque<int>(1, 2, 3);
            deque.PushFront(4);
            Assert.AreEqual(new[] { 4, 1, 2, 3 }, deque.ToArray());
        }

        [Test]
        public void PushBack_FillDeque_Test()
        {
            Deque<int> deque = new Deque<int>(1, 2, 3);
            deque.PushBack(4);
            Assert.AreEqual(new[] { 1, 2, 3, 4 }, deque.ToArray());
        }
    }
}