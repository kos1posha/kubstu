using System;

namespace s5_tpo_lw_03;

public class Point
{
    public decimal X;
    public decimal Y;

    public Point() => (X, Y) = (0, 0);
    public Point(decimal x, decimal y) => (X, Y) = (x, y);

    public bool IncludedInRegion_Task03(decimal r)
    {
        if (r <= 0) throw new ArgumentException();
        Point lb = new(-r, -r), lt = new(-r, r), rb = new(r, -r);
        return IncludedInRectangle(r * 2, r * 2, lb) && !IncludedInCircle(r, lt) && !IncludedInCircle(r, rb);
    }

    public int IncludedInRegion_Task03_Test(decimal r)
    {
        if (r <= 0) throw new ArgumentException();
        Point lb = new(-r, -r), lt = new(-r, r), rb = new(r, -r);
        if (!IncludedInRectangle(r * 2, r * 2, lb)) return 3;
        if (IncludedInCircle(r, lt) || IncludedInCircle(r, rb)) return 2;
        return 1;
    }

    public bool IncludedInRectangle(decimal w, decimal h, Point lb)
    {
        return w > 0 && h > 0
            ? lb.X <= X && X <= lb.X + w && lb.Y <= Y && Y <= lb.Y + h
            : throw new ArgumentException();
    }

    public bool IncludedInCircle(decimal r, Point c)
    {
        return r > 0
            ? (X - c.X).Pow(2) + (Y - c.Y).Pow(2) < r.Pow(2)
            : throw new ArgumentException();
    }
}