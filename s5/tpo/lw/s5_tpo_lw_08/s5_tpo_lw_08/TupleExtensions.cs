namespace s5_tpo_lw_08;

public static class TupleExtensions
{
    public static (T2, T1) Reverse<T1, T2>(this (T1, T2) tuple) => (tuple.Item2, tuple.Item1);
}