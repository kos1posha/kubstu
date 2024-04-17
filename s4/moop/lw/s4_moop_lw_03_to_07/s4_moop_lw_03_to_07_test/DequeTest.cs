using System;
using System.Linq;
using NUnit.Framework;
using s4_moop_lw_03_to_07;

namespace s4_moop_lw_03_to_07_test
{
    [TestFixture]
    public static class DequeTest
    {
        #region lw_03_tests
        
        [Test]
        public static void AddFirstWithNormalDeque()
        {
            Deque<int> test = new Deque<int>();
            
            for (int i = 0; i < 10; i++) 
                test.PushFront(i);
            
            int[] expected = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
            int[] actual = test.ToArray();
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void AddLastWithNormalDeque()
        {
            Deque<int> test = new Deque<int>();
            
            for (int i = 0; i < 10; i++) 
                test.PushBack(i);

            int[] expected = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int[] actual = test.ToArray();
            
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public static void PopFirstWithNormalDeque()
        {
            Deque<int> test = new Deque<int>( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 );

            int expectedPopValue = 0;
            int actualPopValue = test.PopFront();
            int[] expectedDequeValue = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
            int[] actualDequeValue = test.ToArray();
            
            Assert.AreEqual(expectedPopValue, actualPopValue);
            Assert.AreEqual(expectedDequeValue, actualDequeValue);
        }
        [Test]
        public static void PopFirstWithEmptyDeque()
        {
            Deque<int> test = new Deque<int>();
            Assert.Throws<Exception>(() => { test.PopFront(); });
        }
        [Test]
        public static void PopLastWithNormalDeque()
        {
            Deque<int> test = new Deque<int>( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 );

            int expectedPopValue = 9;
            int actualPopValue = test.PopBack();
            int[] expectedDequeValue = { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
            int[] actualDequeValue = test.ToArray();
            
            Assert.AreEqual(expectedPopValue, actualPopValue);
            Assert.AreEqual(expectedDequeValue, actualDequeValue);
        }
        [Test]
        public static void PopLastWithEmptyDeque()
        {
            Deque<int> test = new Deque<int>();
            Assert.Throws<Exception>(() => { test.PopBack(); });
        }

        [Test]
        public static void ClearWithNormalDeque()
        {
            Deque<int> test = new Deque<int>( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 );
            
            test.Clear();

            int[] expected = { };
            int[] actual = test.ToArray();

            Assert.AreEqual(expected, actual);
        }
        
        #endregion
        
        #region lw_04_tests
        
        [Test]
        public static void DequeWithIntegerElements()
        {
            Deque<int> test = new Deque<int>();
            
            for (int i = 0; i < 10; i++)
                test.PushFront(i);
            for (int i = 0; i < 5; i++)
                test.PopBack();
            
            int[] expected = test.ToArray();
            int[] actual = {9, 8, 7, 6, 5};
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void DequeWithStringElemenets()
        {
            Deque<string> test = new Deque<string>();
            
            for (int i = 0; i < 10; i++)
                test.PushFront(i.ToString());
            for (int i = 0; i < 5; i++)
                test.PopBack();
            
            string[] expected = test.ToArray();
            string[] actual = {"9", "8", "7", "6", "5"};
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void DequeWithDecimalElements()
        {
            Deque<decimal> test = new Deque<decimal>();
            
            for (decimal i = 0; i < 11; i += 1.11m)
                test.PushFront(i);
            for (int i = 0; i < 5; i++)
                test.PopBack();
            
            decimal[] expected = test.ToArray();
            decimal[] actual = { 9.99m, 8.88m, 7.77m, 6.66m, 5.55m };
            
            Assert.AreEqual(expected, actual);
        }
        
        #endregion
        
        #region lw_05_tests
        
        [Test]
        public static void CloneWithNormalDeque()
        {
            Deque<int> test = new Deque<int>();
            for (int i = 0; i < 10; i++)
                test.PushFront(i);

            int[] expected = test.ToArray();
            int[] actual = ((Deque<int>)test.Clone()).ToArray();

            Assert.AreEqual(expected, actual);
            Assert.AreNotSame(test, actual);
        }
        [Test]
        public static void CloneWithSingleElementDeque()
        {
            Deque<int> test = new Deque<int>();
            test.PushFront(1);

            int[] expected = test.ToArray();
            int[] actual = ((Deque<int>)test.Clone()).ToArray();

            Assert.AreEqual(expected, actual);
            Assert.AreNotSame(test, actual);
        }
        [Test]
        public static void CloneWithEmptyDeque()
        {
            Deque<int> test = new Deque<int>();

            int[] expected = test.ToArray();
            int[] actual = ((Deque<int>)test.Clone()).ToArray();

            Assert.AreEqual(expected, actual);
            Assert.AreNotSame(test, actual);
        }
        
        #endregion
        
        #region lw_06_tests
        
        [Test]
        public static void PipelineTest()
        {
            Deque<int> test = new Deque<int>( 2, 4, 3, 0, 9, 5, 0, 9, 6, 0 );

            int[] expectedNoZero = { 2, 4, 3, 9, 5, 9, 6 };
            int[] actualNoZero = test.Where(x => x != 0).ToArray();
            int expectedMin = 2;
            int actualMin = test.Where(x => x != 0).Min();
            
            Assert.AreEqual(expectedNoZero, actualNoZero);
            Assert.AreEqual(expectedMin, actualMin);
        }
        [Test]
        public static void ForeachTest()
        {
            Deque<int> test = new Deque<int>( 2, 4, 3, 0, 9, 5, 0, 9, 6, 0 );
            
            Deque<int> tempDeque = new Deque<int>();
            int tempMin = Int32.MaxValue;
            foreach (int item in test)
                if (item != 0)
                {
                    tempDeque.PushBack(item);
                    tempMin = Math.Min(tempMin, item);
                }

            int[] expectedNoZero = { 2, 4, 3, 9, 5, 9, 6 };
            int[] actualNoZero = tempDeque.ToArray();
            int expectedMin = 2;
            int actualMin = tempMin;
            
            Assert.AreEqual(expectedNoZero, actualNoZero);
            Assert.AreEqual(expectedMin, actualMin);
        }
        
        #endregion
        
        #region lw_07_tests

        [Test]
        public static void SerializeTestWithNormalDeque()
        {
            Deque<int> test = new Deque<int>( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 );
            
            Deque<int>.Serialize("deque_save.dat", test);

            int[] expected = test.ToArray();
            int[] actual = Deque<int>.Deserialize("deque_save.dat").ToArray();
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void SerializeTestWithNullDeque()
        {
            Assert.Throws<ArgumentNullException>(() => { Deque<int>.Serialize("deque_save.dat", null); });
        }
        
        #endregion
    }
}
