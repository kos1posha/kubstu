using s5_tpo_lw_03;
using System;
using Xunit;

namespace s5_tpo_lw_03_tests;

public class MutantKillerTests
{
    [Fact]
    public void DecimalExtensions_Mutant8()
    {
        decimal num = 1m;
        decimal pow = num.Pow(0);
        Assert.Equal(1m, num);
        Assert.Equal(1m, pow);
    }

    [Fact]
    public void Point_Mutant15()
    {
        Point p = new();
        Assert.Throws<ArgumentException>(() => { p.IncludedInRegion_Task03(0); });
        Assert.Throws<ArgumentException>(() => { p.IncludedInRegion_Task03(-1); });
    }

    [Fact]
    public void Point_Mutant16() 
    {
        Point p = new(-1m, 0.1m);
        bool expected = false;
        bool actual = p.IncludedInRegion_Task03(1);
        Assert.Equal(expected, actual);

    }

    [Fact]
    public void Point_Mutant22()
    {
        Point p = new(-1m, 0.1m);
        int expectedArea = 2;
        int actualArea = p.IncludedInRegion_Task03_Test(1);
        Assert.Equal(expectedArea, actualArea);
    }

    [Fact]
    public void Point_Mutant31()
    {
        
    }

    [Fact]
    public void Point_Mutant34()
    {
        Point p = new();
        Assert.Throws<ArgumentException>(() => { p.IncludedInRectangle(0, 1, new Point()); });
        Assert.Throws<ArgumentException>(() => { p.IncludedInRectangle(-1, 1, new Point()); });
        Assert.Throws<ArgumentException>(() => { p.IncludedInRectangle(1, 0, new Point()); });
        Assert.Throws<ArgumentException>(() => { p.IncludedInRectangle(1, -1, new Point()); });
    }

    [Fact]
    public void Point_Mutant39()
    {
        Point p = new();
        Assert.Throws<ArgumentException>(() => { p.IncludedInCircle(0, new Point()); });
        Assert.Throws<ArgumentException>(() => { p.IncludedInCircle(-1, new Point()); });
    }
}
