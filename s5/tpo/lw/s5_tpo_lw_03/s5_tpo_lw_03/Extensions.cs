namespace s5_tpo_lw_03;

public static class DecimalExtensions
{
    public static decimal Pow(this decimal x, int n)
    {
        decimal result = 1;
        for (int i = 0; i < n; i++) result *= x;
        return result;
    }
}