using System;
using s4_moop_lw_02;
using NUnit.Framework;

namespace s4_moop_lw_02_test
{
    [TestFixture]
    class InsertionSortTest
    {
        [Test]
        public void SortTestNormalArrayWithUniqueElements()
        {
            int[] test = { 1, 2, 9, -4, 5 };
            int[] expected = { -4, 1, 2, 5, 9 };
            int[] actual = InsertionSort.Sort(test);
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public void SortTestNormalArrayWithSameElements()
        {
            int[] test = { 2, 2, 2 };
            int[] expected = { 2, 2, 2 };
            int[] actual = InsertionSort.Sort(test);
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public void SortTestNormalArrayWithRepeatedElements()
        {
            int[] test = { 1, 2, 2, 2, 1, 4 };
            int[] expected = { 1, 1, 2, 2, 2, 4 };
            int[] actual = InsertionSort.Sort(test);
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public void SortTestArrayWithOneElement()
        {
            int[] test = { 3 };
            int[] expected = { 3 };
            int[] actual = InsertionSort.Sort(test);
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public void SortTestEmptyArray()
        {
            int[] test = null;
            int[] actual;
            Assert.Throws<ArgumentException>(() => { actual = InsertionSort.Sort(test); });
        }
    }
}