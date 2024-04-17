using System;
using s5_tpo_lw_03;
using Xunit;

namespace s5_tpo_lw_03_tests;

public class PointTests
{
    // Классы эквивалентности:
    // 1) точка входит в квадрат и не входит в окружности -> true
    // 2) точка входит в квадрат и в окружности -> false
    // 3) точка не входит в квадрат -> false
    // 4) входной радиус меньше нуля -> ArgumentException

    const decimal testRadius = 1;

    [Fact]
    public void Task3_EquivalenceClass1_Test()
    {
        Point testPoint_EC1 = new(1m, 0m);

        bool expected = true;
        bool actual = testPoint_EC1.IncludedInRegion_Task03(testRadius);
        Assert.Equal(expected, actual);

        int expectedArea = 1;
        int actualArea = testPoint_EC1.IncludedInRegion_Task03_Test(testRadius);
        Assert.Equal(expectedArea, actualArea);
    }

    [Fact]
    public void Task3_EquivalenceClass2_Test()
    {
        Point testPoint_EC2 = new(1m, -0.1m);

        bool expected = false;
        bool actual = testPoint_EC2.IncludedInRegion_Task03(testRadius);
        Assert.Equal(expected, actual);

        int expectedArea = 2;
        int actualArea = testPoint_EC2.IncludedInRegion_Task03_Test(testRadius);
        Assert.Equal(expectedArea, actualArea);
    }

    [Fact]
    public void Task3_EquivalenceClass3_Test()
    {
        Point testPoint_EC3 = new(1.1m, 0m);

        bool expected = false;
        bool actual = testPoint_EC3.IncludedInRegion_Task03(testRadius);
        Assert.Equal(expected, actual);

        int expectedArea = 3;
        int actualArea = testPoint_EC3.IncludedInRegion_Task03_Test(testRadius);
        Assert.Equal(expectedArea, actualArea);
    }

    [Fact]
    public void Task3_EquivalenceClass4_Test()
    {
        Point testPoint_EC4 = new();
        Assert.Throws<ArgumentException>(() => { testPoint_EC4.IncludedInRegion_Task03(-1); });
    }
}