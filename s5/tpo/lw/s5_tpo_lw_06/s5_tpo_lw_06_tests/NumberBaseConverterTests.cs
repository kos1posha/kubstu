using System;
using NUnit.Framework;
using static s5_tpo_lw_06.NumberBaseConverter;

namespace s5_tpo_lw_06_tests
{
    [TestFixture]
    public class NBCBlackBoxTests
    {
        // Классы эквивалентности:
        // 1) строка является положительным целым числом в 8-ричной системе счисления -> int
        // 2) строка не является целым числом -> ArgumentException
        // 3) строка является отрицательным целым числом -> ArgumentOutOfRangeException
        // 4) строка является положительным целым числом не в 8-ричной системе счисления -> FormatException

        [Test]
        [TestCase("0", 0), TestCase("1", 1), TestCase("4241", 2209)]
        public void Base8ToBase10_EquivalenceClass1_Test(string target, int expected)
            => Assert.AreEqual(expected, Base8ToBase10(target));

            [Test]
        [TestCase(""), TestCase("-"), TestCase("string")]
        public void Base8ToBase10_EquivalenceClass2_Test(string target) 
            => Assert.Throws<ArgumentException>(() => { Base8ToBase10(target); });

        [Test]
        [TestCase("-1"), TestCase("-2"), TestCase("-17000")]
        public void Base8ToBase10_EquivalenceClass3_Test(string target) 
            => Assert.Throws<ArgumentOutOfRangeException>(() => { Base8ToBase10(target); });

        [Test]
        [TestCase("8"), TestCase("9"), TestCase("6789")]
        public void Base8ToBase10_EquivalenceClass4_Test(string target) 
            => Assert.Throws<FormatException>(() => { Base8ToBase10(target); });
    }
    
    [TestFixture]
    public class NBCWhiteBoxTests
    {
        [Test]
        [TestCase("11", 9)]
        public void Base8ToBase10_Path1_Test(string target, int expected)
            => Assert.AreEqual(expected, Base8ToBase10(target));

        [Test]
        [TestCase("abc", typeof(ArgumentException))]
        public void Base8ToBase10_Path2_Test(string target, Type exception) 
            => Assert.Throws(exception, () => { Base8ToBase10(target); });

        [Test]
        [TestCase("-1000", typeof(ArgumentOutOfRangeException))]
        public void Base8ToBase10_Path3_Test(string target, Type exception) 
            => Assert.Throws(exception, () => { Base8ToBase10(target); });

        [Test]
        [TestCase("78", typeof(FormatException))]
        public void Base8ToBase10_Path4_Test(string target, Type exception) 
            => Assert.Throws(exception, () => { Base8ToBase10(target); });
    }
}