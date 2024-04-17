using System.Collections;
using NUnit.Framework;
using s5_tpo_lw_04;

namespace s5_tpo_lw_04_tests
{
    [TestFixture]
    public class StringExtensionsTestsWithTestCaseSource
    {
        public static IEnumerable TestCaseSource()
        {
            yield return new TestCaseData("ab", "abc").Returns("aabbc");
            yield return new TestCaseData("abc", "ab").Returns("aabbc");
        }
        
        [Test, TestCaseSource(nameof(TestCaseSource))]
        public string Merge_Test(string source, string mergedString)
        {
            return source.Merge(mergedString);
        }
    }
}