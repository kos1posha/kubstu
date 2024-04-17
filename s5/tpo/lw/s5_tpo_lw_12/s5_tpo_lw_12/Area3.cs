namespace s5_tpo_lw_12;

public class Area3 : IArea
{
    public readonly decimal Radius;

    public Area3()
    {
        Radius = 1;
    }

    public Area3(decimal radius)
    {
        Radius = radius;
    }

    public bool IsPointInArea(decimal x, decimal y)
    {
        if ((x > 0 && y > 0) || (x < 0 && y < 0))
            return false;
        return _decSquare(x + Radius) + _decSquare(y - Radius) <= Radius ||
               (x >= 0 && x <= 2 * Radius && y <= 0 && y >= -Radius);
    }

    private static decimal _decSquare(decimal num) => num * num;
}