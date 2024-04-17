using System;
using NUnit.Framework;
using s5_tpo_lw_04;

namespace s5_tpo_lw_04_tests
{
    [TestFixture]
    public class StringExtensionsTests
    {
        [Test]
        public void Merge_Path1_Test()
        {
            string source = "ab";
            string mergedString = "abc";

            string expected = "aabbc";
            string actual = source.Merge(mergedString);
            
            Assert.AreEqual(expected, actual);
        }
        
        [Test]
        public void Merge_Path2_Test()
        {
            string source = "abc";
            string mergedString = "ab";

            string expected = "aabbc";
            string actual = source.Merge(mergedString);
            
            Assert.AreEqual(expected, actual);
        }
    }
}