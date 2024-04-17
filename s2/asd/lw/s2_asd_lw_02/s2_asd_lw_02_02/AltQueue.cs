using System;

namespace s2_asd_lw_02_02
{
    class AltQueue
    {
        private int[] Body = new int[Max];
        public static int Max = 100;
        public int Length = 0;
        public AltQueue() { }
        public AltQueue(int[] body)
        {
            Body = body;
            Length = body.Length;
        }
        public bool Full => Length > Max;
        public bool Empty => Length == 0;
        public void Add(int value)
        {
            if (Full) throw new Exception("Queue is full");
            Body[Length++] = value;
        }
        public int Peek => Body[0];
        public int Get()
        {
            if (Empty) throw new Exception("Queue is empty");
            int value = Peek;
            Length--;
            for (int i = 0; i < Length; i++)
            {
                Body[i] = Body[i + 1];
            }
            return value;
        }
        public void Clear()
        {
            for (int i = 0; i < Length; i++)
            {
                Body[i] = 0;
            }
            Length = 0;
        }
        public void Show()
        {
            for (int i = 0; i < Length; i++)
            {
                Console.Write($"[{Body[i]}] ");
            }
        }
    }
}
