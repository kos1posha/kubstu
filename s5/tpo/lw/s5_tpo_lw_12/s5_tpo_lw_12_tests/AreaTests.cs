using Xunit;
using s5_tpo_lw_12;

namespace s5_tpo_lw_12_tests;

public class AreaTests
{
    [Fact]
    public void LeftTopInCircleCenter_False_Test()
    {
        Area3 area = new(3);
        bool actual = area.IsPointInArea(-3, 3);
        Assert.Equal(true, actual);
    }

    [Fact]
    public void LeftTopOnCircleBorder_False_Test()
    {
        Area3 area = new(3);
        bool actual1 = area.IsPointInArea(-3, 0);
        Assert.Equal(true, actual1);
        bool actual2 = area.IsPointInArea(-6, 3);
        Assert.Equal(true, actual2);
        bool actual3 = area.IsPointInArea(-3, 6);
        Assert.Equal(true, actual3);
        bool actual4 = area.IsPointInArea(0, 3);
        Assert.Equal(true, actual4);
    }

    [Fact]
    public void LeftTopOutCircle_False_Test()
    {
        Area3 area = new(3);
        bool actual1 = area.IsPointInArea(-0.1m, 0.1m);
        Assert.Equal(false, actual1);
        bool actual2 = area.IsPointInArea(-6, 6);
        Assert.Equal(false, actual2);
    }

    [Fact]
    public void RightBottomInRectangleCenter_True_Test()
    {
        Area3 area = new(3);
        bool actual = area.IsPointInArea(3, -1.5m);
        Assert.Equal(true, actual);
    }

    [Fact]
    public void RightBottomOnRectangleBorder_True_Test()
    {
        Area3 area = new(3);
        bool actual1 = area.IsPointInArea(0, 0);
        Assert.Equal(true, actual1);
        bool actual2 = area.IsPointInArea(6, 0);
        Assert.Equal(true, actual2);
        bool actual3 = area.IsPointInArea(6, -3);
        Assert.Equal(true, actual3);
        bool actual4 = area.IsPointInArea(-3, 0);
        Assert.Equal(true, actual4);
    }

    [Fact]
    public void RightBottomOutRectangle_True_Test()
    {
        Area3 area = new(3);
        bool actual1 = area.IsPointInArea(6.1m, -1.5m);
        Assert.Equal(false, actual1);
        bool actual2 = area.IsPointInArea(3, -3.1m);
        Assert.Equal(false, actual2);
    }

    [Fact]
    public void RightTop_False_Test()
    {
        Area3 area = new(3);
        bool actual = area.IsPointInArea(1, 1);
        Assert.Equal(false, actual);
    }

    [Fact]
    public void LeftBottom_False_Test()
    {
        Area3 area = new(3);
        bool actual = area.IsPointInArea(-1, -1);
        Assert.Equal(false, actual);
    }
}