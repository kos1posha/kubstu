using System;
using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;
using s4_moop_lw_08;


namespace s4_moop_lw_08_test
{
    [TestFixture]
    public static class listTest
    {
        #region MapTests

        [Test]
        public static void MapWithIntArray()
        {
            int[] test = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            int[] expected = { 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 };
            int[] actual = list.map(test, x => x * x).ToArray();
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void MapWithStringArray()
        {
            string[] test = { "aab", "bac", "ca", "c", "bbc", "acc", "abc" };

            string[] expected = { "baa", "cab", "ac", "c", "cbb", "cca", "cba" };
            string[] actual = list.map(test, x => new string(x.Reverse().ToArray())).ToArray();
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void MapWithIntList()
        {
            List<int> test = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            List<int> expected = new List<int>() { 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 };
            List<int> actual = list.map(test, x => x * x).ToList();
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void MapWithStringList()
        {
            List<string> test = new List<string> { "aab", "bac", "ca", "c", "bbc", "acc", "abc" };

            List<string> expected = new List<string> { "baa", "cab", "ac", "c", "cbb", "cca", "cba" };
            List<string> actual = list.map(test, x => new string(x.Reverse().ToArray())).ToList();

            Assert.AreEqual(expected, actual);
        }

        #endregion

        #region FoldTests

        [Test]
        public static void FoldWithIntArray()
        {
            int[] test = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            int expected = 45;
            int actual = list.fold(test, (x, y) => x + y);
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FoldWithStringArray()
        {
            string[] test = { "aab", "bac", "ca", "c", "bbc", "acc", "abc" };

            string expected = "aabbaccacbbcaccabc";
            string actual = list.fold(test, (x, y) => x + y);
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FoldWithIntList()
        {
            List<int> test = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

            int expected = 45;
            int actual = list.fold(test, (x, y) => x + y);
            
            Assert.AreEqual(expected, actual);
        }
        [Test]
        public static void FoldWithStringList()
        {
            List<string> test = new List<string>() { "aab", "bac", "ca", "c", "bbc", "acc", "abc" };

            string expected = "aabbaccacbbcaccabc";
            string actual = list.fold(test, (x, y) => x + y);
            
            Assert.AreEqual(expected, actual);
        }

        #endregion
        
        
    }
}