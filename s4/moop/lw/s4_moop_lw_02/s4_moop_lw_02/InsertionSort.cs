using System;

namespace s4_moop_lw_02
{
    public static class InsertionSort
    {
        public static int[] Sort(int[] array)
        {
            if (array == null)
                throw new ArgumentException("ArgumentException: array can not be empty");

            for (int i = 1; i < array.Length; i++)
                if (array[i] < array[i - 1])
                    for (int j = i - 1; j != -1 && array[j + 1] < array[j]; j--)
                        (array[j], array[j + 1]) = (array[j + 1], array[j]);

            return array;
        }
    }
}
