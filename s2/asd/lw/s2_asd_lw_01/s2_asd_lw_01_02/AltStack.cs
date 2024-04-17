using System;
using System.Collections.Generic;
using System.Text;

namespace s2_asd_lw_01_02
{
    class AltStack
    {
        private static int max = 100;
        private int[] altStack = new int[max];
        public int Count = 0;
        public bool Empty() => Count == 0;
        public bool Full() => Count == max;
        public int Peek() => altStack[Count - 1];
        public int Pop()
        {
            if (Empty()) throw new Exception("Exception: Stack is empty.");
            int pop = altStack[--Count];
            altStack[Count] = 0;
            return pop;
        }
        public void Push(int push)
        {
            if (Full()) throw new Exception("Exception: Stack overflow");
            altStack[Count++] = push;
        }
        public void Clear()
        {
            while (Count > 0) altStack[--Count] = 0;
        }
        public void Show()
        {
            int i = Count;
            while (i > 0) Console.WriteLine(altStack[--i]);
        }
    }
}
